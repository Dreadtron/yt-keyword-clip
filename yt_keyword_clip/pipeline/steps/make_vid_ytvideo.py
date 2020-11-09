from .step import Step
from yt_keyword_clip.model.ytvideo import YTVideo


class MakeVidYTVideo(Step):
    def process(self, data, inputs, utils):
        return [YTVideo(url) for url in data]
