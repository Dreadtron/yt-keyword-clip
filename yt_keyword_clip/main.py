import sys
import getopt

from yt_keyword_clip.utils import Utils
from yt_keyword_clip.pipeline.pipeline import Pipeline
from yt_keyword_clip.pipeline.steps.preflight import Preflight
from yt_keyword_clip.pipeline.steps.get_vid_list import GetVidList
from yt_keyword_clip.pipeline.steps.make_vid_ytvideo import MakeVidYTVideo
from yt_keyword_clip.pipeline.steps.get_vid_cap import GetVidCap
from yt_keyword_clip.pipeline.steps.read_vid_cap import ReadVidCap
from yt_keyword_clip.pipeline.steps.search_vid_cap import SearchVidCap
from yt_keyword_clip.pipeline.steps.get_vid_file import GetVidFile
from yt_keyword_clip.pipeline.steps.make_vid_clip import MakeVidClip
from yt_keyword_clip.pipeline.steps.postflight import Postflight


def print_usage():
    print("python main.py OPTIONS")
    print("OPTIONS:")
    print("{:>6} {:<15}{}".format("-c", "--channel_id", "Target Youtube Channel"))
    print("{:>6} {:<15}{}".format("-k", "--keyword", "Keyword to search through video captions"))
    print("{:>6} {:<15}{}".format("-l", "--clip_limit", "Clip limit when combining clips"))


CHN_ID = "UCKSVUHI9rbbkXhvAXK-2uxA"
KeyWrd = "incredible"
ClpLmt = 30


def main():
    inputs = {
        "channel_id": CHN_ID,
        "keyword": KeyWrd,
        "clip_limit": ClpLmt,
    }

    # command line argument handling
    short_ops = "hc:k:l:"
    long_ops = "help channel_id= keyword= clip_limit=".split()
    try:
        opts, args = getopt.getopt(sys.argv[1:], short_ops, long_ops)
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print_usage()
            sys.exit(0)
        elif opt in ("-c", "--channel_id"):
            inputs["channel_id"] = arg
        elif opt in ("-k", "--keyword"):
            inputs["keyword"] = arg
        elif opt in ("-l", "--clip_limit"):
            inputs["clip_limit"] = arg

    if not CHN_ID or not KeyWrd or not ClpLmt:
        print_usage()
        sys.exit(2)

    # main execution
    steps = [
        Preflight(),
        GetVidList(),
        MakeVidYTVideo(),
        GetVidCap(),
        ReadVidCap(),
        SearchVidCap(),
        GetVidFile(),
        MakeVidClip(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == "__main__":
    main()





