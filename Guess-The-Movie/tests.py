from __future__ import annotations
import pytest
from guessthemovie import SetUp

# testing get_movie() method of SetUp class
def test_get_movie():
    """tests the return type of get_movie() mehtod"""
    setup = SetUp()
    return_value = setup.get_movie() 
    assert isinstance(return_value, tuple)
    assert isinstance(return_value[0], str)
    assert isinstance(return_value[1], str)