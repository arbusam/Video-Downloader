from .includes import *

def file_read(tableName, filepath):

    try:
        f = open(filepath, "r")
    except FileNotFoundError:
        print(FILE_NOT_FOUND)
        return
    except ModuleNotFoundError:
        print(FILE_NOT_FOUND)
        return
    else:
        link_list = f.readlines()
        f.close()
        print(link_list)
    return link_list
    

    # while True:
    #     url = f.readline()
    #     if url != "":
    #         add_data(tableName, url)
    #     else:
    #         break