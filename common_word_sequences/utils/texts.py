import re

from string import punctuation
from utils.styles import Color


def clean_text(text: str) -> str:

    """
    Given a string as input, clean the input removing punctuation and transform to case insensitive.
    Args:
        text (str): String to clean
    Returns:
        normalized_text (str): Cleaned string
    """

    custom_punctuation = punctuation.replace("'", "")  # remove apostrophes
    try:
        text_lower = text.lower()  # make text lowercase
    except:
        print(f"{Color.FAIL}Input is not a string. Exiting.{Color.RESET}")
        raise
    normalized_text = re.sub(
        r"[{}]".format(custom_punctuation), "", text_lower
    )  # remove punctuation
    return normalized_text


def read_files(files: list) -> str:
    """
    Given a list of files, read each file and return a string of all the files
    Args:
        files (list): List of files to read
    Raises:
        FileNotFoundError: If file is not found
        OSError: If file is not readable
    Returns:
        str: Combined string from readed files
    """

    text = ""
    for file in files:
        try:
            with open(file, encoding="utf8") as input:
                text += input.read()
        except FileNotFoundError:
            print(f"{Color.FAIL}File {file} not found.\nExiting.{Color.RESET}")
            raise
        except OSError as err:
            print(f"{Color.FAIL}{err}.\nExiting{Color.RESET}")
            raise
    return text
