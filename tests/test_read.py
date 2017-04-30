import os
import sys; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import numpy as np
import pytest

from dasprodml import PMLproxy

def test_read_metadata():
    pml_object = PMLproxy(os.path.join(os.path.dirname(__file__), 'data/testcase/case1.epc'))
    assert pml_object.das_acquisition != None
    #assert pml_object.das_instrument_box != None #TODO after lxml fix uncomment
    assert pml_object.fiber_optical_path != None
    dasdata, timestamps = pml_object.read_raw_traces(pml_object.das_acquisition.Raw[0].RawData.RawDataArray.Values.ExternalFileProxy[0],
                                                     pml_object.das_acquisition.Raw[0].RawDataTime.TimeArray.Values.ExternalFileProxy[0],
                                                     0, pml_object.das_acquisition.Raw[0].RawData.RawDataArray.Values.ExternalFileProxy[0].Count)
    np.testing.assert_array_equal(dasdata, np.ones(dasdata.shape, dtype=dasdata.dtype))
    np.testing.assert_array_equal(timestamps, np.ones(timestamps.shape, dtype=dasdata.dtype))
    trigger_time = pml_object.read_raw_trigger_time(pml_object.das_acquisition.Raw[0].RawDataTriggerTime.TimeArray.Values.ExternalFileProxy[0])
    assert trigger_time == 2
