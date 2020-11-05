from yt_keyword_clip.pipeline.pipeline import Pipeline
from yt_keyword_clip.pipeline.steps.get_vid_list import GetVidList
from yt_keyword_clip.pipeline.steps.step import StepException

CHN_id = "UCJHA_jMfCvEnv-3kRjTCQXw"


def main():
    inputs = {
        "channel_id": CHN_id
    }
    steps = [
        GetVidList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == "__main__":
    main()

#



