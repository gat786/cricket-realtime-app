from dataclasses import dataclass

@dataclass
class RankingQuery:
  client_id:    str
  comp_type:    str = "test"
  type:         str = "bat"
  date:         str = "20240810"
  lang:         str = "en"
  feed_format:  str = "json"
