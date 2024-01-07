from player_service.utils import setup
from player_service.utils import exports

import uvicorn
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from player_service.utils import search

origins = [
  "http://localhost",
  "http://localhost:5173"
  "http://localhost:4173"
]
app     = FastAPI()
port    = 8000
logger  = logging.getLogger(__name__)

if exports.port.isnumeric():
  port  = int(exports.port)

class PlayerSearchQuery(BaseModel):
  name: str
  country_name: str

    
@app.get("/")
def get_players():
  return {
    "message": "Players info can be retrieved from here"
  }
  

@app.post("/search")
def get_player_from_name(player_search_query: PlayerSearchQuery):
  logger.debug(player_search_query)
  
  closest_matches = search.search_from_file(
    player_name=player_search_query.name.lower(),
    country_name=player_search_query.country_name.lower()
  )
  closest_matches.fillna("", inplace=True)
  return {
    "players": closest_matches.to_dict(orient="records")
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
    "player_service.main:app", 
    host="0.0.0.0", 
    port=port, 
    reload=True
  )
