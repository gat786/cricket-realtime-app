from utils import setup
import utils.load_env as local_env
import logging
from scraper import client as scrape_client
from datetime import datetime
from dateutil.relativedelta import relativedelta

logger = logging.getLogger()

if __name__ == "__main__":
  logger.info("Welcome to ICC Scraper app")
  date_fmt = """%Y%m%d"""
  current_date = datetime.now().strftime(date_fmt)
  start_date   = (datetime.strptime(current_date,date_fmt) - relativedelta(years = 10)).strftime(date_fmt)
  logger.info(f"curr: {current_date}, past: {start_date}")
  scrape_client.scrape_rankings(
    comp_type='test',
    type='bat'
  )
  # scrape_client.get_ranking()
  # example.try_jinja()
