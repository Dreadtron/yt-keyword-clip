import logging
import os
from datetime import datetime

from yt_keyword_clip.settings import LOG_DIR


def main_logger():
    os.makedirs(LOG_DIR, exist_ok=True)

    # base logger
    logger = logging.getLogger("main_logger")
    logger.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter("%(asctime)s | %(levelname)s |%(message)s")
    log_time = datetime.now().strftime('%y-%m-%d')

    # file handler
    file_handler = logging.FileHandler(os.path.join(LOG_DIR, f"{log_time}.log"))
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    # stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.WARNING)
    stream_handler.setFormatter(file_formatter)
    logger.addHandler(stream_handler)


