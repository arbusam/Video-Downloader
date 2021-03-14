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

<<<<<<< HEAD
    links = ["https://www.youtube.com/watch?v=d-diB65scQU"]

=======
links = ["https://www.youtube.com/watch?v=BaW_jenozKc"]

def start():
>>>>>>> 6c4f3e6c7fdaf43078ca631d623de4696030eca1
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(links)