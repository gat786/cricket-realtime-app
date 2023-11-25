from score_service.utils import setup
from score_service.utils import exports
import uvicorn

from fastapi import FastAPI
from score_service import filter

from score_service.paths.match import main as match

app     = FastAPI()
port    = 8000 
if exports.port.isnumeric():
  port    = int(exports.port)

@app.get("/")
def read_root():
  return {
    "message": "Hello World"
  }
  
app.mount("/match",match.app)


def main():
  uvicorn.run(
    "score_service.`main:app",
    host="0.0.0.0",
    port=port,
    reload=True,
  )
