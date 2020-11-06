from yt_keyword_clip.pipeline.steps.step import Step, StepException


class Postflight(Step):
    def process(self, data, inputs, utils):
        print("In postflight")