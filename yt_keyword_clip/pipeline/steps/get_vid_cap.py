import time
from pytube import YouTube
from pytube.exceptions import RegexMatchError

from .step import Step, StepException


class GetVidCap(Step):
    def process(self, data, inputs, utils):
        start = time.time()

        for url in data:
            if utils.check_cap_dup(url):  # check for duplicates
                print(f"File <{utils.url_vid_id(url)}> already exist, file skipped.")
                continue

            try:
                source = YouTube(url)
                en_caption = source.captions['en']
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
                print(f"File <{utils.url_vid_id(url)}> completed")
            except RegexMatchError as e:
                print(f"!!! Pytube error: {e} for {url}")
                continue
            except AttributeError as e:
                print(f"!!! Attribute error: {e} for {url}")

            # save the caption to a file
            text_file = open(utils.get_cap_dir(url), "w", encoding="utf-8")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        print(f"Took {time.time() - start} seconds.")
