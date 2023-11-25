from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_players():
  return {
    "message": "Players info can be retrieved from here"
  }
  

@app.get("/{player_name}")
def get_player_from_name(player_name: str):
  return {
    "message": f"Player {player_name} info can be retrieved from here"
  }
