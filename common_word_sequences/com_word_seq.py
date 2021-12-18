import sys
import argparse

from resources.ngram_tool import NgramTool
from utils.styles import Color
from utils.texts import read_files


def main(files: list, top: int, words: int) -> None:

    """
    Run common_word_sequences program
    Args:
        files (list): List of files to read
        top (int): Number of top n-grams to return
        words (int): Number of words to use in n-grams
    """

    if files:
        try:
            text = read_files(files)
        except:
            sys.exit(1)
    else:
        if sys.stdin.isatty():
            print(f"\n{Color.FAIL}No input detected. Exiting.{Color.RESET}")
            sys.exit(1)
        else:
            text = sys.stdin.read()

    my_ngram_tool = NgramTool(top, words)
    try:
        my_ngram_tool.process(text)
    except:
        sys.exit(1)


if __name__ == "__main__":

    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Given text(s) will return a list of the most common word sequences."
    )
    parser.add_argument(
        "-f",
        "--file",
        required=False,
        nargs="*",
        help="Path to file(s) to process. If no file is specified, stdin will be used.",
    )
    parser.add_argument(
        "-t",
        "--top",
        required=False,
        type=int,
        default=100,
        help="Number of top results to return. If no value is specified, 100 will be used.",
    )
    parser.add_argument(
        "-w",
        "--words",
        required=False,
        type=int,
        default=3,
        help="Number of words in each n-gram. If no value is specified, 3 will be used.",
    )
    args = parser.parse_args()

    # Run program
    main(args.file, args.top, args.words)
