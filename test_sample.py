import pytest
from main import print_message

def test_print_message():
    x = print_message("test")
    assert x == "test"