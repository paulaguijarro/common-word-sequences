import pytest
import io
import sys

from utils.texts import clean_text


def test_clean_text():

    params = "IO! PAEAN! IO! SING. Io? Susse and Strasse"
    expected = "io paean io sing io susse and strasse"
    assert clean_text(params) == expected


def test_clean_text_empty():
    params = ""
    expected = ""
    assert clean_text(params) == expected


def test_clean_text_exception():
    params = None
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    with pytest.raises(Exception):
        clean_text(params)
    sys.stdout = sys.__stdout__
    assert "Input is not a string. Exiting." in capturedOutput.getvalue()
