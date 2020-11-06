from yt_keyword_clip.pipeline.steps.step import Step, StepException


class Preflight(Step):
    def process(self, data, inputs, utils):
        print("In preflight")
        utils.make_dir()
