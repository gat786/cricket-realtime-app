from dataclasses import dataclass
from typing import List

@dataclass
class ClientConfig:
  clientName:           str
  configCacheTime:      int
  refreshInterval:      int
  apiCacheTiming:       int
  defaultLanguage:      str
  isPushAllowed:        bool
  pushStream:           str
  baseAPIPath:          str
  intervalApi:          str
  common_apis:          dict
  clientDependencies:   List
  scheduleApiParams:    dict
  widgets:              dict
  vue:                  dict
  allowedTrans:         dict
  versions:             dict
  comp_labels:          dict
  comp_type_ids_list:   List
