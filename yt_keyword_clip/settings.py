import os
from dotenv import load_dotenv


load_dotenv()

YT_API_KEY = os.getenv("YT_API_KEY")

DOWNLOADS_DIR = "downloads"
CAP_DIR = os.path.join(DOWNLOADS_DIR, "captions")
VID_DIR = os.path.join(DOWNLOADS_DIR, "videos")
ClIP_DIR = os.path.join(DOWNLOADS_DIR, "clips")

