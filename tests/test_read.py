import os
import sys; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pytest

from dasprodml import PMLproxy

def test_read_metadata():
    pass
    a = PMLproxy(os.path.join(os.path.dirname(__file__), 'data/Case1/Case1.epc'))
    assert a.acquisition != None
    assert a.das_instrument_box != None
    assert a.fiber_optical_path != None
