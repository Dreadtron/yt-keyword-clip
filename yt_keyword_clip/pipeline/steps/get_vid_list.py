import urllib.request
import json

from yt_keyword_clip.pipeline.steps.step import Step
from yt_keyword_clip.settings import YT_API_KEY  # get environment variable with python-dotenv, see .env


class GetVidList(Step):

    def process(self, data, inputs, utils):
        channel_id = inputs["channel_id"]  # set all inputs as dict

        if utils.check_list_dup(channel_id):
            print(f"Found existing list of :[{channel_id}]")
            return self.read_list(utils.get_list_dir(channel_id))

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + f'key={YT_API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25'

        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                break
        print(video_links)
        self.list_to_file(video_links, utils.get_list_dir(channel_id))
        return video_links

    def list_to_file(self, video_links, file_path):
        with open(file_path, "w") as file:
            for url in video_links:
                file.write(url + "\n")

    def read_list(self, file_path):
        video_links = []
        with open(file_path, "r") as file:
            for url in file:
                video_links.append(url.strip())
        return video_links