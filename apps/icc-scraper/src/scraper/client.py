import functools
import requests
import logging
from typing import List
import pandas as pd
from datetime import datetime
from requests import exceptions
from constants import date_fmt
from dateutil.relativedelta import relativedelta

import models
import models.clientconfig
import models.playerrank
import models.querymodel
import models.save_format
from constants import date_fmt

from templating import templatequery

import utils.load_env as local_env

from fs import io


base_url  = "https://assets-icc.sportz.io"
logger    = logging.getLogger()
@functools.lru_cache(maxsize=128)
def _get_client_config() -> models.clientconfig.ClientConfig | None:
  logger.info("Output is not cached, fetching from API")
  try:
    response = requests.get(f"{base_url}/static-assets/buildv3-stg/js/clientConfig.json")
    response.raise_for_status()
    clientConfig = response.json()
    clientConfig = models.clientconfig.ClientConfig(**clientConfig)
    return clientConfig
  except Exception as e:
    logger.warn(f"Getting client config failed with: {e.with_traceback()}")


def _get_ranking(
    rankings_url: str,
    client_id: str,
    comp_type: str,
    rank_for: str,
    date_to_fetch_for: str,
    failure_count: int = 0
  ):
  return_data = {}
  ranking_model = models.querymodel.RankingQuery(
    client_id = client_id,
    comp_type = comp_type,
    type      = rank_for,
    date      = date_to_fetch_for
  )
  logger.info(f"getting Data for {ranking_model}")
  templated_url = templatequery.template(
    query = rankings_url, 
    ranking_model = ranking_model
  )
  try:
    response = requests.get(templated_url)
    response.raise_for_status()
    data = response.json()
    if "data" in data:
      data_inside = data["data"]
      if "bat-rank" in data_inside:
        batsman_rank = data_inside["bat-rank"]
        
        if "rank_date" in batsman_rank:
          if batsman_rank["rank_date"] == None:
            last_updated_ts: str = batsman_rank["last_updated"]
            last_updated_ts = last_updated_ts[:last_updated_ts.find("T")]
            rank_date = last_updated_ts
            
            logger.warning(f"rank date is none, using last update ts as rank date: {rank_date}")
            # last_updated = datetime.fromisoformat(,"%Y-%m-%d")
          else:
            rank_date = batsman_rank["rank_date"]
        return_data["rank_date"] = rank_date
        if "rank" in batsman_rank:
          rankings = batsman_rank["rank"]
          logger.info(f"Ranking has items: {len(rankings)}")
          if type(rankings) == list:
            rankings_list = []
            for rank_item in rankings:
              p_rank_item = models.playerrank.PlayerRankingItem.model_validate(rank_item)
              if p_rank_item.no == "=":
                p_rank_item.no = previous_rank_number
              previous_rank_number = p_rank_item.no
              rankings_list.append(p_rank_item)
            return_data["ranks"] = rankings_list
            return return_data
          else:
            print("ranking is not a list")
        else:
          logger.info("rank not present")
      else:
        logger.info("bat-rank not present")
  except exceptions.HTTPError as e:
    if e.response.status_code == 404:
      logger.warning("Error fetching data for the current date, fetching for a backoff date")
      if failure_count < 5:
        backoff_list = [7, 14, 28, 56, 90]
        current_fetch_dt        = datetime.strptime(date_to_fetch_for, date_fmt)
        backoff_date: datetime  = current_fetch_dt - relativedelta(days = backoff_list[failure_count])
        backoff_date            = backoff_date.strftime(date_fmt)
        logger.warning(f"Trying to fetch for {backoff_date}")
        return _get_ranking(
          rankings_url=rankings_url,
          client_id=client_id,
          comp_type=comp_type,
          rank_for=rank_for,
          date_to_fetch_for=backoff_date,
          failure_count=failure_count + 1
        )
      else:
        logger.error("Reached limit backing off, Considering we have reached the end of data")
        exit(1)
  except Exception as e:
    logger.error(e)
    exit(1)
  return

def scrape_rankings(
    comp_type: str,
    rank_for: str,
    save: bool = False,
    save_fmt: models.save_format.SaveFormat = models.save_format.SaveFormat.json
  ):
  """
  This function scrapes the entire data that it can find for the specified comp_type
  & type from the current date till the date it can find and it will store it in 
  folders like `comp_type/type/date.json`

  comp_type is one of `test, odi, t20`

  rank_for is one of `team, bat, ball, allrounder`
  """

  date_fmt = """%Y%m%d"""
  current_date        = datetime.now().strftime(date_fmt)
  # date_to_fetch_for   = current_date
  date_to_fetch_for = "20231108"
  save_dir      = f"{local_env.OUTPUT_DIR}/{comp_type}/{rank_for}"
  io.create_folder(save_dir)

  logger.info("Fetching Client Config for latest config")
  client_config = _get_client_config()
  ranking_api = client_config.widgets["rankings"]
  past_exists = True
  while past_exists:
    if "page" in ranking_api:
      full_rankings_api           = ranking_api["page"]
      full_rankings_api_client_id = full_rankings_api["client_id"]
      logger.info(f"Client ID found for rankings: {full_rankings_api_client_id}")
      full_rankings_data_url      = full_rankings_api["dataApis"]["rankingMatchFormats"]["api"]
      
      output_file_name = f"{save_dir}/{date_to_fetch_for}.json"
      ranking_data = _get_ranking(
        rankings_url=full_rankings_data_url,
        client_id=full_rankings_api_client_id,
        comp_type=comp_type,
        rank_for=rank_for,
        date_to_fetch_for=date_to_fetch_for
      )
      if ranking_data is not None:
        ranking_data_df = pd.DataFrame(ranking_data["ranks"])
        ranking_data_df.to_json(
          path_or_buf=output_file_name,
          orient="records"
        )
        if "rank_date" in ranking_data:
          date_to_fetch_for = datetime.strptime(ranking_data["rank_date"],"%Y-%m-%d")
          date_to_fetch_for = date_to_fetch_for.strftime(date_fmt)
        else:
          logging.info(ranking_data)
      else:
        logger.info("We may have reached the end of data")
