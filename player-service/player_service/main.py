from player_service.utils import setup
from player_service.utils import exports

import uvicorn
from fastapi import FastAPI

from player_service.paths.players import main as players

app   = FastAPI()
port  = 8000
if exports.port.isnumeric():
  port  = int(exports.port)
  

@app.get("/")
def read_root():
  return {
    "message": "Hello World",
    "greetings": "I am Player Service use my /players endpoints to get player info"
  }

app.mount("/players", players.app)

def run_app():
  uvicorn.run(
    "player_service.main:app", 
    host="127.0.0.1", 
    port=port, 
    reload=True
  )
