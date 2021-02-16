# My Video Downloader

## Usage:
Install the `tabulate` and `argparse` modules and run `python3 url_dump/main.py -h` for instructions.

## Table: **`url_dump`**

| Column Name | Column Properties |
| :---------: | :---------------- |
| `id` | - Integer <br /> - Primary Key <br /> - Auto-Incrementing |
| `url` | - YouTube video link <br /> (Example: https://www.youtube.com/watch?v=d-diB65scQU) |
| `created_date` | - Date and Time field <br /> - Must NOT be blank <br /> - Defaults to 'now' |
| `download_date` | - Date & Time when the video file was last downloaded |

<br />

## `url_dump` example in Excel
![Image of Excel Example](/docs/youtube_downloader_example.png)

<br />

## Table: **`youtube_links`**

| Column Name | Column Properties |
| ----------: | :---------------- |
| `video_id` | Auto incrementing positive number |
| `url` | Example: https://www.youtube.com/watch?v=d-diB65scQU |
| `title` | Bobby McFerrin - Don't Worry Be Happy (Official Video) |
| `publish_date` | Feb 25, 2009 |
| `channel_name` | The Real Bobby McFerrin |
| `channel_url` | https://www.youtube.com/channel/UCRo1OSKmBh6oxs6R0ANvINg |
| `download_date` | Date & Time when the video file was last **downloaded** |
| `processed_date` | Date & Time when the file was last **processed** |
| `filename_video` |  |
| `filename_audio` | |
| `filename_description` | |
| `filename_subtitles_en` | |
| `filename_info_json` | |
| `filename_thumbnail_webp` | |
| `filename_thumbnail_jpg` | |
| `video_codec` | x264, x265, xvid, ... |
| `video_resolution` | 1920x1080, 1080x720, ... |
| `video_frame_rate` | number of frames per second (25fps, 30fps etc) |
| `audio_codec` | mp3, aac, m4a, ... |
| `audio_sample_rate` | 44KHz, 48Khz, ... |

<br />

## Reference Links
- [**SQLite** - _Syntax_ Documentation](https://sqlite.org/lang.html "SQLite - Syntax Documentation")
- [**SQLite** - _Date And Time_ Functions](https://sqlite.org/lang_datefunc.html "SQLite - Date And Time Functions")
