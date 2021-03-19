from .db import create_table, add_data, file_read, read_from_table
import argparse
from colorama import init, Fore, Back, Style

table_name = "url_dump"

def readURLs():
    parser = argparse.ArgumentParser(description="This is the 'url_dump' module!")

    # Here is an example showing how to use arguments in your code
    parser.add_argument("-u", "--url", type=str, help="Enter a URL to be added")
    parser.add_argument("-f", "--file", type=str, help="Enter a file containing URLs to be added (one URL per line)")

    args = parser.parse_args()
    create_table(table_name)
    
    if args.url != None:
        add_data(table_name, args.url)
    if args.file != None:
        file_read(table_name, args.file)

    print(f"This is the {table_name} table:")
    print(read_from_table(table_name))


def addURL(url):

    create_table(table_name)
    
