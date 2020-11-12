from moviepy.editor import VideoFileClip, CompositeVideoClip, TextClip, concatenate_videoclips

from .step import Step


class MakeVidClip(Step):
    def process(self, data, inputs, utils):
        clips = []

        for result in data:
            vid_dir = result.ytvideo.vid_dir
            print(f"{result.cap_time}-limit:{len(clips)}/{inputs['clip_limit']}")
            start_time, end_time = self.process_timestamp(result.cap_time)

            vid_clip = VideoFileClip(vid_dir).subclip(start_time, end_time)
            clips.append(vid_clip)
            vid_clip.reader.close()  # this line sometimes prevent a moviepy error message after final_clip is generated
            if len(clips) > int(inputs["clip_limit"]):
                ans = input("Reached clip limit. Continue? (y/n)")
                if ans == "y":
                    limit = int(inputs["clip_limit"])
                    print("Add 20 to clip limit.")
                    inputs["clip_limit"] = limit + 20
                else:
                    print("Reached clip limit.")
                    break

        final_clip = concatenate_videoclips(clips)
        final_clip_path = utils.get_clip_dir(inputs["channel_id"], inputs["keyword"])
        final_clip.write_videofile(final_clip_path)

    def process_timestamp(self, cap_time):
        # timestamp structure: 00:00:08,300 --> 00:00:14,219
        start_time, end_time = cap_time.split(" --> ")
        return self.make_moviepy_timestamp(start_time), self.make_moviepy_timestamp(end_time)

    def make_moviepy_timestamp(self, timestamp):
        h, m, s = timestamp.split(":")
        s, ms = s.split(",")
        return int(h), int(m), int(s) + int(ms) / 1000
