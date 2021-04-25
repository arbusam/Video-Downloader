from .includes import *
from db import *
from .file import *

table_name = "url_dump"

def readURLs():
    init(autoreset=True)
    parser = argparse.ArgumentParser(description="This application stores YouTube URL(s) into the database.", formatter_class=argparse.RawTextHelpFormatter)

    # Here is an example showing how to use arguments in your code
    parser.add_argument("-u", "--url", type=str, help="Enter a URL to be added")
    parser.add_argument("-f", "--file", type=str, help="Enter a file containing URLs to be added (one URL per line)")
    parser.add_argument("-t", "--type", type=str, help=f"""Enter the download type
Options:
    {Fore.GREEN}video{Fore.RESET}         video file (default resolution of up to 720p)
    {Fore.GREEN}video480p{Fore.RESET}     video file (up to a resolution of 480p)
    {Fore.GREEN}video720p{Fore.RESET}     video file (up to a resolution of 720p)
    {Fore.GREEN}video1080p{Fore.RESET}    video file (up to a resolution of 1080p)
    {Fore.GREEN}audio{Fore.RESET}         audio file (mp3 format)
    {Fore.GREEN}thumb{Fore.RESET}         thumbnail image
    {Fore.GREEN}desc{Fore.RESET}          video description file
    {Fore.GREEN}sub{Fore.RESET}           subtitles file
    {Fore.GREEN}json{Fore.RESET}          JSON metadata file (from YouTube)
    {Fore.GREEN}all{Fore.RESET}           all of the above
    Combine multiple options with a {Fore.YELLOW}+{Fore.RESET}
    Default value: {Fore.GREEN}video+thumb+audio{Fore.RESET}
    Note: Do not add spaces around the {Fore.YELLOW}+{Fore.RESET}
""")

    args = parser.parse_args()
    create_table(table_name)

    link_list = []
    valid_url_list = []
    
    if args.url != None and args.file != None:
        print(URL_FILE_BOTH_PRESENT)
        exit()

    elif args.url != None:
        link_list = args.url
        
    elif args.file != None:

        link_list = file_read(table_name, args.file)

    try:
        if args.file != None:
            print(f"Found {Fore.BLUE}{len(link_list)}{Fore.RESET} lines in {Fore.YELLOW}{args.file}{Fore.RESET}")

    except TypeError:
        print(f"File {Fore.YELLOW} {str(args.file)} {Fore.WHITE} does {Fore.RED} not {Fore.WHITE} exist")
    
    if link_list != None:
        for url in link_list: 
            url = url.strip()
            if validate_url(url):
                # add the url to the valid_url_list[]
                valid_url_list.append(url)
                print(f"\t{url}{Fore.GREEN} valid")
            else:
                print(f"\t{url}{Fore.RED} invalid")


    # If there is atleast one valid link in the valid_url_list,
    duplicate = False
    if len(valid_url_list):
        for url in valid_url_list:
            data = read_from_table(table_name)
            url_data = []
            for entry_in_data in data:
                url_data.append(entry_in_data[1]) # Add the url from each data entry
            if url not in url_data:
                add_data(table_name, url)
            else:
                duplicate = True
        if duplicate:
            print("\n" + DUPLICATES + "\n")

    else:
        print(
            f"\n{Fore.RED}{len(valid_url_list)} {Fore.RESET}valid links. {Fore.RED}Nothing to process.{Fore.RESET}\n"
        )

    print(f"This is the {table_name} table:")
    print(tabulate(read_from_table(table_name), headers=["ID", "URL", "CREATED", "DOWNLOAD"], tablefmt="fancy_grid"))

    download_types = ["video, audio", "desc"]

    if args.type != None:
        download_types = []
        video_passed = False
        for download_type in args.type.split("+"):
            if download_type == "all":
                download_types = ["video", "audio", "thumb", "desc", "sub", "json"]
                break
            if "video" in download_type:
                if video_passed != True:
                    video_passed = True
                else:
                    print(ONLY_ONE_VIDEO_ERROR)
                    download_types = ["video", "audio", "thumb", "desc", "sub", "json"]
                    break
            if download_type == "video" or download_type == "video480p" or download_type == "video720p" or download_type == "video1080p" or download_type == "audio" or download_type == "thumb" or download_type == "desc" or download_type == "sub" or download_type == "json":
                download_types.append(download_type)
            else:
                print(INVALID_TYPE_ERROR)
                download_types = ["video", "audio", "thumb", "desc", "sub", "json"]
                break
                
    print(download_types)
    # TODO: Call video_download here


def addURL(url):

    create_table(table_name)
    
