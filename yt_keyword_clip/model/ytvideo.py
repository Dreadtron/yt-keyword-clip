import os

from yt_keyword_clip.settings import CAP_DIR, VID_DIR

class YTVideo:
    def __init__(self, url):
        self.url = url
        self.id = self.url_vid_id(self.url)
        self.cap_dir = self.get_cap_dir()
        self.vid_dir = self.get_vid_dir()
        self.captions = None

    def __str__(self):
        return f"YTVideo<{self.id}>"

    def __repr__(self):
        content = " : ".join([
            "video url = " + str(self.url),
            "caption path = " + str(self.cap_dir),
            "video path = " + str(self.vid_dir_dir),
        ])
        return f"<Video:{self.id}-{content})>"

    @staticmethod
    def url_vid_id(url):
        return url.split("watch?v=")[-1]

    def get_cap_dir(self):
        return os.path.join(CAP_DIR, self.id + ".txt")

    def get_vid_dir(self):
        return os.path.join(VID_DIR, self.id + ".txt")