import os
import logging

logger = logging.getLogger()

def create_folder(path: str):
  if not os.path.exists(path=path):
    try:
      os.makedirs(path) 
    except Exception as e:
      logger.error(f"Error creating the directory: {path}, {e}")