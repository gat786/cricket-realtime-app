import functools
import requests
import logging
from typing import List
import pandas as pd

import models
import models.clientconfig
import models.playerrank
import models.querymodel
from templating import templatequery


base_url  = "https://assets-icc.sportz.io"
logger    = logging.getLogger()

@functools.lru_cache(maxsize=128)
def get_client_config() -> models.clientconfig.ClientConfig | None:
  logger.info("Output is not cached, fetching from API")
  try:
    response = requests.get(f"{base_url}/static-assets/buildv3-stg/js/clientConfig.json")
    response.raise_for_status()
    clientConfig = response.json()
    clientConfig = models.clientconfig.ClientConfig(**clientConfig)
    return clientConfig
  except Exception as e:
    logger.warn(f"Getting client config failed with: {e.with_traceback()}")


def get_ranking():
  client_config = get_client_config()
  ranking_api = client_config.widgets["rankings"]
  rankings_list = []
  if "page" in ranking_api:
    full_rankings_api           = ranking_api["page"]
    full_rankings_api_client_id = full_rankings_api["client_id"]
    full_rankings_data_url      = full_rankings_api["dataApis"]["rankingMatchFormats"]["api"]
    logger.info(f"{full_rankings_data_url}")
    templated_url = templatequery.template(full_rankings_data_url, models.querymodel.RankingQuery(
      client_id=full_rankings_api_client_id,
    ))
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
              
              df = pd.DataFrame(rankings_list)
              df.to_json(
                "batsman_rankings.json",
                orient="records"
              )
            else:
              print('ranking is not a list')
          else:
            logger.info('rank not present')
        else:
          logger.info('bat-rank not present')
        
    except Exception as e:
      logger.error(e)

  return
