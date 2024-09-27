import logging
from logging.handlers import TimedRotatingFileHandler

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    handler = TimedRotatingFileHandler("/src/logs/app.log", when="midnight", interval=1)
    handler.suffix = "%Y-%m-%d"
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger

logger = setup_logging()