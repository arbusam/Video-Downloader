# Turning off 'Python BLACK Formatter' for this file
# fmt: off
from colorama import init, Fore, Back, Style

FILE_NOT_FOUND = Fore.RED + "The file provided does not exist."

URL_FILE_BOTH_PRESENT = "URL and Filename provided. Only one of them is allowed."
URL_FILE_NEITHER_PRESENT = "Neither URL nor Filename provided. One of them is required."
URL_VALIDATION_ERROR = "There was an error validating the URL."
URLS_VALIDATION_ERROR = "There was an error validating one of the URLs."

INVALID_DOWNLOAD_TYPE = "{type}" + Fore.RED + "\t[invalid]" 
BOTH_URL_AND_FILE_PRESENT = "\n" + Fore.RED + "URL and Filename provided. Only one of them is allowed."
NEITHER_URL_OR_FILE_PRESENT = "\n" + Fore.RED + "Neither URL nor Filename provided. One of them is required."

VALIDATING_TYPE = "\n" + Fore.YELLOW + "Validating download type(s): " + Fore.RESET + "{type}"
INVALID_DOWNLOAD_TYPE = "{type}" + Fore.RED + "\t[invalid]"

FILE_DOES_NOT_EXIST = "\n" + Fore.RED + "File not found: " + Fore.YELLOW + "{file}"
FOUND_ENTRIES_IN_FILE = "\n" + Fore.YELLOW + "Found " + Fore.LIGHTBLUE_EX + "{num}" + Fore.YELLOW + " entries in " + Fore.RESET + "{file}" + Fore.YELLOW + "."
VALIDATING_LINKS_FROM_FILE = "\n" + Fore.YELLOW + "Validating" + Fore.LIGHTBLUE_EX + " {num} " + Fore.YELLOW + "link(s) from "  + Fore.RESET + "{file}" + Fore.YELLOW + " file:"

LINK_VALID = "\t" + Fore.GREEN + "{link}"
LINK_INVALID = "\t" + Fore.RED + "{link}"

ADDING_LINKS_TO_DB = "\n" + Fore.YELLOW + "Inserting" + Fore.LIGHTBLUE_EX + " {num} "  + Fore.RESET + "{type}" + Fore.YELLOW + " link(s) in " + Fore.LIGHTBLUE_EX + "{table}" + Fore.YELLOW +" table:"
ADDED_LINK_NAME = "\t" + Fore.GREEN + "[done]" + Fore.RESET + "\t  {url}"
SKIPPED_LINK_NAME = "\t" + Fore.RED + "[skipped]" + Fore.RESET + " {url}" 