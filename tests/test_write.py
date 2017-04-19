import os
import sys; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pytest

from dasprodml import PMLproxy

def test_write_initial():
    a = PMLproxy(os.path.join(os.path.dirname(__file__), 'data/Case1/Case1.epc'))
    assert 1 == 1 # TODO
