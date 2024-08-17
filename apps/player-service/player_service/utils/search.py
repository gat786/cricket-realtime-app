from player_service.utils import exports
import pandas as pd

import logging

logger = logging.getLogger()

def search_from_file(player_name: str, country_name: str):
  logger.debug(f"Player name supplied for searching: {[player_name]}")
  names_split           = player_name.split(" ")
  first_name, last_name = "", ""
  if len(names_split) > 1:
    first_name, last_name = names_split[0], names_split[-1]
  else: 
    first_name, last_name = names_split[0], ""
  logger.debug(f"FirstName: {first_name}, Second Name: {last_name}")
  with open(f"{exports.data_root}/player/players_data.csv") as player_csv_file:
    df: pd.DataFrame = pd.read_csv(player_csv_file)
    df["country_name_search"] = df["country_name"].str.lower()
    df["firstname_search"] = df["firstname"].str.lower()
    df["lastname_search"] = df["lastname"].str.lower()
    
    same_country = df[df["country_name_search"] == country_name]
    same_lastname = same_country[same_country["lastname_search"] == last_name]
    
    first_name = [x for x in first_name]
    first_letter = first_name[0]
    logger.debug(f"Searching for first letter - {first_letter}")
    closest_match = same_lastname[same_lastname["firstname_search"].str.startswith(first_letter)]
    
    closest_match.drop(columns=["country_name_search", "firstname_search", "lastname_search"], inplace=True)
    return closest_match
    
