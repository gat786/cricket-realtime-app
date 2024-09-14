from dotenv import load_dotenv
import os
import logging

load_dotenv()

logLevel = os.getenv("LOGLEVEL", 10)

logging.basicConfig(
  level=logLevel,
  format='%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s',
  datefmt='%Y-%m-%d %H:%M:%S'
)
