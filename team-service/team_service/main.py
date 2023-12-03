from team_service.utils import setup
from team_service.utils import exports

import uvicorn
import logging
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import pandas as pd

origins = [
  "http://localhost",
  "http://localhost:5173"
]

app     = FastAPI()
port    = 8000
logger  = logging.getLogger(__name__)

if exports.port.isnumeric():
  port  = int(exports.port)
    
@app.get("/")
def get_teams():
  return {
    "message": "Teams info can be retrieved from here"
  }
  
@app.get("/list")
def get_teams_list():
  with open(exports.data_root + "/player/teams.csv", "r") as f:
    csv_file_content = pd.read_csv(f,encoding="utf-8")
    
    teams_json = csv_file_content.to_json(orient="records",date_format="iso")
    
    return json.loads(teams_json)
  
@app.get("/{team_id}")
def get_team_from_name(team_id: str):
  with open(exports.data_root + "/player/teams.csv", "r") as f:
    csv_file_content = pd.read_csv(f,encoding="utf-8")
    
    teams_json = csv_file_content.to_json(orient="records",date_format="iso")
    
    teams = json.loads(teams_json)
    
    for team in teams:
      if team["name"].lower() == team_id.lower():
        return team
      if team["code"].lower() == team_id.lower():
        return team
    
    return {
      "message": "Team not found"
    }
  
app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

def run_app():
  uvicorn.run(
    "team_service.main:app", 
    host="0.0.0.0", 
    port=port, 
    reload=True
  )
