# Video Downloader

## Sample YouTube Data

**Channel Name:** Royalty Free Music - No Copyright Music <br />
**Channel URL:** https://www.youtube.com/channel/UCQsBfyc5eOobgCzeY8bBzFg <br />
**Example Video:** https://www.youtube.com/watch?v=6c2hT_f5Q2g <br />

## Table: **`url_dump`**

| Column Name | Column Properties |
| :---------: | :---------------- |
| `id` | - Integer <br /> - Primary Key <br /> - Auto-Incrementing |
| `url` | - YouTube video link <br /> (Example: https://www.youtube.com/watch?v=6c2hT_f5Q2g) |
| `created_date` | - Date and Time field <br /> - Must NOT be blank <br /> - Defaults to 'now' |
| `download_date` | - Date & Time when the video file was last downloaded |

<br />

## Table: **`youtube_links`**

| Column Name | Column Properties |
| ----------: | :---------------- |
| `video_id` | Auto incrementing positive number |
| `url` | Example: https://www.youtube.com/watch?v=6c2hT_f5Q2g |
| `title` | Running Backwards - Pentium Beats | YouTube Royalty Free Music For Videos Download Free Music Chill |
| `publish_date` | Mar 19, 2021 |
| `channel_name` | Royalty Free Music - No Copyright Music |
| `channel_url` | https://www.youtube.com/watch?v=6c2hT_f5Q2g |
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
- [**youtube-dl** - Youtube-DL GitHub Page](https://github.com/ytdl-org/youtube-dl "Youtube-DL GitHub Page")


<br />

***

<br />

# Cron and Crontab


## Windows Users (only)

If you are a Windows user, please refer to the following article which explains how you can add a cron job or scheduled task on Windows (not relevant for Mac / Linux users).

- [How to add a cron job or scheduled task on Windows](https://www.schakko.de/2020/03/15/how-to-add-a-cron-job-scheduled-task-on-windows/ "How to add a cron job or scheduled task on Windows")



## Schedule jobs with crontab on macOS

Running scripts on your computer is great. Running them automatically is even greater. If you are on a Mac (or Linux), you can use our good friend `crontab`, which is a scheduling tool that will run jobs (scripts) at regular intervals.


## Create / Edit crontab jobs

Use the following command to open crontab in edit mode:

**`crontab -e`**



You add a job to crontab by editing the job list. A job is specified in the following format (first line):

![Image of crontab format](/docs/cron_job_example.png)


## Useful Link
- [Crontab Guru](https://crontab.guru/ "Crontab Guru")
- [How to save output or errors to a file with Linux shell redirection](https://www.thegeeksearch.com/how-to-save-output-or-errors-to-a-file-with-linux-shell-redirection/ "How to save output or errors to a file with Linux shell redirection")
- [BASH Shell Redirect Output and Errors To /dev/null](https://www.cyberciti.biz/faq/how-to-redirect-output-and-errors-to-devnull/ "BASH Shell Redirect Output and Errors To /dev/null")
- [How to redirect standard error in bash](https://www.cyberciti.biz/faq/how-to-redirect-standard-error-in-bash/ "How to redirect standard error in bash")



## Setting the script to run in crontab

On the Mac, we can use `crontab -e` to open an editor in Vim. Type `i` to enter *Insert Mode* which will allow you to edit the cron document. Once done, hit the `Escape` key to exit out of the Insert Mode. Next, type `:wq` to save and exit the crontab.

Here is an example python script that will execute every minute.

```shell
* * * * * say "Hi"; echo "Hello there. Can you see me on the terminal?"
```

**Note:** To comment out a crontab job, simply add a hash tag **#** in front of the line (crontab job).


## List active crontab jobs

Use the following command to list all your active crontab jobs:

**`crontab -l`**


## Delete all the cron job

Use the following command to delete all the cron jobs:

**`crontab -r`**


## Log the output of a crontab jobs

Consider the following crontab job example.

```shell
* * * * * cd /Users/captaincodeau/My_Git_Code/My_Video_Downloader_AARV; echo "Yo" 1>> cron/logs/output.txt 2>> cron/logs/errors.txt
```

Here the `1>>` redirects the standard **output** (if there is any) to `cron/logs/output.txt` and `2>>` redirects the standard **error** (if there is any) to `cron/logs/errors.txt`.

> Note that the `>>` represents 'append mode' and a single `>` represents 'write mode'. 


## Now try the following...

Copy the contents of `cron/sample_cron.txt` and paste them in your crontab using the command `crontab -e`. Remember to update the path with the appropriate path (as per your directory structure).

```shell
* * * * * cd /Users/captaincodeau/My_Git_Code/My_Video_Downloader_AARV; echo "Yo" 1>> cron/logs/output.txt 2>> cron/logs/errors.txt
```

> After about a minute, you will find 2 new files in your `/cron/logs` directory. Checkout the contents of each file. 

