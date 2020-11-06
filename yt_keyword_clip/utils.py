import os
from yt_keyword_clip.settings import DOWNLOADS_DIR, CAP_DIR, VID_DIR


class Utils:
    def __init__(self):
        pass

    def make_dir(self):
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(CAP_DIR, exist_ok=True)
        os.makedirs(VID_DIR, exist_ok=True)

    def get_list_dir(self, channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + ".txt")

    def check_list_dup(self, channel_id):
        path = self.get_list_dir(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    @staticmethod
    def url_vid_id(url):
        return url.split("watch?v=")[-1]

    def get_cap_dir(self, url):
        return os.path.join(CAP_DIR, self.url_vid_id(url) + ".txt")

    def check_cap_dup(self, url):
        path = self.get_cap_dir(url)
        return os.path.exists(path) and os.path.getsize(path) > 0
