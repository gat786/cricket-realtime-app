import uvicorn
import os
import json
import time
import asyncio
import logging
from json.decoder import JSONDecodeError

from score_service.utils import setup
from score_service.utils import exports

from fastapi import FastAPI, HTTPException, WebSocket
from fastapi.middleware.cors import CORSMiddleware

from score_service import filter
from score_service.utils import exports


origins = [
  "http://localhost",
  "http://localhost:5173",
  "http://localhost:4173"
]
data_root = exports.data_root
app     = FastAPI()
port    = 8000
logger  = logging.getLogger()
if exports.port.isnumeric():
  port    = int(exports.port)

@app.get("/")
def read_root():
  return {
    "message": "Welcome to score service"
  }

def get_match_info(match_json):
  match_info = match_json["info"]
  info_data = {}
  
  if "city" in match_info:
    info_data["city"] = match_info["city"]
  
  if "dates" in match_info:
    info_data["date"] = match_info["dates"][0]
  
  if "event" in match_info:
    info_data["event"] = match_info["event"]
    
  if "officials" in match_info:
    info_data["officials"] = match_info["officials"]
  
  if "players" in match_info:
    info_data["players"] = match_info["players"]
    
  if "teams" in match_info:
    info_data["teams"] = match_info["teams"]
    info_data["title"] = " vs ".join(match_info["teams"])
    
  if "toss" in match_info:
    info_data["toss"] = match_info["toss"]
  
  if "venue" in match_info:
    info_data["venue"] = match_info["venue"]
  
  return match_info

@app.websocket_route("/live/")
async def live_score(websocket: WebSocket):
  await websocket.accept()
  while True:
    data = await websocket.receive_text()
    print(f"received: {data}")
    try:
      message = json.loads(data)
      if "match_id" in message:
        match_id = message["match_id"]
        if os.path.exists(f"{data_root}/matches/{match_id}.json"):
          starting_stream_message = {
            "type": "information",
            "data": {
              "message": f"Match ID received starting match streaming for match {match_id}"
            }
          }
          await websocket.send_json(starting_stream_message)
          
          with open(f"{data_root}/matches/{match_id}.json") as f:
            match_json = json.load(f)
            match_info = get_match_info(match_json=match_json)
            
            match_details = {
              "type": "match_details",
              "data": {
                "match_id": match_id,
                "message": "Match Found below is the details about the match",
                "data": match_info
              }
            }
            
            await asyncio.sleep(1)
            await websocket.send_json(match_details)
            
            innings = match_json["innings"]
            
            for inning_number, inning in enumerate(innings):
              message = {
                "type": "information",
                "data": { 
                  "message": f"Starting Inning {inning_number + 1}"
                }
              }
              await websocket.send_json(message)
              overs = inning["overs"]
              for over in overs:
                over_no = over["over"]
                deliveries = over["deliveries"]
                for delivery_no_in_over, delivery in enumerate(deliveries):
                  await asyncio.sleep(5)
                  data_to_send = {
                    "type": "ball_data",
                    "data": {
                      "over": over_no,
                      "delivery": delivery_no_in_over,
                      "innings": inning_number,
                      "data": delivery
                    }
                  }
                  await websocket.send_json(data_to_send)
            
            
            await websocket.send_json({
                "type": "information",
                "data": {
                  "message": "Match Streaming Ended"
                }
              })
            await websocket.send_json({
              "type": "information",
              "data": {
                "message": "Result of the match"
              }
              }
            )
            
            await websocket.send_json({
              "type": "outcome", 
              "data" : match_info["outcome"] 
            })
        else:
          await websocket.send_json({
            "type": "error-message",
            "data": {
              "message": "Match ID Not Found, Please send a valid match id to start streaming"
            }
          }
        )
      else:
        message = {
          "type": "error-message",
          "data": {
            "message": "Match ID Not Found in the message",
            "help": "Please send a valid message in format {'match_id': 12345} where 12345 is match_id"
          }
        }
        await websocket.send_json(message)
    except JSONDecodeError as e:
      print("Exception is: ",e)
      message = {
        "type": "error-message",
        "data": {
          "message": "Invalid JSON",
          "help": "Please send a valid JSON in format {'match_id': 12345} where 12345 is match_id"
        }
      }
      await websocket.send_json(
        message
      )

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
        "message": "Match Found below is the data about the match",
        "match_id": match_id,
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
  logger.info("Starting up Score service")
  uvicorn.run(
    "score_service.main:app",
    host="0.0.0.0",
    port=port,
    reload=True,
  )
