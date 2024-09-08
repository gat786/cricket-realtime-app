from jinja2 import Environment
from jinja2 import FileSystemLoader
from models import querymodel
import logging
import os

logger = logging.getLogger()

def template(
    query: str,
    ranking_model: querymodel.RankingQuery
  ):
  env = Environment(
      variable_start_string="{{", 
      variable_end_string="}}",
  )
  template = env.from_string(query)
  url = template.render(
    CLIENTID  = ranking_model.client_id,
    COMPTYPE  = ranking_model.comp_type,
    TYPE      = ranking_model.type,
    DATE      = ranking_model.date,
    LANG      = ranking_model.lang
  )

  logger.debug(f"Templated url: {url}")
  return url

  
