from .db import create_table, add_data, file_read
import argparse

table_name = "url_dump"

def readURLs():
    parser = argparse.ArgumentParser(description="This is the 'url_dump' module!")

    # Here is an example showing how to use arguments in your code
    parser.add_argument("-u", "--url", type=str, help="Enter a URL to be added")
    parser.add_argument("-f", "--file", type=str, help="Enter a file containing URLs to be added (one URL per line)")

    args = parser.parse_args()
    create_table(table_name)
    print(args.url)
    print(args.file)

    if args.url == None and args.file == None: # If the user doesn't pass any arguments on run time.
        url = input("What URL(s) would you like to save (enter 'multi_select' for multiple)? ")
        if url == "multi_select":
            filepath = input("What is the path of the file? ")
            file_read(table_name, filepath)
        elif url != "": # Making sure the app doesn't crash if the user doesn't type anything.
            file_read(table_name, args.file)
    
    if args.url != None:
        add_data(table_name, args.url)
    if args.file != None:
        file_read(table_name, args.file)


def addURL(url):

    create_table(table_name)
    
