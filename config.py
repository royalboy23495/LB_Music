import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "24528020"))
API_HASH = getenv("API_HASH", "6d71c8d22ca45f4dd2ec073c510c07c6")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", 7116962630:AAFZsO_wz5iNxjam7AraXdhaMLq1yP-2MVM)

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", mongodb+srv://royalboy001144:Rishabh10031977@cluster0.jcznc3e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 180))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", -1002085205622))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7172177832"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("valentinaxmusicbot01")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("d994cb16-3b7d-4558-a559-a73edf83b536")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/Learningbots79/LB_Music", # dont Change this otherwise u get error 🧧
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ValentinaXSupport")
SUPPORT_CHAT = getenv("SUPPORT_GROUP", "https://t.me/VALENTINAXSUPPORTGROUP")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", BQBnW9k1bBLWVvuHiEnHaq7idWCjbS5232Vo9lHQalNWWqnnKAYtdAMx2aVRkDGXLOLf1Mz_Ufmlxjo6zS9WaalKTgFL2sSwuqTbf-1Dz4RWS5yaUgLIAvVqXEyJa7F1kIBbtE3REE6gEptTNRDlGPGVjFMHgtUPGiEZXga8-qnZL3h7j6FHheNqUm7kJeBTBTO9XgYjRW00PltZf9AF9176iWWBsLFBmyjio0dmai4B_6YMnm2Y3jN0_I24skPl7XqzzT80jOMEgbDt0P0WYxavnG0rgNyLr0j-7tS7RtQVVq2QRTlKZ8haRPDZbdbHXZ8o-1c9eYtJDIbz8iCtC9FXAAAAAat-v6gA)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/1ea57d01c705a708d6103.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/1ea57d01c705a708d6103.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/1ea57d01c705a708d6103.jpg"
STATS_IMG_URL = "https://graph.org/file/1ea57d01c705a708d6103.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/1ea57d01c705a708d6103.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
STREAM_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
