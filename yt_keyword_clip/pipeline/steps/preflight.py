import logging
from datetime import datetime

from yt_keyword_clip.pipeline.steps.step import Step, StepException


class Preflight(Step):
    def process(self, data, inputs, utils):
        log_time = datetime.now()
        logging.getLogger("main_logger").info(f"In preflight<{log_time}>")
        utils.make_dir()
