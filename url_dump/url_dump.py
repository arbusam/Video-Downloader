from os import read
from .includes import *
from common import *
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
    # 'list' argument
    parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="list all URLs that are pending download",
    )

    # 'num' argument
    parser.add_argument(
        "-n",
        "--num",
        type=int,
        default=0,
        help="list the last 'num' URLs pending download (in reverse order)",
    )

    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="list the last 'num' URLs pending download (in reverse order)",
    )

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

    string_download_types = default_download_type
    download_types = default_download_type.split("+")

    if args.type != None:
        validated_types = validate_download_types(args)
        download_types = validated_types[0]
        if validated_types[1]:
            string_download_types = args.type
        else:
            string_download_types = default_download_type
        

    # If there is at least one valid link in the valid_url_list,
    duplicate = False
    
    if len(valid_url_list):
        add_data(db_table_url_dump, "url, type", [valid_url_list, string_download_types])
    else:
        print(
            f"\n{Fore.RED}{len(valid_url_list)} {Fore.RESET}valid links. {Fore.RED}Nothing to process.{Fore.RESET}\n"
        )

    if args.output != None and args.output != "":
        wb = Workbook()

        ws = wb.active
        ws.title = "URL Dump"
        
        ws = populate_headings(ws, headings)
        ws = populate_data(ws, read_from_table(db_table_url_dump, "ORDER BY ID ASC"))

        wb.save(filename=args.output)
                
    # TODO: Call video_download here


def addURL(url):
    create_table(table_name)
    
