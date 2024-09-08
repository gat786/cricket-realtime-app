import functools
import requests
import logging
from typing import List
import pandas as pd
from datetime import datetime

import models
import models.clientconfig
import models.playerrank
import models.querymodel
import models.save_format

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
    templated_url: str
  ):
  rankings_list = []
  try:
    response = requests.get(templated_url)
    response.raise_for_status()

    data = response.json()
    if "data" in data:
      data_inside = data["data"]
      if 'bat-rank' in data_inside:
        batsman_rank = data_inside['bat-rank']
        if 'rank' in batsman_rank:
          rankings = batsman_rank['rank']
          logger.info(f"type of rankings: {type(rankings)}")
          if type(rankings) == list:
            for rank_item in rankings:
              p_rank_item = models.playerrank.PlayerRankingItem.model_validate(rank_item)
              if p_rank_item.no == "=":
                p_rank_item.no = previous_rank_number
              previous_rank_number = p_rank_item.no
              rankings_list.append(p_rank_item)
            return rankings_list
          else:
            print('ranking is not a list')
        else:
          logger.info('rank not present')
      else:
        logger.info('bat-rank not present')
  except Exception as e:
    logger.error(e)
  return

def scrape_rankings(
    comp_type: str,
    type: str,
    save: bool = False,
    save_fmt: models.save_format.SaveFormat = models.save_format.SaveFormat.json
  ):
  """
  This function scrapes the entire data that it can find for the specified comp_type
  & type from the current date till the date it can find and it will store it in 
  folders like `comp_type/type/date.json`

  comp_type is one of `test, odi, t20`

  type is one of `team, bat, ball, allrounder`
  """

  date_fmt = """%Y%m%d"""
  current_date  = datetime.now().strftime(date_fmt)
  save_dir      = f"{local_env.OUTPUT_DIR}/{current_date}/{comp_type}/{type}"
  io.create_folder(save_dir)

  client_config = _get_client_config()
  ranking_api = client_config.widgets["rankings"]
  rankings_list = []
  if "page" in ranking_api:
    full_rankings_api           = ranking_api["page"]
    full_rankings_api_client_id = full_rankings_api["client_id"]
    full_rankings_data_url      = full_rankings_api["dataApis"]["rankingMatchFormats"]["api"]
    logger.info(f"{full_rankings_data_url}")
    templated_url = templatequery.template(
      query = full_rankings_data_url, 
      ranking_model = models.querymodel.RankingQuery(
        client_id = full_rankings_api_client_id,
      )
    )
    ranking_data = _get_ranking(templated_url=templated_url)
    ranking_data_df = pd.DataFrame(ranking_data)
    ranking_data_df.to_json(
      path_or_buf=f"{save_dir}/data.json",
      orient="records"
    )
