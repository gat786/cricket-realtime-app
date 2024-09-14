import json
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import dotenv
import os

dotenv.load_dotenv()
# Configure logging to stream to console
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

catalog_file_path = os.getenv("CATALOG_FILE")
app = FastAPI()

# Load the JSON data
def load_player_data():
    try:
        with open(catalog_file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logger.error("Player data file not found")
        return []
    except json.JSONDecodeError:
        logger.error("Error decoding JSON data")
        return []

players = load_player_data()

class Player(BaseModel):
    id: str
    name: str
    full_name: str
    gender: str
    nationality: str
    skill: str
    role: str
    batting_style_name: str
    bowling_style_name: str
    debut: str
    date_of_birth: str

@app.get("/searchPlayer")
async def search_player(fname: str, lname: str):
    logger.info(f"Searching for player: {fname} {lname}")
    full_name = f"{fname} {lname}".lower()
    matching_players = [
        Player(**p) for p in players 
        if full_name in p['full_name'].lower() or full_name in p['name'].lower()
    ]
    
    if not matching_players:
        logger.warning(f"No players found for: {fname} {lname}")
        raise HTTPException(status_code=404, detail="No players found")
    
    logger.info(f"Found {len(matching_players)} matching players")
    return matching_players

@app.get("/starPlayerOfTheDay")
async def star_player_of_the_day():
    # Placeholder for future implementation
    logger.info("Star Player of the Day endpoint accessed")
    return {"message": "Star Player of the Day feature coming soon!"}

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the Cricket Player API"}

if __name__ == "__main__":
    logger.info("Starting the Cricket Player API")
    uvicorn.run(app, host="0.0.0.0", port=8000)