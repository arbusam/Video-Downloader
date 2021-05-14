from colorama import init, Fore, Back, Style

URL_FILE_BOTH_PRESENT = Fore.RED + "Either URL or the Filename are allowed. But not both!"
FILE_NOT_FOUND = Fore.RED + "The file provided does not exist."
DUPLICATES = Fore.WHITE + f"One or more of the URLs provided are either {Fore.RED}already in the table {Fore.RESET}or {Fore.RED}are duplicates in the file. Those URLs will not be added."
INVALID_TYPE_ERROR = Fore.RED + "Invalid type passed in. Reverting to default types."