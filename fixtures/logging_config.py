import logging

LOG_FORMAT = "[%(asctime)s] %(levelname)s - %(filename)s: %(message)s"
logging.basicConfig(
    filename="logs/test.log",
    level=logging.INFO,
    format=LOG_FORMAT,
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger()
