import os
import json

from fastapi import FastAPI, HTTPException

from score_service import filter
from score_service.utils import exports

app = FastAPI()

@app.get("/")
def read_root():
  return {
    "message": "Welcome to match subpath"
  }

@app.get("/list")
def match_list():
  return {
    "list": filter.filter_files()
  }

@app.get("/{match_id}")
def get_match(match_id: str):    
  data_root = exports.data_root
  
  if os.path.exists(f"{data_root}/matches/{match_id}.json"):
    with open(f"{data_root}/matches/{match_id}.json") as match_file:
      match_json = json.load(match_file)
      
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
