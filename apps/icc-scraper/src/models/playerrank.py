from dataclasses import dataclass
from pydantic import BaseModel, Field
from typing import List

@dataclass
class PlayerRankingItem(BaseModel):
  no: int | str
  change: str
  Player_name: str = Field(alias="Player-name")
  Player_id: str
  Country_id: str
  Country_name: str 
  Country: str 
  team_id: int
  team_name: str
  Points: int 
  careerbest: str
  rankdate: str
  Player_url: str | None = Field(default="")
