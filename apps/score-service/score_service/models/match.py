from dataclasses import dataclass
from typing import List


@dataclass
class Match:
  match_date:           str
  match_player_gender:  str
  match_level:          str
  match_game_type:      str
  match_title:          str
  match_file_id:        str
  match_teams:          List[str]
