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
  rank_for:  querymodel.RankFor = querymodel.RankFor.bat,
  scrape_from_date: str =  datetime.now().strftime(date_fmt)
):
  output_dir = local_env.OUTPUT_DIR
  if output_dir == None or output_dir == "":
    logger.error("Please define an env `OUTPUT_DIR`. Cannot continue without it.")
    logger.error("Exiting..")
    exit(1)
  logger.info(f"Fetching Rankings for {comp_type.name}, {rank_for.name}")
  
  scrape_client.scrape_rankings(
    comp_type = comp_type.name,
    rank_for  = rank_for.name,
    scrape_from_date = scrape_from_date
  )

if __name__ == "__main__":
  logger.info("Welcome to ICC Scraper app")
  typer_app()
  
  # scrape_client.get_ranking()
  # example.try_jinja()
