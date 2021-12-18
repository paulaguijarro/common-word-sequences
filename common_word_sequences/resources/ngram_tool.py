from prettytable import PrettyTable
from collections import Counter
from nltk.util import ngrams

from utils.texts import clean_text
from utils.styles import Color


class NgramTool:
    def __init__(self, top: int, words: int):
        self.top = top
        self.words = words

    def _top_word_sequences(self, input_list: list) -> list:

        """
        Given a list of words, returns a list of n most common n-grams
        and their counts from the most common to the least.
        Args:
            input_list (list): List of words to process
        Returns:
            list: List of n-grams and their counts
        """

        try:
            # all_ngrams = zip(*[input_list[i:] for i in range(self.words)])
            all_ngrams = ngrams(
                input_list, self.words
            )  # using ngrams from nltk to improve performance
            top_ngrams = Counter(all_ngrams).most_common(self.top)
        except:
            print(
                f"{Color.FAIL}Error while creating list of n most common n-grams. Exiting.{Color.RESET}"
            )
            raise
        return top_ngrams

    def _pretty_results(self, top_ngrams: list) -> None:

        """
        Given a list of ngrams and their counts, print them in a pretty table.
        Args:
            top_ngrams (list): List of ngrams and their counts
        """

        if top_ngrams:
            t = PrettyTable(["Word Sequence", "Count"])
            t.title = f"Top {self.top} most common {self.words}-word sequences"
            t.align["Word Sequence"] = "l"
            for ngram, count in top_ngrams:
                t.add_row([" ".join(ngram), count])
            print(f"\n{Color.OKGREEN}{t}{Color.RESET}")

        else:
            print(f"\n{Color.FAIL}No results found{Color.RESET}")

    def process(self, text: str) -> None:
        print(f"\n{Color.INFO}Processing text...{Color.RESET}")
        text = clean_text(text)
        text = [word.strip("'") for word in text.split()] # split text and remove leading/trailing single quotes
        top_ngrams = self._top_word_sequences(text)
        text = None  # free up memory
        self._pretty_results(top_ngrams)
