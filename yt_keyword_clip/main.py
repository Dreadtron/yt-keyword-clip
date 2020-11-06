from yt_keyword_clip.utils import Utils
from yt_keyword_clip.pipeline.pipeline import Pipeline
from yt_keyword_clip.pipeline.steps.preflight import Preflight
from yt_keyword_clip.pipeline.steps.get_vid_list import GetVidList
from yt_keyword_clip.pipeline.steps.get_vid_cap import GetVidCap
from yt_keyword_clip.pipeline.steps.postflight import Postflight

CHN_id = "UCKSVUHI9rbbkXhvAXK-2uxA"


def main():
    inputs = {
        "channel_id": CHN_id
    }
    steps = [
        Preflight(),
        GetVidList(),
        GetVidCap(),
        Postflight()
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == "__main__":
    main()





