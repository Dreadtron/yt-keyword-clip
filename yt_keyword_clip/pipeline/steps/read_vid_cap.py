import os

from pprint import pprint

from .step import Step
from yt_keyword_clip.settings import CAP_DIR


class ReadVidCap(Step):
    def process(self, data, inputs, utils):
        # {dict_cap_data} structure: {"cap_file": {"cap_content": "timestamp"}}
        # {dict_captions} structure: {"cap_content": "timestamp"}
        # cap_file: captions files. name structure: "(filename).txt"
        # time_stamp: boolean for whether this line is a caption timestamp
        # cap_time: caption timestamp. structure: "(time) --> (time)"
        # cap_content: caption itself. structure: "(captions)"
        dict_cap_data = {}
        for cap_file in os.listdir(CAP_DIR):
            dict_captions = {}
            with open(os.path.join(CAP_DIR,cap_file), "r") as caption:
                time_stamp = False
                cap_time = None
                cap_content = None
                for line in caption:
                    line = line.strip()
                    if "-->" in line:
                        time_stamp = True
                        cap_time = line
                        continue
                    if time_stamp:
                        cap_content = line
                        dict_captions[cap_content] = cap_time  # for loop will search for dict key
                        time_stamp = False
            dict_cap_data[cap_file] = dict_captions
        pprint(dict_cap_data)
        return dict_cap_data

