from .includes import *
from .db import *

table_name = "url_dump"

def readURLs():
    init(autoreset=True)
    parser = argparse.ArgumentParser(description="This is the 'url_dump' module!")

    # Here is an example showing how to use arguments in your code
    parser.add_argument("-u", "--url", type=str, help="Enter a URL to be added")
    parser.add_argument("-f", "--file", type=str, help="Enter a file containing URLs to be added (one URL per line)")
    parser.add_argument("-t", "--type", type=str, help="Enter the download type to download with. Options: 'video', 'audio', 'desc'. (Conbine multiple options with a '+' ) Default value: 'video+audio'")

    args = parser.parse_args()
    create_table(table_name)

    link_list = []
    
    if args.url != None and args.file != None:
        print(URL_FILE_BOTH_PRESENT)
        quit()

    elif args.url != None:
        link_list = args.url
        
    elif args.file != None:

        link_list = file_read(table_name, args.file)

    try:
        print("Found " + Fore.BLUE + str(len(link_list)) + Fore.WHITE + " in " + Fore.YELLOW + args.file)
    except TypeError:
        print("File " + Fore.YELLOW + str(args.file) + Fore.WHITE + " does" + Fore.RED + " not " + Fore.WHITE + "exist")
    
    if link_list != None:
        for url in link_list:
            url = url.strip()
            if validate_url(url):
                add_data(table_name, url)
                print(Fore.WHITE + url + Fore.GREEN + " valid")
            else:
                print(Fore.WHITE + url + Fore.RED + " invalid")

    print(f"This is the {table_name} table:")
    print(read_from_table(table_name))

    download_type = {"video, audio"}

    if args.type != None:
        download_type = args.type.split("+")
    print(download_type)
    # TODO: Call video_download here


def addURL(url):

    create_table(table_name)
    
