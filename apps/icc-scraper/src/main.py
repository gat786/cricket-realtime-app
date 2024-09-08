from utils import setup
import logging
from scraper import client as scrape_client

logger = logging.getLogger()

if __name__ == "__main__":
  logger.info("Welcome to ICC Scraper app")
  scrape_client.get_ranking()
  # example.try_jinja()
