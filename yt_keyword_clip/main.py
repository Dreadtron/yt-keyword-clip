import urllib.request
import json
from yt_keyword_clip.settings import YT_API_KEY


def get_all_video_in_channel(channel_id):
    api_key = os.getenv(YT_API_KEY)  # get environment variable with python-dotenv

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url + f'key={api_key}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25'

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
    return video_links


CHN_id = "UCJHA_jMfCvEnv-3kRjTCQXw"
links = get_all_video_in_channel(CHN_id)

print(len(links))
print(links)

