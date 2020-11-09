from .step import Step


class ReadVidCap(Step):
    def process(self, data, inputs, utils):
        # {dict_captions} structure: {"cap_content": "timestamp"}
        # cap_file: captions files. name structure: "(filename).txt"
        # time_stamp: boolean for whether this line is a caption timestamp
        # cap_time: caption timestamp. structure: "(time) --> (time)"
        # cap_content: caption itself. structure: "(captions)"
        for ytvideo in data:
            if not utils.check_cap_dup(ytvideo):
                continue

            dict_captions = {}
            with open(ytvideo.cap_dir, "r") as caption:
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
            ytvideo.captions = dict_captions
        return data
