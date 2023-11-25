from .utils import setup
from .utils import exports
from .models import match

from typing import List

import logging
import random

logger = logging.getLogger(__name__)

def filter_files():
  data_root = exports.data_root
  logger.info(f"data_root: {data_root}")
  
  logger.info("Reading readme file for all matches list")
  
  match_list = []
  
  with open(f"{data_root}/matches/README.txt") as match_list_file:
    file_match_list = match_list_file.read().splitlines() 
    for item in file_match_list:
      items = [n.strip() for n in item.split("-")]
      match_date          = f"{items[0]}-{items[1]}-{items[2]}"
      match_level         = items[3]
      match_game_type     = items[4]
      match_file_id       = items[6]
      match_player_gender = items[5]
      match_title         = items[7]
      match_list.append(
        match.Match(
          match_date          = match_date,
          match_player_gender = match_player_gender,
          match_level         = match_level,
          match_title         = match_title,
          match_file_id       = match_file_id,
          match_game_type     = match_game_type
        )
      )
  
  random_match_list = random.sample(match_list, 10)
  
  logging.debug(f"random_match_list: {random_match_list}")
  
  return random_match_list
