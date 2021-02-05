# Video-Downloader

# My_Video_Downloader_AARV
My Video Downloader (ver. Amen, Arhan, Riyaan, Vraj)

**Table 1 - 'url_dump'**
TABLE NAME
    - "url_dump"

TABLE COLUMNS
    - "id"
        - primary key
        - auto increment

    - "url"
        - web address
        - Example: https://www.youtube.com/watch?v=d-diB65scQU

    - "created_date"
        - date and time field (auto update/create)
        - when the url was added to your table

    - "download_date"
        - date time when the video was finally downloaded

**Table 2 - 'youtube_links'**
TABLE NAME
    - "youtube_links"

TABLE COLUMNS
    - "video_id"
        (Auto incrementing positive number)
    - "url"
        https://www.youtube.com/watch?v=d-diB65scQU
    - "title"
        Bobby McFerrin - Don't Worry Be Happy (Official Video)
    - "publish_date"
        Feb 25, 2009
    - "channel_name"
        The Real Bobby McFerrin
    - "channel_url"
        https://www.youtube.com/channel/UCRo1OSKmBh6oxs6R0ANvINg
- "download_date"
        (Date & time when the video was downloaded)
    - "processed_date"
        (Date & time when the video was PROCESSED)
    - "filename_video"
    - "filename_audio"
    - "filename_description"
    - "filename_subtitles_en"
    - "filename_info_json"
    - "filename_thumbnail_webp"
    - "filename_thumbnail_jpg"
- "video_codec" 
        (x264, x265, xvid,...)
    - "video_resolution"
        (1920x1080, 1080x720...)
    - "video_frame_rate"
        (number of frames per second... 25fps, 30fps..)
    - "audio_codec"
        (mp3, aac, m4a,....)
    - "audio_sample_rate"
        (44KHz, 48Khz...)