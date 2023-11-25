from player_service.utils import exports
import pandas as pd


def search_from_file(player_name: str, country_name: str):
  first_name, last_name = player_name.split(" ")
  print(f"Searching for {first_name} {last_name}")
  with open(f"{exports.data_root}/player/players_data.csv") as player_csv_file:
    df: pd.DataFrame = pd.read_csv(player_csv_file)
    df["country_name_search"] = df["country_name"].str.lower()
    df["firstname_search"] = df["firstname"].str.lower()
    df["lastname_search"] = df["lastname"].str.lower()
    
    same_country = df[df["country_name_search"] == country_name]
    same_lastname = same_country[same_country["lastname_search"] == last_name]
    
    first_name = [x for x in first_name]
    first_letter = first_name[0]
    print(f"Searching for first letter - {first_letter}")
    closest_match = same_lastname[same_lastname["firstname_search"].str.startswith(first_letter)]
    
    closest_match.drop(columns=["country_name_search", "firstname_search", "lastname_search"], inplace=True)
    return closest_match
    
