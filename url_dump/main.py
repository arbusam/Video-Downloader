from .db import create_table, add_data, file_read

def addURLs():
    table_name = "url_dump"

    create_table(table_name)
    url = input("What URL(s) would you like to save (enter 'multi_select' for multiple)? ")
    if url == "multi_select":
        filepath = input("What is the path of the file? ")
        file_read(table_name, filepath)
    else:
        add_data(table_name, url)
