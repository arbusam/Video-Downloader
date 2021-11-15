from __future__ import unicode_literals
from colorama.ansi import Fore
import youtube_dl
from colorama import Fore
from os.path import expanduser, dirname, realpath
from common import db, config

# home = expanduser("~")
# print(home)

# User Defined
videos_dir = "videos"
file_format_basename = "[%(uploader)s]-[%(upload_date)s]-[%(title)s]-[%(id)s]"
file_format_ext = ".%(ext)s"

# Download formats
AUDIO_VIDEO_720_MUX = "bestvideo[height=720][ext=mp4]+bestaudio[ext=m4a]/bestvideo[height=1080][ext=mp4]+bestaudio[ext=m4a]/best"
AUDIO_ONLY = "bestaudio"

download_format = "best"

# home = expanduser("~")
filepath = realpath(__file__)
sub_dir = dirname(realpath(__file__))
parent_dir = dirname(dirname(realpath(__file__)))
videos_dir = parent_dir + "/" + videos_dir + "/"


# links = ["https://www.youtube.com/watch?v=BaW_jenozKc"]

ydl_opts = {
        "outtmpl": videos_dir + file_format_basename + file_format_ext,
        "prefer_ffmpeg": True,
        "retries": 2,
        "keepvideo": True,
        "ignoreerrors": True,
        "addmetadata": True,
        "noplaylist": True,
        "continuedl": False,  # Try to continue downloads if possible
        "noprogress": False,  # Do not print the progress bar
        "writedescription": False,  # Write the video description to a .description file
        "writeinfojson": False,  # Write the video json data to a .info.json file
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
        'audioformat' : "mp3", # convert to mp3 
    }

def download():
    data = db.read_from_table(config.db_table_url_dump, "ORDER BY ID ASC")

    links = []
    for row in data:
        links.append(row[1])

    types = []
    for row in data:
        types.append(row[2])

    ids = []
    for row in data:
        ids.append(row[0])

    for type in types:
        types_list = type.split("+")
        # find out if types_list has 'video' and 'audio'
        if 'video' in types_list and 'audio' in types_list:
            ydl_opts["format"] = "best"
        elif 'worstvideo' in types_list and 'worstaudio' in types_list:
            ydl_opts["format"] = "worst"
        elif 'video' in types_list and 'audio' not in types_list:
            ydl_opts["format"] = "bestvideo"
        elif 'audio' in types_list and 'video' not in types_list:
            ydl_opts["format"] = "bestaudio"

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for link in links:
            if data[links.index(link)][4] == None:
                ydl.download([link])
            else:
                continue
            ydl.download([link])
            db.update_download_date(config.db_table_url_dump, ids[links.index(link)])
        print(Fore.GREEN + "Finished downloading!" + Fore.YELLOW + " " + str(len(links)) + " " + Fore.RESET + "videos downloaded")
