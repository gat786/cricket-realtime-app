from fastapi import FastAPI
from pydantic import BaseModel

import logging

from player_service.utils import search

logger = logging.getLogger(__name__)

class PlayerSearchQuery(BaseModel):
  name: str
  country_name: str

app = FastAPI()

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
