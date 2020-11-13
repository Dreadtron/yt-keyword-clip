import logging

from .step import Step
from yt_keyword_clip.model.sresults import SResults


class SearchVidCap(Step):
    def process(self, data, inputs, utils):
        keyword = inputs["keyword"]
        results = []
        for ytvideo in data:
            captions = ytvideo.captions
            if not captions:
                continue

            for cap_content in captions:
                if keyword in cap_content:
                    cap_time = captions[cap_content]
                    search_result = SResults(ytvideo, cap_content, cap_time)
                    results.append(search_result)
                    # print(f"Found <{keyword}> at <{cap_time}> in <{ytvideo.id}>")
        logging.getLogger("main_logger").info(f"Found {len(results)} matches")
        return results
