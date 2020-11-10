from pytube import YouTube
from pytube.exceptions import RegexMatchError

from .step import Step
from yt_keyword_clip.settings import VID_DIR  # sreuslts.ytvideo.vid_dir is an absolute dir


class GetVidFile(Step):
    def process(self, data, inputs, utils):
        unique_sresult = set([sresults.ytvideo for sresults in data])
        print(f" Files needs to download: {len(unique_sresult)}")
        for ytvideo in unique_sresult:
            url = ytvideo.url
            id = ytvideo.id
            if utils.check_vid_dup(ytvideo):
                print(f"File <{id}> already exist, skipping...")
                continue
            print(f"Downloading <{id}>...")
            try:
                YouTube(url).streams.first().download(output_path=VID_DIR, filename=id)
            except RegexMatchError as e:
                print(f"!!! Pytube error: {e} for {url}")
                continue
        return data
