import pytest
from io import StringIO
import sys

def test_range_not_exceeding_ten():
    """Check if the range does not exceed 10"""
    capturedOutput = StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                    # Redirect stdout

    for i in range(10):
        output = "This is the {} time line 2 is running".format(i)

    sys.stdout = sys.__stdout__                 # Reset redirected stdout

    assert capturedOutput.getvalue().count("time") == 10


def test_range_not_exceeding_ten_invalid():
    """Check if the range does not exceed 10. This should fail because it prints a
    message that is more than one line."""

    capturedOutput = StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                    # Redirect stdout

    for i in range(15):
        output = "This is the {} time line 2 is running".format(i)

    sys.stdout = sys.__stdout__                 # Reset redirected stdout



def test_range_exceeding_ten():
    """check if it runs a range bigger than 10 without error"""

    for i in range(20):
        output = "This is the {} time line 2 is running".format(i)


def test_empty_range():
    """Check that code still runs when empty range specified."""
    capturedOutput = StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput                    # Redirect stdout

    for i in range(0):
        output = "This is the {} time line 2 is running".format(i)

    sys.stdout = sys.__stdout__                 # Reset redirected stdout

    assert capturedOutput.getvalue()

def test_negative_range():
    """Check that code still runs when negative range specified."""


    for i in range(-1, 0):
        assert "This is the {}".format(i) ==\
           'This is the -1 time line 2 '

import os

@pytest.fixture
def file_path():
    return "testings/mainTest.py"


def test_open_file(file_path):
    with open(file_path,'a', encoding='utf-8') as f:
        assert 'w' in dir(f)


from main import *