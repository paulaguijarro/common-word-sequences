import pytest
import io
import sys

from resources.ngram_tool import NgramTool


def test_top_word_sequences_5():
    input_list = ["io", "paean", "io", "sing", "io", "susse", "and", "strasse"]
    expected = [
        (("io", "paean", "io"), 1),
        (("paean", "io", "sing"), 1),
        (("io", "sing", "io"), 1),
        (("sing", "io", "susse"), 1),
        (("io", "susse", "and"), 1),
    ]
    assert NgramTool(top=5, words=3)._top_word_sequences(input_list) == expected


def test_top_word_sequences_3():
    input_list = ["io", "paean", "io", "paean", "io", "susse", "and", "strasse"]
    expected = [
        (("io", "paean"), 2),
        (("paean", "io"), 2),
        (("io", "susse"), 1),
    ]
    assert NgramTool(top=3, words=2)._top_word_sequences(input_list) == expected


def test_top_word_sequences_exception():
    input_list = 1
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    with pytest.raises(Exception):
        NgramTool(top=3, words=2)._top_word_sequences(input_list)
    sys.stdout = sys.__stdout__
    assert (
        "Error while creating list of n most common n-grams. Exiting."
        in capturedOutput.getvalue()
    )


def test_pretty_results_no_results():
    params = []
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    NgramTool(top=3, words=2)._pretty_results(params)
    sys.stdout = sys.__stdout__
    assert "No results found" in capturedOutput.getvalue()


def test_pretty_results_results():
    params = [
        (("io", "paean"), 2),
        (("paean", "io"), 2),
        (("io", "susse"), 1),
    ]
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    NgramTool(top=3, words=2)._pretty_results(params)
    sys.stdout = sys.__stdout__
    assert "Top 3 most common 2-word sequences" in capturedOutput.getvalue()
