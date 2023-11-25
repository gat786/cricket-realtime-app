from .utils import setup
import uvicorn

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
  return {
    "message": "Hello World"
  }


def main():
  uvicorn.run(
    "score_service.`main:app",
    host="0.0.0.0",
    port=8000,
    reload=True,
  )
