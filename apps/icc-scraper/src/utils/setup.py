from dotenv import load_dotenv
import coloredlogs
import logging
import os

load_dotenv()

grey = "\x1b[38;20m"
yellow = "\x1b[33;20m"
red = "\x1b[31;20m"
bold_red = "\x1b[31;1m"
reset = "\x1b[0m"

log_format = "%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s"

logging.basicConfig(
  level=logging.DEBUG,
)

coloredlogs.install(
  logging.INFO,
  fmt=log_format,
  datefmt="%Y-%m-%m %H:%M:%S"
)


