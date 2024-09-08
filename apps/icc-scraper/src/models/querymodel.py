from dataclasses import dataclass
from enum import Enum

class CompType(str, Enum):
  test  = 1
  odi   = 2
  t20   = 3

class RankFor(str, Enum):
  bat         = 1
  bowl        = 2
  allrounder  = 3

@dataclass
class RankingQuery:
  client_id:    str
  comp_type:    str = "test"
  type:         str = "bat"
  date:         str = "20240810"
  lang:         str = "en"
  feed_format:  str = "json"
