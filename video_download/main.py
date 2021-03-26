from __future__ import unicode_literals
import youtube_dl
import colorama
from os.path import expanduser, dirname, realpath

# home = expanduser("~")
# print(home)

def start():
    filepath = realpath(__file__)
    sub_dir = dirname(realpath(__file__))
    parent_dir = dirname(dirname(realpath(__file__)))

    videos_dir = "[videos]"
    file_format_basename = "[%(channel)s]-[%(upload_date)s]-[%(title)s]-[%(id)s]"

    # Download formats
    AUDIO_VIDEO_720_MUX = "bestvideo[height=720][ext=mp4]+bestaudio[ext=m4a]/bestvideo[height=1080][ext=mp4]+bestaudio[ext=m4a]/best"
    AUDIO_ONLY = "bestaudio"

    download_format = AUDIO_VIDEO_720_MUXs


links = ["https://www.youtube.com/watch?v=BaW_jenozKc"]

def start():
    ydl_opts = {
        "outtmpl": videos_dir + file_format_basename + file_format_ext,
        "prefer_ffmpeg": True,
        "retries": 2,
        "keepvideo": False,
        "ignoreerrors": True,
        "addmetadata": True,
        "noplaylist": True,
        "continuedl": False,  # Try to continue downloads if possible
        "noprogress": True,  # Do not print the progress bar
        "writedescription": True,  # Write the video description to a .description file
        "writeinfojson": True,  # Write the video json data to a .info.json file
        "writesubtitles": True,
        "writeautomaticsub": True,
        "write-srt": True,
        "sub-lang": "en",
        "convert-subs": "srt",
        "add-video_infodata": True,
        "forcethumbnail": True,
        "writethumbnail": True,  # Write the thumbnail image to a file
        "format": download_format,
        "verbose": False,  # Print additional info to stdout
        "quiet": False,  # Print messages to stdout?
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(links)