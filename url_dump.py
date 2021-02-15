# Calling this file will add the URL
# into the 'url_dump' table.

# Homework Tasks
# 1. Create a table 'url_dump' if not exists.
# 2. Accept the URL from the user.
# 3. Finally, add that into the 'url_dump' table.
# Optional
# 4. Add the ability to provide a filename containing
#    a list of URLs (one URL per line).

from db import create_table, add_data, file_read

table_name = "url_dump"

create_table(table_name)
url = input("What URL(s) would you like to save (enter 'multi_select' for multiple)? ")
if url == "multi_select":
    filepath = input("What is the path of the file? ")
    file_read(table_name, filepath)
else:
    add_data(table_name, url)
