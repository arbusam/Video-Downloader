import argparse
import youtube_dl
from colorama import init, Fore, Back, Style
from common import *
from .errors import *

def validate_url(url):
    extractors = youtube_dl.extractor.gen_extractors()
    for e in extractors:
        if e.suitable(url) and e.IE_NAME != "generic":
            return True

def display_arguments():
    parser = argparse.ArgumentParser(
        description=f"This application {Fore.LIGHTMAGENTA_EX}stores{Fore.RESET} one or more YouTube URL(s) into the {Fore.LIGHTMAGENTA_EX}database{Fore.RESET}.\nYou must add the links into the database {Fore.LIGHTMAGENTA_EX}before{Fore.RESET} they can be downloaded.",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    # 'url' argument
    parser.add_argument("-u", "--url", type=str, help="YouTube URL (link)")

    # 'file' argument
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        help="file containing YouTube URLs (one URL per line)",
    )

    # 'type' argument
    parser.add_argument(
        "-t",
        "--type",
        type=str,
        default=default_download_type,
        help=f"""
        Download type.
        Options are {Fore.GREEN}video{Fore.RESET}, {Fore.GREEN}audio{Fore.RESET}, {Fore.GREEN}thumb{Fore.RESET} (thumbnail), {Fore.GREEN}desc{Fore.RESET} (description), {Fore.GREEN}sub{Fore.RESET} (subtitles), {Fore.GREEN}json{Fore.RESET} (json file), {Fore.GREEN}all{Fore.RESET} (everything). Combine multiple options using {Fore.YELLOW}+{Fore.RESET} (for example: {Fore.YELLOW}video+audio+thumb{Fore.RESET}).""",
    )
    return parser

def validate_download_types(args):
    download_types = []
    video_passed = False
    for download_type in args.type.split("+"):
        if download_type == "all":
            download_types = file_types
            break
        if "video" in download_type:
            if video_passed != True:
                video_passed = True
            else:
                print(ONLY_ONE_VIDEO_ERROR)
                download_types = default_download_type.split("+")
                break
        if download_type in file_types:
            download_types.append(download_type)
        else:
            print(INVALID_TYPE_ERROR)
            download_types = default_download_type.split("+")
    return download_types