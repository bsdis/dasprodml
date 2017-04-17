import os, sys; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import pytest
from dasprodml import PMLproxy

def test_write_initial():
    a = PMLproxy()
    assert 1 == 1
