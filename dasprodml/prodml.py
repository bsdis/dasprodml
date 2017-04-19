import os
import zipfile

import dasprodml.DasAcquisition as da
import dasprodml.FiberOpticalPath as fp

class PMLproxy(object):

    '''ProdML proxy object

    '''

    def __init__(self, path):
        """Initialize from an .epc file.
        """
        self.epc_path = path
        self.acquisition = None

    def read_metadata(self):
        """Read metadata.
        """
        with zipfile.ZipFile(self.epc_path) as z:
            for filename in z.namelist():
                if not os.path.isdir(filename):
                    extracted_filename = z.extract(filename)
                    if 'Acquisition' in filename:
                        self.read_acquisition(extracted_filename)
                    elif 'DasInstrumentBox' in filename:
                        self.read_das_instrument_box(extracted_filename)
                    elif 'FiberOpticalPath' in filename:
                        self.read_fiber_optical_path(extracted_filename)
                    os.remove(extracted_filename)

    def read_acquisition(self, filename):
        """Read acquisition xml.
        """
        self.acquisition = da.parse(filename, silence=True)

    def read_das_instrument_box(self, filename):
        """Read acquisition xml.
        """
        self.das_instrument_box = da.parse(filename, silence=True)

    def read_fiber_optical_path(self, filename):
        """Read acquisition xml.
        """
        self.fiber_optical_path = fp.parse(filename, silence=True)
