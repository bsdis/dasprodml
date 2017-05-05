import datetime
import io
import logging
import os
import tempfile
import uuid

import h5py
import numpy as np
import opc
from opc.constants import CONTENT_TYPE as CT
from opc.constants import RELATIONSHIP_TYPE as RT
from opc.packuri import PackURI

import dasprodml.DasAcquisition as da
import dasprodml.FiberOpticalPath as fp
import dasprodml.DasAcquisitionSub
import dasprodml.FiberOpticalPathSub

#=============== Constants

EPC_EXTENSION = '.epc'
EPC_EXTENSION_WARNING = 'The EPC package shall have the ".epc" file extension!'

class EPC_CT:
    """EPC content types.
    """
    DAS_ACQUISITION = 'application/x-prodml+xml;version=2.0;type=DasAcquisition'
    DAS_INSTRUMENT_BOX = 'application/x-prodml+xml;version=2.0;type=DasInstrumentBox'
    EPC_EXTERNAL_PART_REFERENCE = 'application/x-prodml+xml;version=2.0;type=EpcExternalPartReference'
    FIBER_OPTICAL_PATH = 'application/x-prodml+xml;version=2.0;type=FiberOpticalPath'


class EPC_RT:
    """EPC relationship types.
    """
    DESTINATION_OBJECT = 'http://schemas.energistics.org/package/2012/relationships/destinationObject'
    SOURCE_OBJECT = 'http://schemas.energistics.org/package/2012/relationships/sourceObject'
    ML_TO_EXTERNAL_PART_PROXY = 'http://schemas.energistics.org/package/2012/relationships/mlToExternalPartProxy'
    EXTERNAL_PART_PROXY_TO_ML = 'http://schemas.energistics.org/package/2012/relationships/externalPartProxyToMl'
    EXTERNAL_RESOURCE = 'http://schemas.energistics.org/package/2012/relationships/externalResource'
    DESTINATION_MEDIA = 'http://schemas.energistics.org/package/2012/relationships/destinationMedia'
    SOURCE_MEDIA = 'http://schemas.energistics.org/package/2012/relationships/sourceMedia'
    CHUNKED_PART = 'http://schemas.energistics.org/package/2012/relationships/chunkedPart'

#=============== PMLproxy class

def load_eepr(blob):
    """Loads EpcExternalPartReference from xml.
    """
    blob_input = io.BytesIO(blob)
    eepr = da.parse(blob_input, silence=True)
    blob_input.close()
    return eepr

class PMLproxy(object):

    '''ProdML proxy object

    '''

    def __init__(self, path, raw_chunk_width=1024, raw_data_type=np.float32):
        """Initialize from an .epc file.
        """
        self.epc_path = path
        if not path.endswith(EPC_EXTENSION):
            logging.warning(EPC_EXTENSION_WARNING)
        self.epc_folder = os.path.dirname(path)
        self.package = None
        self.raw_chunk_width = raw_chunk_width
        self.raw_data_type = raw_data_type # TODO find better way to send dtype
        self.external_hdf_files = {}
        self.das_acquisition = None
        self.das_instrument_box = None
        self.fiber_optical_path = None
        self.das_acquisition_part = None
        self.das_instrument_box_part = None
        self.fiber_optical_path_part = None
        self.eeprs = {}
        # Open file if exists, otherwise create a new one.
        if os.path.exists(self.epc_path):
            self.open()
        else:
            self.create()

    def open(self):
        """Open existing file.
        """
        self.package = opc.OpcPackage.open(self.epc_path)
        for part in self.package.parts:
            if part._content_type == CT.OPC_CORE_PROPERTIES:
                self.core_properties = part
            elif part._content_type == EPC_CT.DAS_ACQUISITION:
                tfile = tempfile.NamedTemporaryFile('wb')
                tfile.write(part._blob)
                self.das_acquisition = da.parse(tfile.name, silence=True)
                self.das_acquisition_part = part
                tfile.close()
                for rel in part.rels:
                    if rel._reltype == EPC_RT.ML_TO_EXTERNAL_PART_PROXY:
                        for eepr_rel in rel.target_part.rels:
                            eepr = load_eepr(rel.target_part.blob)
                            if eepr_rel._reltype == EPC_RT.EXTERNAL_RESOURCE:
                                self.external_hdf_files[eepr.uuid] = eepr_rel.target_ref
                                self.eeprs[eepr.uuid] = eepr
            elif part._content_type == EPC_CT.DAS_INSTRUMENT_BOX:
                tfile = tempfile.NamedTemporaryFile('wb')
                tfile.write(part._blob)
                #self.das_instrument_box = da.parse(tfile.name, silence=True) # TODO lxml.etree_.parse() fails on that file, but there is no BOM, need to debug
                #self.das_instrument_box_part = part
                tfile.close()
            elif part._content_type == EPC_CT.FIBER_OPTICAL_PATH:
                tfile = tempfile.NamedTemporaryFile('wb')
                tfile.write(part._blob)
                self.fiber_optical_path = fp.parse(tfile.name, silence=True)
                self.fiber_optical_path_part = part
                tfile.close()

    def create(self, creator='Test', version='1.0'):
        """Create a new file.
        """
        self.package = opc.OpcPackage()
        # Package metadata.
        self.creator = creator
        self.version = version
        # Objects.
        self.das_acquisition = None
        self.das_instrument_box = None
        self.fiber_optical_path = None
        # Create core properties.
        self.core_properties = opc.package.Part(partname=PackURI('/docProps/core.xml'), content_type=CT.OPC_CORE_PROPERTIES, blob=None)
        self.package._add_relationship(reltype=RT.CORE_PROPERTIES, target=self.core_properties, rId='idCoreProperties')

    def save(self):
        """Save the file.
        """
        # Core properties.
        if self.core_properties._blob is None:
            core_properties_xml = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
                                 '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">\n'
                                 '  <dc:creator>' + str(self.creator) + '</dc:creator>\n'
                                 '  <version>'+ str(self.version) + '</version>\n'
                                 '  <dcterms:created xsi:type="dcterms:W3CDTF">' + datetime.datetime.now().isoformat() + '</dcterms:created>\n'
                                 '</cp:coreProperties>')
            self.core_properties._blob = core_properties_xml
        # Das aquisition.
        if self.das_acquisition:
            output = io.StringIO()
            output.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
            self.das_acquisition.export(output, 0,
                                    namespacedef_ = 'xmlns:prodml="http://www.energistics.org/energyml/data/prodmlv2" xmlns:eml="http://www.energistics.org/energyml/data/commonv2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            das_acquisition_xml = output.getvalue()
            print(vars(self.das_acquisition))
            output.close()
            if self.das_acquisition_part:
                self.das_acquisition_part._blob = das_acquisition_xml
            else:
                self.das_acquisition_part = opc.package.Part(partname=PackURI('/DasAcquisition_'+self.das_acquisition.uuid+'.xml'), content_type=EPC_CT.DAS_ACQUISITION, blob=das_acquisition_xml)
            self.package._add_relationship(reltype=EPC_RT.DESTINATION_OBJECT, target=self.das_acquisition_part, rId='idAquisition')
        # Das instrument box.
        if self.das_instrument_box:
            output = io.StringIO()
            output.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
            self.das_instrument_box.export(output, 0,
                                    namespacedef_ = 'xmlns:eml="http://www.energistics.org/energyml/data/commonv2" xmlns:prodml="http://www.energistics.org/energyml/data/prodmlv2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.energistics.org/energyml/data/prodmlv2 ../../../../xsd_schemas/DasInstrumentBox.xsd"')
            das_instrument_box_xml = output.getvalue()
            output.close()
            if self.das_instrument_box_part:
                self.das_instrument_box_part._blob = das_instrument_box_xml
            else:
                self.das_instrument_box_part = opc.package.Part(partname=PackURI('/DasInstrumentBox_'+self.das_instrument_box.uuid+'.xml'), content_type=EPC_CT.DAS_INSTRUMENT_BOX, blob=das_instrument_box_xml)
            if self.das_acquisition:
                self.das_acquisition_part._add_relationship(reltype=EPC_RT.DESTINATION_OBJECT, target=self.das_instrument_box_part, rId='_'+self.das_instrument_box.uuid)
                self.das_instrument_box_part._add_relationship(reltype=EPC_RT.SOURCE_OBJECT, target=self.das_acquisition_part, rId='_'+self.das_acquisition.uuid)
            else:
                self.package._add_relationship(reltype=EPC_RT.DESTINATION_OBJECT, target=das_instrument_box_part, rId='idDasInstrumentBox')
        # Fiber optical path.
        if self.fiber_optical_path:
            output = io.StringIO()
            output.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
            self.fiber_optical_path.export(output, 0,
                                    namespacedef_ = 'xmlns:eml="http://www.energistics.org/energyml/data/commonv2" xmlns:prodml="http://www.energistics.org/energyml/data/prodmlv2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.energistics.org/energyml/data/prodmlv2 ../../../../xsd_schemas/FiberOpticalPath.xsd"')

            fiber_optical_path_xml = output.getvalue()
            output.close()
            if self.fiber_optical_path_part:
                self.fiber_optical_path_part._blob = fiber_optical_path_xml
            else:
                self.fiber_optical_path_part = opc.package.Part(partname=PackURI('/FiberOpticalPath_'+self.fiber_optical_path.uuid+'.xml'), content_type=EPC_CT.FIBER_OPTICAL_PATH, blob=fiber_optical_path_xml)
            if self.das_acquisition:
                self.das_acquisition_part._add_relationship(reltype=EPC_RT.DESTINATION_OBJECT, target=self.fiber_optical_path_part, rId='_'+self.fiber_optical_path.uuid)
                self.fiber_optical_path_part._add_relationship(reltype=EPC_RT.SOURCE_OBJECT, target=self.das_acquisition_part, rId='_'+self.das_acquisition.uuid)
            else:
                self.package._add_relationship(reltype=EPC_RT.DESTINATION_OBJECT, target=fiber_optical_path_part, rId='idFiberOpticalPath')
        # External files.
        self.external_hdf_files = {}
        for Raw in self.das_acquisition.Raw:
            if (Raw.RawData is not None and
                Raw.RawData.RawDataArray is not None and
                Raw.RawData.RawDataArray.Values is not None):
                for DasExternalDatasetPart in Raw.RawData.RawDataArray.Values.ExternalFileProxy:
                    eepr = DasExternalDatasetPart.EpcExternalPartReference
                    self.external_hdf_files[eepr.Uuid] = str(eepr.Uuid) + '.h5'
                    self.write_hdf_metadata(eepr.Uuid, Raw)
                    self.write_hdf_data_array_metadata(self.external_hdf_files[eepr.Uuid], Raw, DasExternalDatasetPart)
            if (Raw.RawDataTime is not None and
                Raw.RawDataTime.TimeArray is not None and
                Raw.RawDataTime.TimeArray.Values is not None):
                for DasExternalDatasetPart in Raw.RawDataTime.TimeArray.Values.ExternalFileProxy:
                    eepr = DasExternalDatasetPart.EpcExternalPartReference
                    self.external_hdf_files[eepr.Uuid] = str(eepr.Uuid) + '.h5'
                    self.write_hdf_metadata(eepr.Uuid, Raw)
                    self.write_hdf_time_data_array_metadata(self.external_hdf_files[eepr.Uuid], Raw.RawDataTime, DasExternalDatasetPart)
            if (Raw.RawDataTriggerTime is not None and
                Raw.RawDataTriggerTime.TimeArray is not None and
                Raw.RawDataTriggerTime.TimeArray.Values is not None):
                for DasExternalDatasetPart in Raw.RawDataTriggerTime.TimeArray.Values.ExternalFileProxy:
                    eepr = DasExternalDatasetPart.EpcExternalPartReference
                    self.external_hdf_files[eepr.Uuid] = str(eepr.Uuid) + '.h5'
                    self.write_hdf_metadata(eepr.Uuid, Raw)
                    self.write_hdf_time_data_array_metadata(self.external_hdf_files[eepr.Uuid], Raw.RawDataTriggerTime, DasExternalDatasetPart)
        for eepr_uuid in self.external_hdf_files:
            if eepr_uuid in self.eeprs:
                continue
            eepr = da.EpcExternalPartReference.factory()
            eepr.schemaVersion = '2'
            eepr.uuid = eepr_uuid
            eepr.set_Citation(da.Citation.factory(Title='Hdf Proxy',
                                          Originator='Energistics',
                                          Creation=datetime.datetime.utcnow(),
                                          Format='Energistics'))
            output = io.StringIO()
            output.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
            eepr.export(output, 0,
                                    namespacedef_ = 'xmlns:eml="http://www.energistics.org/energyml/data/commonv2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.energistics.org/energyml/data/commonv2 ../../../common/v2.1/xsd_schemas/EmlAllObjects.xsd" xsi:type="eml:EpcExternalPartReference"')

            eepr_xml = output.getvalue()
            output.close()
            eepr_part = opc.package.Part(partname=PackURI('/EpcExternalPartReference_'+eepr_uuid+'.xml'), content_type=EPC_CT.EPC_EXTERNAL_PART_REFERENCE, blob=eepr_xml)
            self.das_acquisition_part._add_relationship(reltype=EPC_RT.ML_TO_EXTERNAL_PART_PROXY, target=eepr_part, rId='_'+eepr_uuid)
            eepr_part._add_relationship(reltype=EPC_RT.EXTERNAL_PART_PROXY_TO_ML, target=self.das_acquisition_part, rId='_'+self.das_acquisition.uuid)
            eepr_part._add_relationship(reltype=EPC_RT.EXTERNAL_RESOURCE, target=self.external_hdf_files[eepr_uuid], rId='Hdf5File', external=True)
            self.eeprs[eepr_uuid] = eepr

        # Save the package.
        self.package.save(self.epc_path)

    def add_das_acquisition(self, das_acquisition):
        """Add DAS acquisition object to the package.
        """
        self.das_acquisition = das_acquisition

    def add_das_instrument_box(self, das_instrument_box):
        """Add DAS instrument box to the package.
        """
        self.das_instrument_box = das_instrument_box

    def add_fiber_optical_path(self, fiber_optical_path):
        """Add fiber optical path to the package.
        """
        self.fiber_optical_path = fiber_optical_path

    def write_hdf_metadata(self, uuid, Raw):
        """Write hdf metadata.
        """
        filename = self.external_hdf_files[uuid]
        # Create das raw hdf file.
        hdf_file = h5py.File(os.path.join(self.epc_folder, filename), 'a')
        hdf_file.attrs['uuid'] = uuid
        if 'Acquisition' not in hdf_file:
            hdf_file.create_group('Acquisition')
            hdf_file['Acquisition'].attrs['AcquisitionDescription'] = self.das_acquisition.get_AcquisitionDescription()
            hdf_file['Acquisition'].attrs['AcquisitionId'] = self.das_acquisition.get_AcquisitionId()
            hdf_file['Acquisition'].attrs['FacilityId'] = [n.encode("ascii", "ignore") for n in self.das_acquisition.get_FacilityId()]
            if self.das_acquisition.get_GaugeLength():
                hdf_file['Acquisition'].attrs['GaugeLength'] = self.das_acquisition.get_GaugeLength().get_valueOf_()
            if self.das_acquisition.get_MaximumFrequency():
                hdf_file['Acquisition'].attrs['MaximumFrequency'] = self.das_acquisition.get_MaximumFrequency().get_valueOf_()
            if self.das_acquisition.get_MeasurementStartTime():
                hdf_file['Acquisition'].attrs['MeasurementStartTime'] = self.das_acquisition.get_MeasurementStartTime().isoformat()
            if self.das_acquisition.get_MinimumFrequency():
                hdf_file['Acquisition'].attrs['MinimumFrequency'] = self.das_acquisition.get_MinimumFrequency().get_valueOf_()
            hdf_file['Acquisition'].attrs['NumberOfLoci'] = self.das_acquisition.get_NumberOfLoci()
            hdf_file['Acquisition'].attrs['PulseRate'] = self.das_acquisition.get_PulseRate().get_valueOf_()
            if self.das_acquisition.get_PulseWidth():
                hdf_file['Acquisition'].attrs['PulseWidth'] = self.das_acquisition.get_PulseWidth().get_valueOf_()
            if self.das_acquisition.get_SpatialSamplingInterval():
                hdf_file['Acquisition'].attrs['SpatialSamplingInterval'] = self.das_acquisition.get_SpatialSamplingInterval().get_valueOf_()
            if self.das_acquisition.get_StartLocusIndex():
                hdf_file['Acquisition'].attrs['StartLocusIndex'] = self.das_acquisition.get_StartLocusIndex()
            if self.das_acquisition.get_TriggeredMeasurement():
                hdf_file['Acquisition'].attrs['TriggeredMeasurement'] = self.das_acquisition.get_TriggeredMeasurement()
            if self.das_acquisition.get_VendorCode():
                hdf_file['Acquisition'].attrs['VendorCode'] = self.das_acquisition.get_VendorCode().get_Name()
        index = 1
        calibration_dtype = np.dtype([('CalibrationLocusIndex', np.uint64),
                                      ('CalibrationOpticalPathDistance', np.float64),
                                      ('CalibrationFacilityLength', np.float64),
                                      ('CalibrationType', 'S64')])
        for calibration in self.das_acquisition.get_Calibration():
            group_name = 'Acquisition/Calibration['+str(index)+']'
            if group_name not in hdf_file:
                hdf_file.create_group(group_name)
                hdf_file[group_name].attrs['FacilityKind'] = calibration.get_FacilityKind()
                hdf_file[group_name].attrs['FacilityName'] = calibration.get_FacilityName()
                hdf_file[group_name].attrs['NumberOfCalibrationPoints'] = calibration.get_NumberOfCalibrationPoints()
                dset_name = group_name+'/CalibrationDataPoints'
                hdf_file.create_dataset(dset_name,
                                        shape=(calibration.get_NumberOfCalibrationPoints(),),
                                        dtype=calibration_dtype)
                for j, cdp in enumerate(calibration.get_CalibrationDataPoints()):
                    hdf_file[dset_name][j, 'CalibrationLocusIndex'] = cdp.get_CalibrationLocusIndex()
                    hdf_file[dset_name][j, 'CalibrationOpticalPathDistance'] = cdp.get_CalibrationOpticalPathDistance().get_valueOf_()
                    hdf_file[dset_name][j, 'CalibrationFacilityLength'] = cdp.get_CalibrationFacilityLength().get_valueOf_()
                    hdf_file[dset_name][j, 'CalibrationType'] = cdp.get_CalibrationType()
            index += 1
        hdf_file.require_group('Acquisition/Custom')
        if 'Acquisition/Raw' not in hdf_file:
            hdf_file.create_group('Acquisition/Raw')
            if Raw.get_OutputDataRate():
                hdf_file['Acquisition/Raw'].attrs['OutputDataRate'] = Raw.get_OutputDataRate().get_valueOf_()
            if Raw.get_RawDataUnit():
                hdf_file['Acquisition/Raw'].attrs['RawDataUnit'] = Raw.get_RawDataUnit()
            if Raw.get_StartLocusIndex():
                hdf_file['Acquisition/Raw'].attrs['StartLocusIndex'] = Raw.get_StartLocusIndex()
            hdf_file['Acquisition/Raw'].attrs['uuid'] = Raw.get_uuid()
        hdf_file.flush()
        hdf_file.close()

    def write_hdf_data_array_metadata(self, filename, Raw, dataset):
        """Write hdf metadata.
        """
        # RawData dataset.
        hdf_file = h5py.File(os.path.join(self.epc_folder, filename), 'a')
        dataset_path = dataset.get_PathInExternalFile()
        if dataset_path not in hdf_file:
            hdf_file.create_dataset(dataset_path,
                                    shape=(dataset.get_Count(), Raw.get_NumberOfLoci()),
                                    chunks=(self.raw_chunk_width, Raw.get_NumberOfLoci()),
                                    dtype=self.raw_data_type)
        hdf_file[dataset_path].attrs['Count'] = dataset.get_Count()
        hdf_file[dataset_path].attrs['Dimensions'] = [n.encode("ascii", "ignore") for n in Raw.get_RawData().get_Dimensions()]
        hdf_file[dataset_path].attrs['PartEndTime'] = dataset.get_PartEndTime()
        hdf_file[dataset_path].attrs['PartStartTime'] = dataset.get_PartStartTime()
        hdf_file[dataset_path].attrs['StartIndex'] = dataset.get_StartIndex()
        hdf_file.flush()
        hdf_file.close()

    def write_hdf_time_data_array_metadata(self, filename, raw_data_time, dataset):
        """Write hdf metadata.
        """
        hdf_file = h5py.File(os.path.join(self.epc_folder, filename), 'a')
        dataset_path = dataset.get_PathInExternalFile()
        if dataset_path not in hdf_file:
            hdf_file.create_dataset(dataset_path,
                                    shape=(dataset.get_Count(),),
                                    dtype=np.int64)
        hdf_file[dataset_path].attrs['Count'] = dataset.get_Count()
        hdf_file[dataset_path].attrs['PartEndTime'] = dataset.get_PartEndTime()
        hdf_file[dataset_path].attrs['PartStartTime'] = dataset.get_PartStartTime()
        hdf_file[dataset_path].attrs['StartIndex'] = dataset.get_StartIndex()
        hdf_file[dataset_path].attrs['EndTime'] = raw_data_time.get_EndTime()
        hdf_file[dataset_path].attrs['StartTime'] = raw_data_time.get_StartTime()
        hdf_file.flush()
        hdf_file.close()

    def write_raw_traces(self, dasdata_external_file_proxy, timestamps_external_file_proxy, start_index, dasdata, timestamps):
        """Write block of traces of raw data and the corresponding timestamps.
        dasdata should be of shape (traces, loci).
        timestamps sholud be of shape (traces,).
        It is saved at [start_index:start_index+traces, :].
        start_index is 0-based.
        """
        # Dasdata.
        filename = self.external_hdf_files[dasdata_external_file_proxy.EpcExternalPartReference.Uuid]
        hdf_file = h5py.File(os.path.join(self.epc_folder, filename), 'a')
        dataset_path = dasdata_external_file_proxy.get_PathInExternalFile()
        hdf_file[dataset_path][start_index:start_index+dasdata.shape[0], :] = dasdata
        # Timestamps.
        filename = self.external_hdf_files[timestamps_external_file_proxy.EpcExternalPartReference.Uuid]
        hdf_file = h5py.File(os.path.join(self.epc_folder, filename), 'a')
        dataset_path = timestamps_external_file_proxy.get_PathInExternalFile()
        hdf_file[dataset_path][start_index:start_index+timestamps.shape[0]] = timestamps
        hdf_file.flush()
        hdf_file.close()

    def write_raw_trigger_time(self, external_file_proxy, timestamp):
        """Write trigger time.
        """
        filename = self.external_hdf_files[external_file_proxy.EpcExternalPartReference.Uuid]
        hdf_file = h5py.File(os.path.join(self.epc_folder, filename), 'a')
        # Write data.
        dataset_path = external_file_proxy.get_PathInExternalFile()
        hdf_file[dataset_path][0] = timestamp
        hdf_file.flush()
        hdf_file.close()

    def read_raw_traces(self, dasdata_external_file_proxy, timestamps_external_file_proxy, start_index, block_size):
        """Read block of traces of raw data and the corresponding timestamps.
        Return value is (dasdata, timestamps).
        """
        hdf_file = h5py.File(os.path.join(self.epc_folder, self.external_hdf_files[dasdata_external_file_proxy.EpcExternalPartReference.Uuid]), 'a')
        dataset_path = dasdata_external_file_proxy.get_PathInExternalFile()
        dasdata = hdf_file[dataset_path][start_index:start_index+block_size, :]
        hdf_file.close()
        hdf_file = h5py.File(os.path.join(self.epc_folder, self.external_hdf_files[timestamps_external_file_proxy.EpcExternalPartReference.Uuid]), 'a')
        dataset_path = timestamps_external_file_proxy.get_PathInExternalFile()
        timestamps = hdf_file[dataset_path][start_index:start_index+block_size]
        hdf_file.close()
        return (dasdata, timestamps)

    def read_raw_trigger_time(self, external_file_proxy):
        """Read trigger time.
        """
        hdf_file = h5py.File(os.path.join(self.epc_folder, self.external_hdf_files[external_file_proxy.EpcExternalPartReference.Uuid]), 'a')
        dataset_path = external_file_proxy.get_PathInExternalFile()
        timestamp = hdf_file[dataset_path][0]
        hdf_file.close()
        return timestamp
