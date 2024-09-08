import functools
import requests
import logging
from string import Template


import models
import models.clientconfig

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
  if "page" in ranking_api:
    full_rankings_api           = ranking_api["page"]
    full_rankings_api_client_id = full_rankings_api["client_id"]
    full_rankings_data_url      = full_rankings_api["dataApis"]["rankingMatchFormats"]["api"]
    logger.info(f"{full_rankings_data_url}")
  return
