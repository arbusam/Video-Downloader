db_name = "./common/db.sqlite"

# Default download 'type' for url_dump
default_download_type = "video+thumb+desc"

file_types = {
    "video": "\tvideo file (max. default resolution of 720p)",
    "video480p": "video file (up to 480p resolution)",
    "video720p": "video file (up to 720p resolution)",
    "video1080p": "video file (up to 1080p resolution)",
    "audio": "\taudio file (.mp3 format)",
    "thumb": "\tthumbnail image file",
    "desc": "\tvideo description file",
    "sub": "\tsubtitles file",
    "json": "\tJSON metadata file (from YouTube)",
    "all": "\tall standard formats (video+audio+thumb+desc+sub+json)",
}