import datetime
import os
import uuid
import zipfile

import h5py
import numpy as np

import dasprodml.DasAcquisition as da
import dasprodml.FiberOpticalPath as fp

class PMLproxy(object):

    '''ProdML proxy object

    '''

    def __init__(self, path):
        """Initialize from an .epc file.
        """
        self.epc_path = path
        self.epc_folder = os.path.dirname(path)
        self.acquisition = None
        self.das_instrument_box = None
        self.fiber_optical_path = None
        self.raw_chunk_width = 1024
        # Read metadata if exists.
        if os.path.exists(self.epc_path):
            self.read_metadata(self.epc_path)

    def read_metadata(self):
        """Read metadata.
        """
        with zipfile.ZipFile(self.epc_path) as z:
            for filename in z.namelist():
                if not os.path.isdir(filename):
                    extracted_filename = z.extract(filename)
                    if 'Acquisition' in filename:
                        self.acquisition = da.parse(extracted_filename, silence=True)
                    elif 'DasInstrumentBox' in filename:
                        self.das_instrument_box = da.parse(extracted_filename, silence=True)
                    elif 'FiberOpticalPath' in filename:
                        self.fiber_optical_path = fp.parse(extracted_filename, silence=True)
                    os.remove(extracted_filename)

    def write_metadata(self):
        """Flush metadata into the .epc file.
        """
        # Make filenames.
        acquisition_filename = 'Acquisition_' + self.acquisition.get_AcquisitionId() + '.xml'
        dib_uuid = str(uuid.uuid4())
        das_instrument_box_filename = 'DasInstrumentBox_' + dib_uuid + '.xml'
        fop_uuid = str(uuid.uuid4())
        fiber_optical_path_filename = 'FiberOpticalPath_' + fop_uuid + '.xml'
        hdf_filename = 'Raw.hdf'
        eepr_uuid = str(uuid.uuid4())
        eepr_filename = 'EpcExternalPartReference_'+eepr_uuid+'.xml'
        acquisition_rels_filename = '_rels/' + acquisition_filename + '.rels'
        das_instrument_box_rels_filename = '_rels/' + das_instrument_box_filename + '.rels'
        fiber_optical_path_rels_filename = '_rels/' + fiber_optical_path_filename + '.rels'
        eepr_rels_filename = '_rels/' + eepr_filename + '.rels'
        # Create epc external part reference xml for das hdf files.
        eepr = da.EpcExternalPartReference()
        eepr.set_Citation(da.Citation(Title='Hdf Proxy',
                                      Originator='Energistics',
                                      Creation=datetime.datetime.utcnow(),
                                      Format='Energistics'))
        # Save xml files.
        with zipfile.ZipFile(self.epc_path, 'w') as z:
            ## Save main das xml files.
            with open('acquisition_filename', 'w') as f:
                self.acquisition.export(f, 0,
                                        namespacedef_ = 'xmlns:prodml="http://www.energistics.org/energyml/data/prodmlv2" xmlns:eml="http://www.energistics.org/energyml/data/commonv2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="2" uuid="'+self.acquisition.get_AcquisitionId()+'"')
            z.write('acquisition_filename', acquisition_filename)
            with open('das_instrument_box_filename', 'w') as f:
                f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n')
                self.das_instrument_box.export(f, 0,
                           namespacedef_ = 'xmlns:eml="http://www.energistics.org/energyml/data/commonv2" xmlns:prodml="http://www.energistics.org/energyml/data/prodmlv2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" uuid="'+dib_uuid+'" schemaVersion="2.0" xsi:schemaLocation="http://www.energistics.org/energyml/data/prodmlv2 ../../../../xsd_schemas/DasInstrumentBox.xsd"')
            z.write('das_instrument_box_filename', das_instrument_box_filename)
            with open('fiber_optical_path_filename', 'w') as f:
                self.fiber_optical_path.export(f, 0,
                           namespacedef_ = 'xmlns:eml="http://www.energistics.org/energyml/data/commonv2" xmlns:prodml="http://www.energistics.org/energyml/data/prodmlv2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" uuid="'+fop_uuid+'" schemaVersion="2.0" xsi:schemaLocation="http://www.energistics.org/energyml/data/prodmlv2 ../../../../xsd_schemas/FiberOpticalPath.xsd"')
            z.write('fiber_optical_path_filename', fiber_optical_path_filename)
            ## Save epc external part reference xml for das hdf files.
            with open('eepr_filename', 'w') as f:
                f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n')
                eepr.export(f, 0,
                            namespacedef_ = 'xmlns:eml="http://www.energistics.org/energyml/data/commonv2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="2.0" uuid="'+eepr_uuid+'" xsi:schemaLocation="http://www.energistics.org/energyml/data/commonv2 ../../../common/v2.1/xsd_schemas/EmlAllObjects.xsd" xsi:type="eml:EpcExternalPartReference"')
            z.write('eepr_filename', eepr_filename)
            ## Save contenttypes xml.
            with open('content_types_filename', 'w') as f:
                f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n')
                f.write('<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">')
                f.write('  <Override PartName="/'+acquisition_filename+'" ContentType="application/x-prodml+xml;version=2.0;type=DasAcquisition"/>\n')
                f.write('  <Override PartName="/'+eepr_filename+'" ContentType="application/x-prodml+xml;version=2.0;type=EpcExternalPartReference"/>\n')
                f.write('  <Override PartName="/'+fiber_optical_path_filename+'" ContentType="application/x-prodml+xml;version=2.0;type=FiberOpticalPath"/>\n')
                f.write('  <Override PartName="/'+das_instrument_box_filename+'" ContentType="application/x-prodml+xml;version=2.0;type=DasInstrumentBox"/>\n')
                f.write('  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>\n')
                f.write('  <Override PartName="/docProps/extendedCore.xml" ContentType="application/x-extended-core-properties+xml"/>\n')
                f.write('<Default ContentType="application/vnd.openxmlformats-package.relationships+xml" Extenstion="rels"/>\n</Types>')
            z.write('content_types_filename', '[Content_Types].xml')
            # Save rel xmls.
            with open('acquisition_rels_filename', 'w') as f:
                f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n')
                f.write('<Relationships xmlns:eml="http://www.energistics.org/energyml/data/commonv2" xmlns:prodml="http://www.energistics.org/energyml/data/prodmlv2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.openxmlformats.org/package/2006/relationships">\n')
                f.write('  <Relationship Type="http://schemas.energistics.org/package/2012/relationships/externalPartProxyToMl" Target="'+eepr_filename+'" Id="'+eepr_uuid+'"/>\n')
                f.write('  <Relationship TargetMode="Internal" Type="http://schemas.energistics.org/package/2012/relationships/destinationObject" Target="'+fiber_optical_path_filename+'" Id="'+fop_uuid+'"/>\n')
                f.write('  <Relationship TargetMode="Internal" Type="http://schemas.energistics.org/package/2012/relationships/destinationObject" Target="'+das_instrument_box_filename+'" Id="'+dib_uuid+'"/>\n</Relationships>')
            z.write('acquisition_rels_filename', acquisition_rels_filename)
            with open('das_instrument_box_rels_filename', 'w') as f:
                f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n')
                f.write('<Relationships xmlns:eml="http://www.energistics.org/energyml/data/commonv2" xmlns:prodml="http://www.energistics.org/energyml/data/prodmlv2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.openxmlformats.org/package/2006/relationships">\n')
                f.write('  <Relationship Type="http://schemas.energistics.org/package/2012/relationships/sourceObject" Target="'+acquisition_filename+'" Id="'+self.acquisition.get_AcquisitionId()+'"/>\n</Relationships>')
            z.write('das_instrument_box_rels_filename', das_instrument_box_rels_filename)
            with open('fiber_optical_path_rels_filename', 'w') as f:
                f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n')
                f.write('<Relationships xmlns:eml="http://www.energistics.org/energyml/data/commonv2" xmlns:prodml="http://www.energistics.org/energyml/data/prodmlv2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.openxmlformats.org/package/2006/relationships">\n')
                f.write('  <Relationship Type="http://schemas.energistics.org/package/2012/relationships/sourceObject" Target="'+acquisition_filename+'" Id="'+self.acquisition.get_AcquisitionId()+'"/>\n</Relationships>')
            z.write('fiber_optical_path_rels_filename', fiber_optical_path_rels_filename)
            with open('eepr_rels_filename', 'w') as f:
                f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n')
                f.write('<Relationships xmlns:eml="http://www.energistics.org/energyml/data/commonv2" xmlns:prodml="http://www.energistics.org/energyml/data/prodmlv2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.openxmlformats.org/package/2006/relationships">\n')
                f.write('  <Relationship Type="http://schemas.energistics.org/package/2012/relationships/externalPartProxyToMl" Target="'+acquisition_filename+'" Id="'+self.acquisition.get_AcquisitionId()+'"/>\n')
                f.write('  <Relationship TargetMode="External" Type="http://schemas.energistics.org/package/2012/relationships/externalResource" Target="'+hdf_filename+'" Id="'+eepr_uuid+'"/>\n</Relationships>')
            z.write('eepr_rels_filename', eepr_rels_filename)
            # Save xml files in docProps.
            with open('doc_props_core_filename', 'w') as f:
                f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n')
                f.write('<coreProperties xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://energistics.org/package/2014/metadata/core-properties">\n')
                f.write('  <version>1.0</version>\n  <dcterms:created xsi:type="dcterms:W3CDTF">2017-03-28T16:02:35</dcterms:created>\n</coreProperties>')
            z.write('doc_props_core_filename', 'docProps/core.xml')
            with open('doc_props_extended_core_filename', 'w') as f:
                f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n')
                f.write('<extendedCoreProperties xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://energistics.org/package/2014/metadata/extended-core-properties">\n')
                f.write('  <Energistics-ExtendedCoreProp>TestVersion</Energistics-ExtendedCoreProp>\n</extendedCoreProperties>')
            z.write('doc_props_extended_core_filename', 'docProps/extendedCore.xml')
            with open('doc_props_rels_core_filename', 'w') as f:
                f.write('<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>\n')
                f.write('<Relationships xmlns:eml="http://www.energistics.org/energyml/data/commonv2" xmlns:prodml="http://www.energistics.org/energyml/data/prodmlv2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.openxmlformats.org/package/2006/relationships">\n')
                f.write('  <Relationship Type="http://energistics.org/schemas" Target="docProps/extendedCore.xml" Id="ExtendedCoreProperties"/>\n</Relationships>')
            z.write('doc_props_rels_core_filename', 'docProps/_rels/core.xml.rels')
        # Create das raw hdf file.
        hdf_filepath = os.path.join(self.epc_folder, hdf_filename)
        self.hdf_filepath = hdf_filepath
        hdf_file = h5py.File(hdf_filepath, 'w')
        hdf_file.require_group('Acquisition')
        hdf_file['Acquisition'].attrs['AcquisitionDescription'] = self.acquisition.get_AcquisitionDescription()
        hdf_file['Acquisition'].attrs['AcquisitionId'] = self.acquisition.get_AcquisitionId()
        hdf_file['Acquisition'].attrs['FacilityId'] = [n.encode("ascii", "ignore") for n in self.acquisition.get_FacilityId()]
        hdf_file['Acquisition'].attrs['GaugeLength'] = self.acquisition.get_GaugeLength().get_valueOf_()
        hdf_file['Acquisition'].attrs['MaximumFrequency'] = self.acquisition.get_MaximumFrequency().get_valueOf_()
        hdf_file['Acquisition'].attrs['MeasurementStartTime'] = self.acquisition.get_MeasurementStartTime().isoformat()
        hdf_file['Acquisition'].attrs['MinimumFrequency'] = self.acquisition.get_MinimumFrequency().get_valueOf_()
        hdf_file['Acquisition'].attrs['NumberOfLoci'] = self.acquisition.get_NumberOfLoci()
        hdf_file['Acquisition'].attrs['PulseRate'] = self.acquisition.get_PulseRate().get_valueOf_()
        hdf_file['Acquisition'].attrs['PulseWidth'] = self.acquisition.get_PulseWidth().get_valueOf_()
        hdf_file['Acquisition'].attrs['SpatialSamplingInterval'] = self.acquisition.get_SpatialSamplingInterval().get_valueOf_()
        hdf_file['Acquisition'].attrs['StartLocusIndex'] = self.acquisition.get_StartLocusIndex()
        hdf_file['Acquisition'].attrs['TriggeredMeasurement'] = self.acquisition.get_TriggeredMeasurement()
        hdf_file['Acquisition'].attrs['VendorCode'] = self.acquisition.get_VendorCode().get_Name()
        index = 1
        calibration_dtype = np.dtype([('CalibrationLocusIndex', np.uint64),
                                      ('CalibrationOpticalPathDistance', np.float64),
                                      ('CalibrationFacilityLength', np.float64),
                                      ('CalibrationType', 'S64')])
        for calibration in self.acquisition.get_Calibration():
            group_name = 'Acquisition/Calibration['+str(index)+']'
            hdf_file.require_group(group_name)
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
        hdf_file.require_group('Acquisition/Raw')
        hdf_file['Acquisition/Raw'].attrs['Count'] = self.acquisition.get_Raw()[0].get_RawData().get_RawDataArray().get_Values().get_ExternalFileProxy()[0].get_Count()
        hdf_file['Acquisition/Raw'].attrs['OutputDataRate'] = self.acquisition.get_Raw()[0].get_OutputDataRate().get_valueOf_()
        hdf_file['Acquisition/Raw'].attrs['RawDataUnit'] = self.acquisition.get_Raw()[0].get_RawDataUnit()
        hdf_file['Acquisition/Raw'].attrs['StartLocusIndex'] = self.acquisition.get_Raw()[0].get_StartLocusIndex()
        hdf_file['Acquisition/Raw'].attrs['uuid'] = self.acquisition.get_Raw()[0].get_uuid()
        # RawData dataset.
        dataset_path = self.acquisition.get_Raw()[0].get_RawData().get_RawDataArray().get_Values().get_ExternalFileProxy()[0].get_PathInExternalFile()
        hdf_file.create_dataset(dataset_path,
                                shape=(self.acquisition.get_Raw()[0].get_RawData().get_RawDataArray().get_Values().get_ExternalFileProxy()[0].get_Count(), self.acquisition.get_Raw()[0].get_NumberOfLoci()),
                                chunks=(self.raw_chunk_width, self.acquisition.get_Raw()[0].get_NumberOfLoci()),
                                dtype=np.float32)
        hdf_file[dataset_path].attrs['Count'] = self.acquisition.get_Raw()[0].get_RawData().get_RawDataArray().get_Values().get_ExternalFileProxy()[0].get_Count()
        hdf_file[dataset_path].attrs['Dimensions'] = [n.encode("ascii", "ignore") for n in self.acquisition.get_Raw()[0].get_RawData().get_Dimensions()]
        hdf_file[dataset_path].attrs['PartEndTime'] = self.acquisition.get_Raw()[0].get_RawData().get_RawDataArray().get_Values().get_ExternalFileProxy()[0].get_PartEndTime()
        hdf_file[dataset_path].attrs['PartStartTime'] = self.acquisition.get_Raw()[0].get_RawData().get_RawDataArray().get_Values().get_ExternalFileProxy()[0].get_PartStartTime()
        hdf_file[dataset_path].attrs['StartIndex'] = self.acquisition.get_Raw()[0].get_RawData().get_RawDataArray().get_Values().get_ExternalFileProxy()[0].get_StartIndex()
        # RawDataTime dataset.
        dataset_path = self.acquisition.get_Raw()[0].get_RawDataTime().get_TimeArray().get_Values().get_ExternalFileProxy()[0].get_PathInExternalFile()
        hdf_file.create_dataset(dataset_path,
                                shape=(self.acquisition.get_Raw()[0].get_RawDataTime().get_TimeArray().get_Values().get_ExternalFileProxy()[0].get_Count(),),
                                dtype=np.int64)
        hdf_file[dataset_path].attrs['Count'] = self.acquisition.get_Raw()[0].get_RawDataTime().get_TimeArray().get_Values().get_ExternalFileProxy()[0].get_Count()
        hdf_file[dataset_path].attrs['PartEndTime'] = self.acquisition.get_Raw()[0].get_RawDataTime().get_TimeArray().get_Values().get_ExternalFileProxy()[0].get_PartEndTime()
        hdf_file[dataset_path].attrs['PartStartTime'] = self.acquisition.get_Raw()[0].get_RawDataTime().get_TimeArray().get_Values().get_ExternalFileProxy()[0].get_PartStartTime()
        hdf_file[dataset_path].attrs['StartIndex'] = self.acquisition.get_Raw()[0].get_RawDataTime().get_TimeArray().get_Values().get_ExternalFileProxy()[0].get_StartIndex()
        hdf_file[dataset_path].attrs['EndTime'] = self.acquisition.get_Raw()[0].get_RawDataTime().get_EndTime()
        hdf_file[dataset_path].attrs['StartTime'] = self.acquisition.get_Raw()[0].get_RawDataTime().get_StartTime()
        # RawDataTriggerTime dataset.
        dataset_path = self.acquisition.get_Raw()[0].get_RawDataTriggerTime().get_TimeArray().get_Values().get_ExternalFileProxy()[0].get_PathInExternalFile()
        hdf_file.create_dataset(dataset_path,
                                shape=(self.acquisition.get_Raw()[0].get_RawDataTriggerTime().get_TimeArray().get_Values().get_ExternalFileProxy()[0].get_Count(),),
                                dtype=np.int64)
        hdf_file[dataset_path].attrs['Count'] = self.acquisition.get_Raw()[0].get_RawDataTriggerTime().get_TimeArray().get_Values().get_ExternalFileProxy()[0].get_Count()
        hdf_file[dataset_path].attrs['PartEndTime'] = self.acquisition.get_Raw()[0].get_RawDataTriggerTime().get_TimeArray().get_Values().get_ExternalFileProxy()[0].get_PartEndTime()
        hdf_file[dataset_path].attrs['PartStartTime'] = self.acquisition.get_Raw()[0].get_RawDataTriggerTime().get_TimeArray().get_Values().get_ExternalFileProxy()[0].get_PartStartTime()
        hdf_file[dataset_path].attrs['StartIndex'] = self.acquisition.get_Raw()[0].get_RawDataTriggerTime().get_TimeArray().get_Values().get_ExternalFileProxy()[0].get_StartIndex()
        hdf_file[dataset_path].attrs['EndTime'] = self.acquisition.get_Raw()[0].get_RawDataTriggerTime().get_EndTime()
        hdf_file[dataset_path].attrs['StartTime'] = self.acquisition.get_Raw()[0].get_RawDataTriggerTime().get_StartTime()
        hdf_file.flush()
        hdf_file.close()
        # Cleanup of temporary files.
        os.remove('acquisition_filename')
        os.remove('das_instrument_box_filename')
        os.remove('fiber_optical_path_filename')
        os.remove('eepr_filename')
        os.remove('content_types_filename')
        os.remove('acquisition_rels_filename')
        os.remove('das_instrument_box_rels_filename')
        os.remove('fiber_optical_path_rels_filename')
        os.remove('eepr_rels_filename')
        os.remove('doc_props_core_filename')
        os.remove('doc_props_extended_core_filename')
        os.remove('doc_props_rels_core_filename')

    def write_raw_traces(self, start_index, dasdata, timestamps):
        """Write block of traces of raw data and the corresponding timestamps.
        dasdata should be of shape (traces, loci).
        timestamps sholud be of shape (traces,).
        It is saved at [start_index:start_index+traces, :].
        start_index is 0-based.
        """
        hdf_file = h5py.File(self.hdf_filepath, 'a')
        # Write data.
        dataset_path = self.acquisition.get_Raw()[0].get_RawData().get_RawDataArray().get_Values().get_ExternalFileProxy()[0].get_PathInExternalFile()
        hdf_file[dataset_path][start_index:start_index+array.shape[0], :] = dasdata
        dataset_path = self.acquisition.get_Raw()[0].get_RawDataTime().get_TimeArray().get_Values().get_ExternalFileProxy()[0].get_PathInExternalFile()
        hdf_file[dataset_path][start_index:start_index+array.shape[0]] = timestamps
        hdf_file.flush()
        hdf_file.close()

    def write_raw_trigger_time(self, timestamp):
        """Write trigger time.
        """
        hdf_file = h5py.File(self.hdf_filepath, 'a')
        # Write data.
        dataset_path = self.acquisition.get_Raw()[0].get_RawDataTriggerTime().get_TimeArray().get_Values().get_ExternalFileProxy()[0].get_PathInExternalFile()
        hdf_file[dataset_path][0] = timestamp
        hdf_file.flush()
        hdf_file.close()

    def read_raw_traces(self, start_index, block_size):
        """Read block of traces of raw data and the corresponding timestamps.
        Return value is (dasdata, timestamps).
        """
        hdf_file = h5py.File(self.hdf_filepath, 'a')
        # Write data.
        dataset_path = self.acquisition.get_Raw()[0].get_RawData().get_RawDataArray().get_Values().get_ExternalFileProxy()[0].get_PathInExternalFile()
        dasdata = hdf_file[dataset_path][start_index:start_index+block_size, :]
        dataset_path = self.acquisition.get_Raw()[0].get_RawDataTime().get_TimeArray().get_Values().get_ExternalFileProxy()[0].get_PathInExternalFile()
        timestamps = hdf_file[dataset_path][start_index:start_index+block_size]
        hdf_file.flush()
        hdf_file.close()
        return (dasdata, timestamps)

    def read_raw_trigger_time(self):
        """Read trigger time.
        """
        hdf_file = h5py.File(self.hdf_filepath, 'a')
        # Write data.
        dataset_path = self.acquisition.get_Raw()[0].get_RawDataTriggerTime().get_TimeArray().get_Values().get_ExternalFileProxy()[0].get_PathInExternalFile()
        timestamp = hdf_file[dataset_path][0]
        hdf_file.flush()
        hdf_file.close()
        return timestamp
