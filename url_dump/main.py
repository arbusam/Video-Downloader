from .includes import *
from .db import *
from .file import *

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
    valid_url_list = []
    
    if args.url != None and args.file != None:
        print(URL_FILE_BOTH_PRESENT)
        exit()

    elif args.url != None:
        link_list = args.url
        
    elif args.file != None:

        link_list = file_read(table_name, args.file)

    try:
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
    if len(valid_url_list):
        for url in valid_url_list:
            data = read_from_table(table_name)
            url_data = []
            for entry_in_data in data:
                url_data.append(entry_in_data[1]) # Add the url from each data entry
            if url not in url_data:
                add_data(table_name, url)
    else:
        print(
            f"\n[ {Fore.RED}{len(valid_url_list)} {Fore.RESET}valid links. {Fore.RED}Nothing to process.{Fore.RESET} ]"
        )
        exit() 

    print(f"This is the {table_name} table:")
    print(tabulate(read_from_table(table_name), headers=["ID", "URL", "CREATED", "DOWNLOAD"], tablefmt="fancy_grid"))

    download_type = {"video, audio"}

    if args.type != None:
        download_type = args.type.split("+")
    print(download_type)
    # TODO: Call video_download here


def addURL(url):

    create_table(table_name)
    
