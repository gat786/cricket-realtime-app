import os
import logging

logger = logging.getLogger()

def create_folder(path: str):
  is_present = os.path.exists(path=path)
  if not is_present:
    try:
      os.makedirs(path)
    except Exception as e:
      logger.error(f"Error creating the directory: {path}, {e}")
