import time
from multiprocessing import Process

from pytube import YouTube
from pytube.exceptions import RegexMatchError

from .step import Step, StepException


class GetVidCap(Step):
    def process(self, data, inputs, utils):
        processes = []
        start = time.time()

        for i in range(4):
            processes.append(Process(target=self.getvidcap, args=(data, utils)))
        print(processes)
        for process in processes:
            process.start()
        for process in processes:
            process.join()

        print(f"Took {time.time() - start} seconds.")
        return data

    def getvidcap(self, data, utils):
        for ytvideo in data:
            if utils.check_cap_dup(ytvideo):  # check for duplicates
                print(f"File <{ytvideo.id}> already exist, file skipped.")
                continue

            try:
                source = YouTube(ytvideo.url)
                en_caption = source.captions['en']
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
                print(f"File <{ytvideo.url_vid_id(ytvideo.url)}> completed")
            except RegexMatchError as e:
                print(f"!!! Pytube error: {e} for {ytvideo.url}")
                continue
            except AttributeError as e:
                print(f"!!! Attribute error: {e} for {ytvideo.url}")
                continue
            except KeyError as e:
                print(f"!!! Key error: {e} for {ytvideo.url}")
                continue

            # save the caption to a file
            text_file = open(ytvideo.get_cap_dir(), "w", encoding="utf-8")
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
