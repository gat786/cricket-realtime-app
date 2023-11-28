import uvicorn
import os
import json
import time
import asyncio

from score_service.utils import setup
from score_service.utils import exports

from fastapi import FastAPI, HTTPException, WebSocket
from fastapi.middleware.cors import CORSMiddleware

from score_service import filter
from score_service.utils import exports


origins = [
  "http://localhost",
  "http://localhost:5173"
]
data_root = exports.data_root
app     = FastAPI()
port    = 8000 
if exports.port.isnumeric():
  port    = int(exports.port)

@app.get("/")
def read_root():
  return {
    "message": "Welcome to score service"
  }

def get_match_info(match_json):
  match_info = match_json["info"]
  info_data = {
    "city": match_info["city"],
    "date": match_info["dates"][0],
    "event": match_info["event"],
    "officials": match_info["officials"],
    "players": match_info["players"],
    "teams": match_info["teams"],
    "toss": match_info["toss"],
    "venue": match_info["venue"]
  }
  
  return match_info

@app.websocket("/live/")
async def live_score(websocket: WebSocket):
  await websocket.accept()
  while True:
    data = await websocket.receive_text()
    try:
      message = json.loads(data)
      if "match_id" in message:
        match_id = message["match_id"]
        if os.path.exists(f"{data_root}/matches/{match_id}.json"):
          await websocket.send_text("Match ID received starting match streaming")
          
          with open(f"{data_root}/matches/{match_id}.json") as f:
            await websocket.send_text("Match Found below is the data about the match")
            match_json = json.load(f)
            match_info = get_match_info(match_json=match_json)
            
            await asyncio.sleep(1)
            await websocket.send_text(json.dumps(match_info))
            
            innings = match_json["innings"]
            
            for inning_number, inning in enumerate(innings):
              await websocket.send_text(f"Starting Inning {inning_number + 1}")
              overs = inning["overs"]
              for over in overs:
                over_no = over["over"]
                deliveries = over["deliveries"]
                for delivery_no_in_over, delivery in enumerate(deliveries):
                  await asyncio.sleep(5)
                  data_to_send = {
                    "over": over_no,
                    "delivery": delivery_no_in_over,
                    "data": delivery
                  }
                  await websocket.send_text(json.dumps(data_to_send))
            
            
            await websocket.send_text("Match Streaming Ended")
            await websocket.send_text("Result of the match")
            await websocket.send_json(match_info["outcome"])
        else:
          await websocket.send_text("Match ID Not Found, Please send a valid match id to start streaming")
      else:
        await websocket.send_text("Match ID Not Found in the message")
        await websocket.send_text("Please send a valid message in format {'match_id': 12345} where 12345 is match_id")
    except Exception as e:
      print(e)
      await websocket.send_text("Invalid JSON")        

@app.get("/list")
def match_list():
  return {
    "match_list": filter.filter_files()
  }

@app.get("/{match_id}")
def get_match(match_id: str):
  if os.path.exists(f"{data_root}/matches/{match_id}.json"):
    with open(f"{data_root}/matches/{match_id}.json") as match_file:
      match_json = json.load(match_file)
      info_data = get_match_info(match_json)
      return {
        "match_id": "Match Found below is the data about the match",
        "data": info_data
      }
  else:
    raise HTTPException(
      status_code=404,
      detail={
        "reason": "Match Not Found",
        "message": "Please use a proper match id to get the match data"
      }
    )

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

def main():
  uvicorn.run(
    "score_service.main:app",
    host="0.0.0.0",
    port=port,
    reload=True,
  )
