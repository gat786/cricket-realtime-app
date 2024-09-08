from utils import setup
import utils.load_env as local_env
import logging
from scraper import client as scrape_client
from datetime import datetime
from dateutil.relativedelta import relativedelta
from constants import date_fmt
from typer import Typer
from models import querymodel

typer_app = Typer()
logger = logging.getLogger()

@typer_app.command()
def fetch_rankings(
  comp_type: querymodel.CompType = querymodel.CompType.odi,
  rank_for:  querymodel.RankFor = querymodel.RankFor.bat
):
  logger.info(f"Fetching Rankings for {comp_type.name}, {rank_for.name}")
  
  scrape_client.scrape_rankings(
    comp_type = comp_type.name,
    rank_for  = rank_for.name
  )

if __name__ == "__main__":
  logger.info("Welcome to ICC Scraper app")
  typer_app()
  
  # scrape_client.get_ranking()
  # example.try_jinja()
