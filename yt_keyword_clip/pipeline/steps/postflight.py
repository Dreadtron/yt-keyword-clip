import logging
import datetime

from yt_keyword_clip.pipeline.steps.step import Step, StepException


class Postflight(Step):
    def process(self, data, inputs, utils):
        log_time = datetime.now()
        logging.getLogger("main_logger").info(f"In postflight<{log_time}>")