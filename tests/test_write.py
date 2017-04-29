import datetime
import os
import shutil
import sys; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import uuid

import numpy as np
import pytest

import dasprodml.DasAcquisition as da
import dasprodml.FiberOpticalPath as fp

from dasprodml import PMLproxy

def test_write_initial():
    shutil.rmtree('/tmp/prodml-test-case1', ignore_errors=True)
    os.makedirs('/tmp/prodml-test-case1', exist_ok=True)
    prodml_object = PMLproxy('/tmp/prodml-test-case1/case1.epc')
    prodml_object.add_das_acquisition(create_das_acquisition())
    prodml_object.add_das_instrument_box(create_das_instrument_box())
    prodml_object.add_fiber_optical_path(create_fiber_optical_path())
    width = 50
    prodml_object.save()
    for i in range(prodml_object.das_acquisition.Raw[0].RawData.RawDataArray.Values.ExternalFileProxy[0].Count//width):
        dasdata = np.ones((width, prodml_object.das_acquisition.Raw[0].NumberOfLoci), dtype=np.float32)
        timestamps = np.ones((width, ), dtype=np.int64)
        prodml_object.write_raw_traces(prodml_object.das_acquisition.Raw[0].RawData.RawDataArray.Values.ExternalFileProxy[0],
                                       prodml_object.das_acquisition.Raw[0].RawDataTime.TimeArray.Values.ExternalFileProxy[0],
                                       i*width, dasdata, timestamps)
    prodml_object.write_raw_trigger_time(prodml_object.das_acquisition.Raw[0].RawDataTriggerTime.TimeArray.Values.ExternalFileProxy[0], 2)


def create_das_acquisition():
    das = da.DasAcquisition.factory()
    das.set_Aliases([da.ObjectAlias.factory(authority='abc',
                                    Identifier='My alias')])
    das.set_Citation(da.Citation.factory(Title='DAS Acquisition',
                                 Originator='Energistics',
                                 Creation=datetime.datetime.strptime('2015-07-20T01:00:00+0100', '%Y-%m-%dT%H:%M:%S%z'),
                                 Format='Energistics'))
    das.set_CustomData(da.CustomData.factory())
    das.set_ExtensionNameValue([da.ExtensionNameValue.factory(Name='customInt',
                                                      Value=da.StringMeasure.factory(valueOf_=2))])
    das.set_AcquisitionId(str(uuid.uuid4()))
    das.set_AcquisitionDescription('Energistics DAS PRODML Acquisition Sample')
    opticalPath = da.FiberOpticalPath.factory()
    #opticalPath.set_ContentType('Optical Path') # TODO nowhere info about this
    #opticalPath.set_Title('Optical Path')  # TODO nowhere info about this
    #opticalPath.set_Uuid(str(uuid.uuid4())) # TODO nowhere info about this
    das.set_OpticalPath(opticalPath)
    dasInstrumentBox = da.DasInstrumentBox.factory()
    #dasInstrumentBox.set_ContentType('InstrumentBox') # TODO nowhere info about this
    #dasInstrumentBox.set_Title('Instrument Box') # TODO nowhere info about this
    #dasInstrumentBox.set_Uuid(str(uuid.uuid4())) # TODO nowhere info about this
    das.set_DasInstrumentBox(dasInstrumentBox)
    das.set_FacilityId(['ABC Facility',
                        'Well Facility'])
    das.set_VendorCode(da.BusinessAssociate.factory(
        Name="ABCDE",
        Role=[
            da.NameStruct.factory(valueOf_="operator"),
            da.NameStruct.factory(valueOf_="owner"),
        ],
        Alias=[da.NameStruct.factory()],
        Address=da.GeneralAddress.factory(uid='main',
                                  Name='Wyle E Coyote',
                                  Street=['Suite 2100', '515 Congress Avenue'],
                                  City='Austin',
                                  Country='USA',
                                  County='Texas',
                                  PostalCode='78701',
                                  State='Texas',
                                  Province='Texas'),
        PhoneNumber=[da.PhoneNumberStruct.factory(type_='voice')],
        Email=[da.EmailQualifierStruct.factory()],
        AssociatedWith='',
        Contact='',
        PersonName=da.PersonName.factory(Prefix='Wyle',
                                 First='E',
                                 Middle='Coyote',
                                 Last='Esq.',
                                 Suffix=['PhD']) # TODO in reference it is string, in reality it is list
    ))
    das.set_PulseRate(da.FrequencyMeasure.factory(uom='Hz',
                                          valueOf_=50.0))
    das.set_PulseWidth(da.TimeMeasure.factory(uom='ns',
                                      valueOf_=8.0))
    das.set_GaugeLength(da.LengthMeasure.factory(uom='m',
                                         valueOf_=40.0))
    das.set_SpatialSamplingInterval(da.LengthMeasure.factory(uom='m',
                                                     valueOf_=5.0))
    das.set_MinimumFrequency(da.FrequencyMeasure.factory(uom='Hz',
                                                 valueOf_=0.5))
    das.set_MaximumFrequency(da.FrequencyMeasure.factory(uom='Hz',
                                                 valueOf_=25.0))
    das.set_NumberOfLoci(5)
    das.set_StartLocusIndex(0)
    das.set_MeasurementStartTime(datetime.datetime.strptime('2015-07-20T01:23:45.123456+0100', '%Y-%m-%dT%H:%M:%S.%f%z'))
    das.set_TriggeredMeasurement(True)
    rawCustom = da.DasCustom.factory()
    rawCustom.original_tagname_ = 'Custom'
    raw_hdf_uuid = str(uuid.uuid4())
    epcPartReferenceRaw = da.EpcExternalPartReference.factory(_uuid=raw_hdf_uuid, _filename='raw.h5')
    #epcPartReferenceRaw.set_ContentType('InstrumentBox') # TODO nowhere info about this
    #epcPartReferenceRaw.set_Title('Instrument Box') # TODO nowhere info about this
    #epcPartReferenceRaw.set_Uuid(str(uuid.uuid4())) # TODO nowhere info about this
    raw = da.DasRaw.factory(uuid=str(uuid.uuid4()),
                    RawDataUnit='V',
                    OutputDataRate=da.FrequencyMeasure.factory(uom='Hz',
                                                       valueOf_=50.0),
                    StartLocusIndex=0,
                    NumberOfLoci=5,
                    RawData=da.DasRawData.factory(
                        Dimensions=['time', 'locus'],
                        RawDataArray=da.DoubleExternalArray.factory(
                            Values=da.ExternalDataset.factory(
                                ExternalFileProxy=[
                                    da.DasExternalDatasetPart.factory(Count=5000,
                                                              PathInExternalFile='/Acquisition/Raw/RawData',
                                                              StartIndex=0,
                                                              EpcExternalPartReference=epcPartReferenceRaw,
                                                              PartStartTime='2015-07-20T01:23:45.678000+01:00',
                                                              PartEndTime='2015-07-20T01:24:05.658000+01:00')]))),
                    RawDataTime=da.DasTimeArray.factory(
                        StartTime='2015-07-20T01:23:45.678000+01:00',
                        EndTime='2015-07-20T01:24:05.658000+01:00',
                        TimeArray=da.IntegerExternalArray.factory(
                            NullValue=-1,
                            Values=da.ExternalDataset.factory(
                                ExternalFileProxy=[
                                    da.DasExternalDatasetPart.factory(
                                        Count=1000,
                                        PathInExternalFile='/Acquisition/Raw/RawDataTime',
                                        StartIndex=0,
                                        EpcExternalPartReference=epcPartReferenceRaw,
                                        PartStartTime='2015-07-20T01:23:45.678000+01:00',
                                        PartEndTime='2015-07-20T01:24:05.658000+01:00')]))),
                    RawDataTriggerTime=da.DasTimeArray.factory(
                        StartTime='2015-07-20T01:23:45.678000+0100',
                        EndTime='2015-07-20T01:24:05.658000+0100',
                        TimeArray=da.IntegerExternalArray.factory(
                            NullValue=-1,
                            Values=da.ExternalDataset.factory(ExternalFileProxy=[
                                da.DasExternalDatasetPart.factory(
                                    Count=1,
                                    PathInExternalFile='Acquisition/Raw/RawDataTriggerTime',
                                    StartIndex=0,
                                    EpcExternalPartReference=epcPartReferenceRaw,
                                    PartStartTime='2015-07-20T01:23:45.678000+01:00',
                                    PartEndTime='2015-07-20T01:23:45.567000+01:00'
                                )
                            ]
                            )
                        )
                    ),
                    Custom=rawCustom
    )
    das.set_Raw([raw])
    dasCustom = da.DasCustom.factory()
    dasCustom.original_tagname_ = 'Custom'
    das.set_Custom(dasCustom)
    calibrationDataPoint1 =  da.DasCalibrationPoint.factory(
        CalibrationLocusIndex=4,
        CalibrationOpticalPathDistance=da.LengthMeasure.factory(
            uom='m',
            valueOf_=23.500
        ),
        CalibrationFacilityLength=da.LengthMeasure.factory(
            uom='m',
            valueOf_=23.500),
        CalibrationType='tap test'
    )
    calibrationDataPoint2 =  da.DasCalibrationPoint.factory(
        CalibrationLocusIndex=101,
        CalibrationOpticalPathDistance=da.LengthMeasure.factory(
            uom='m',
            valueOf_=-1.000
        ),
        CalibrationFacilityLength=da.LengthMeasure.factory(
            uom='m',
            valueOf_=12.430
        ),
        CalibrationType='last locus to end of fiber'
    )
    calibrationDataPoint3 =  da.DasCalibrationPoint.factory(
        CalibrationLocusIndex=0,
        CalibrationOpticalPathDistance=da.LengthMeasure.factory(
            uom='m',
            valueOf_=5.00
        ),
        CalibrationFacilityLength=da.LengthMeasure.factory(
            uom='m',
            valueOf_=5.00),
        CalibrationType='locus calibration'
    )
    calibrationDataPoint4 =  da.DasCalibrationPoint.factory(
        CalibrationLocusIndex=1,
        CalibrationOpticalPathDistance=da.LengthMeasure.factory(
            uom='m',
            valueOf_=10.00
        ),
        CalibrationFacilityLength=da.LengthMeasure.factory(
            uom='m',
            valueOf_=10.00),
        CalibrationType='locus calibration'
    )
    calibrationDataPoint5 =  da.DasCalibrationPoint.factory(
        CalibrationLocusIndex=4,
        CalibrationOpticalPathDistance=da.LengthMeasure.factory(
            uom='m',
            valueOf_=25.00
        ),
        CalibrationFacilityLength=da.LengthMeasure.factory(
            uom='m',
            valueOf_=25.00),
        CalibrationType='locus calibration'
    )
    calibrationDataPoint6 =  da.DasCalibrationPoint.factory(
        CalibrationLocusIndex=5,
        CalibrationOpticalPathDistance=da.LengthMeasure.factory(
            uom='m',
            valueOf_=30.00
        ),
        CalibrationFacilityLength=da.LengthMeasure.factory(
            uom='m',
            valueOf_=29.907
        ),
        CalibrationType='locus calibration'
    )
    calibrationDataPoint7 =  da.DasCalibrationPoint.factory(
        CalibrationLocusIndex=6,
        CalibrationOpticalPathDistance=da.LengthMeasure.factory(
            uom='m',
            valueOf_=35.00
        ),
        CalibrationFacilityLength=da.LengthMeasure.factory(
            uom='m',
            valueOf_=34.814
        ),
        CalibrationType='locus calibration'
    )
    calibrationDataPoint8 =  da.DasCalibrationPoint.factory(
        CalibrationLocusIndex=99,
        CalibrationOpticalPathDistance=da.LengthMeasure.factory(
            uom='m',
            valueOf_=500.0),
        CalibrationFacilityLength=da.LengthMeasure.factory(
            uom='m',
            valueOf_=491.143
        ),
        CalibrationType='locus calibration'
    )
    calibrationDataPoint9 =  da.DasCalibrationPoint.factory(
        CalibrationLocusIndex=100,
        CalibrationOpticalPathDistance=da.LengthMeasure.factory(
            uom='m',
            valueOf_=505.0
        ),
        CalibrationFacilityLength=da.LengthMeasure.factory(
            uom='m',
            valueOf_=496.050
        ),
        CalibrationType='locus calibration'
    )
    calibrationDataPoint10 =  da.DasCalibrationPoint.factory(
        CalibrationLocusIndex=5,
        CalibrationOpticalPathDistance=da.LengthMeasure.factory(
            uom='m',
            valueOf_=30.0
        ),
        CalibrationFacilityLength=da.LengthMeasure.factory(
            uom='m',
            valueOf_=4.907
        ),
        CalibrationType='locus calibration'
    )
    calibrationDataPoint11 =  da.DasCalibrationPoint.factory(
        CalibrationLocusIndex=6,
        CalibrationOpticalPathDistance=da.LengthMeasure.factory(
            uom='m',
            valueOf_=35.0
        ),
        CalibrationFacilityLength=da.LengthMeasure.factory(
            uom='m',
            valueOf_=9.814),
        CalibrationType='locus calibration'
    )
    calibrationDataPoint12 =  da.DasCalibrationPoint.factory(
        CalibrationLocusIndex=99,
        CalibrationOpticalPathDistance=da.LengthMeasure.factory(
            uom='m',
            valueOf_=500.00
        ),
        CalibrationFacilityLength=da.LengthMeasure.factory(
            uom='m',
            valueOf_=466.143
        ),
        CalibrationType='locus calibration'
    )
    calibrationDataPoint13 =  da.DasCalibrationPoint.factory(
        CalibrationLocusIndex=100,
        CalibrationOpticalPathDistance=da.LengthMeasure.factory(
            uom='m',
            valueOf_=505.00
        ),
        CalibrationFacilityLength=da.LengthMeasure.factory(
            uom='m',
            valueOf_=471.05
        ),
        CalibrationType='locus calibration'
    )
    calibrationDataPoint14 =  da.DasCalibrationPoint.factory(
        CalibrationLocusIndex=100,
        CalibrationOpticalPathDistance=da.LengthMeasure.factory(
            uom='m',
            valueOf_=12.43
        ),
        CalibrationFacilityLength=da.LengthMeasure.factory(
            uom='m',
            valueOf_=-1.0
        ),
        CalibrationType='last locus to end of fiber'
    )
    das.set_Calibration(
        [
            da.DasCalibration.factory(
                NumberOfCalibrationPoints=9,
                FacilityName='Facility name',
                FacilityKind='generic',
                CalibrationDataPoints=[
                    calibrationDataPoint1,
                    calibrationDataPoint2,
                    calibrationDataPoint3,
                    calibrationDataPoint4,
                    calibrationDataPoint5,
                    calibrationDataPoint6,
                    calibrationDataPoint7,
                    calibrationDataPoint8,
                    calibrationDataPoint9
                ]
            ),
            da.DasCalibration.factory(
                NumberOfCalibrationPoints=5,
                FacilityName='Facility name',
                FacilityKind='generic',
                CalibrationDataPoints=[
                    calibrationDataPoint10,
                    calibrationDataPoint11,
                    calibrationDataPoint12,
                    calibrationDataPoint13,
                    calibrationDataPoint14
                ]
            )
        ]
    )
    das.set_Processed(da.DasProcessed())
    return das

def create_das_instrument_box():
    dib = da.DasInstrumentBox(
        SerialNumber='12645A',
        Parameter=[
            da.IndexedObject(
                index=1,
                name='parameter1',
                uom='s',
                description='time'
            )
        ],
        Instrument=da.Instrument(Name='Instrument Box'),
        FirmwareVersion='Firmware version 1'
    )
    dib.set_Citation(
        da.Citation(
            Title='Instrument Box',
            Originator='Fred Mertz, Field Tech',
            Creation=datetime.datetime.strptime('2015-07-20T01:00:00.000000', '%Y-%m-%dT%H:%M:%S.%f'),
            Format='Vendor:ApplicationName')
    )
    return dib

def create_fiber_optical_path():
    fop = fp.FiberOpticalPath(
        Inventory=fp.FiberOpticalPathInventory(
            Connection=[
                fp.FiberConnection(
                    uid='20',
                    Name='Surface Connector',
                    Type='connector',
                    ConnectorType='dry mate'
                )
            ],
            Segment=[
                fp.FiberOpticalPathSegment(
                    uid='10',
                    Name='Surface Fiber',
                    Type='fiber',
                    FiberLength=fp.LengthMeasure(
                        uom='m',
                        valueOf_=25
                    ),
                    OverStuffing=fp.LengthMeasure(
                        uom='m',
                        valueOf_=0
                    ),
                    CableType='single-fiber-cable'
                ),
                fp.FiberOpticalPathSegment(
                    uid='10',
                    Name='Downhole Fiber',
                    Type='fiber',
                    FiberLength=fp.LengthMeasure(
                        uom='m',
                        valueOf_=492.430
                    ),
                    OverStuffing=fp.LengthMeasure(
                        uom='m',
                        valueOf_=9.182
                    ),
                    FiberConveyance=fp.FiberConveyance(
                        Cable=fp.PermanentCable(
                            PermanentCableInstallationType='clamped to tubular',
                            Comment='Over stuffing is equally distributed along the installed downhole cable'
                        )
                    )
                )
            ],
            Terminator=fp.FiberTerminator(
                uid='40',
                Name='Main Terminator',
                TerminationType='termination at cable'
            )
        ),
        OpticalPathNetwork=[
            fp.FiberOpticalPathNetwork(
                uid='OPN1',
                ContextFacility=[
                    fp.FacilityIdentifierStruct(
                        valueOf_='text'
                    )
                ], #TODO problem with between-tag content
                Network=[
                    fp.ProductFlowNetwork(
                        uid='N1',
                        Name='Current Setup Well-01',
                        Unit=[
                            fp.ProductFlowUnit(
                                uid='OPNU10',
                                Facility=fp.FacilityIdentifierStruct(
                                    uidRef=10,
                                    valueOf_='Surface Fiber Segment'
                                ), #TODO problem
                                Port=[
                                    fp.ProductFlowPort(
                                        uid='1',
                                        Direction='inlet',
                                        Name='Connection to LightBox',
                                        ConnectedNode=[
                                            fp.ConnectedNode(
                                                uid='CN',
                                                Node='Instrument Box'
                                            )
                                        ]
                                    ),
                                    fp.ProductFlowPort(
                                        uid='2',
                                        Direction='outlet',
                                        Name='Connection to Surface Connector',
                                        ConnectedNode=[
                                            fp.ConnectedNode(
                                                uid='CSC1',
                                                Node='Surface Connector 1'
                                            )
                                        ]
                                    )
                                ]
                            ),
                            fp.ProductFlowUnit(
                                uid='OPNU20',
                                Facility=fp.FacilityIdentifierStruct(
                                    uidRef=20,
                                    valueOf_='Surface Connector'
                                ), #TODO problem
                                Port=[
                                    fp.ProductFlowPort(
                                        uid='3',
                                        Direction='inlet',
                                        Name='Connection from Surface Connector to Surface Fiber',
                                        ConnectedNode=[
                                            fp.ConnectedNode(
                                                uid='CSC1',
                                                Node='Surface Connector 1'
                                            )
                                        ]
                                    ),
                                    fp.ProductFlowPort(
                                        uid='4',
                                        Direction='outlet',
                                        Name='Connection from Surface Connector to Downhole Fiber',
                                        ConnectedNode=[
                                            fp.ConnectedNode(
                                                uid='CDF1',
                                                Node='Surface Connector 2'
                                            )
                                        ]
                                    )
                                ]
                            ),
                            fp.ProductFlowUnit(
                                uid='OPNU30',
                                Facility=fp.FacilityIdentifierStruct(
                                    uidRef=30,
                                    valueOf_='Downhole Fiber'
                                ), #TODO problem
                                Port=[
                                    fp.ProductFlowPort(
                                        uid='5',
                                        Direction='inlet',
                                        Name='Connection from Surface Connector to Downhole Fiber',
                                        ConnectedNode=[
                                            fp.ConnectedNode(
                                                uid='CDF1',
                                                Node='Surface Connector 2'
                                            )
                                        ]
                                    ),
                                    fp.ProductFlowPort(
                                        uid='6',
                                        Direction='outlet',
                                        Name='Connection from Downhole Fiber to Terminator',
                                        ConnectedNode=[
                                            fp.ConnectedNode(
                                                uid='CT1',
                                                Node='Downhole Connection 1'
                                            )
                                        ]
                                    )
                                ]
                            ),
                            fp.ProductFlowUnit(
                                uid='OPNU40',
                                Facility=fp.FacilityIdentifierStruct(
                                    valueOf_='Terminator'
                                ), #TODO problem
                                Port=[
                                    fp.ProductFlowPort(
                                        uid='7',
                                        Direction='inlet',
                                        Name='Connection from Downhole Fiber to Terminator',
                                        ConnectedNode=[fp.ConnectedNode(
                                            uid='CT1',
                                            Node='Downhole Connection 1'
                                        )
                                        ]
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )
        ],
        FacilityMapping=[
            fp.FiberFacilityMapping(
                uid='FM1',
                TimeStart=datetime.datetime.strptime(
                    '2005-07-20T01:00:00', '%Y-%m-%dT%H:%M:%S'),
                FiberFacilityMappingPart=[
                    fp.FiberFacilityMappingPart(
                        uid='FMP1',
                        OpticalPathDistanceStart=fp.LengthMeasure(
                            uom='m',
                            valueOf_=0.0
                        ),
                        OpticalPathDistanceEnd=fp.LengthMeasure(
                            uom='m',
                            valueOf_=25.0
                        ),
                        FacilityLengthStart=fp.LengthMeasure(
                            uom='m',
                            valueOf_=0.0
                        ),
                        FacilityLengthEnd=fp.LengthMeasure(
                            uom='m',
                            valueOf_=25.0
                        ),
                        Comment="No 'timeEnd' specified since this mapping is still valid. No overstuffing in surface cable",
                        FiberFacility=fp.FiberFacilityGeneric(
                            FacilityName='Surface Cable 1',
                            FacilityKind='Surface Cable'
                        )
                    ),
                    fp.FiberFacilityMappingPart(
                        uid='FMP2',
                        OpticalPathDistanceStart=fp.LengthMeasure(
                            uom='m',
                            valueOf_=25.0
                        ),
                        OpticalPathDistanceEnd=fp.LengthMeasure(
                            uom='m',
                            valueOf_=517.43
                        ),
                        FacilityLengthStart=fp.LengthMeasure(
                            uom='m',
                            valueOf_=0.0
                        ),
                        FacilityLengthEnd=fp.LengthMeasure(
                            uom='m',
                            valueOf_=483.25
                        ),
                        Comment="No 'timeEnd' specified since this mapping is still valid. The over stuffing of 9.182 m equally distributed along the installed downhole cable",
                        FiberFacility=fp.FiberFacilityWell(
                            Name='Well-01 Fiber',
                            WellDatum='kelly bushing',
                            WellboreReference=fp.DataObjectReference(
                                ContentType='wellbore',
                                Title='Main wellbore of well Well-01',
                                Uuid='4ab0fae6-dc0e-405a-b812-203a154c1243'
                            )
                        )
                    )
                ]
            )
        ],
        Defect=[
            fp.FiberPathDefect(
                defectID='OPTDEFECT1',
                OpticalPathDistanceStart=fp.LengthMeasure(
                    uom='ft',
                    valueOf_=352.00
                ),
                DefectType='other',
                TimeStart=datetime.datetime.strptime(
                    '2005-07-20T01:00:00',
                    '%Y-%m-%dT%H:%M:%S'
                ),
                Comment='Consistent signal spike detected at this location'
            )
        ],
        Otdr=[
            fp.FiberOTDR(
                uid='OTDR1',
                Name='Initial OTDR',
                DTimRun=datetime.datetime.strptime('2005-02-14T09:00:00', '%Y-%m-%dT%H:%M:%S'),
                DataInOTDRFile='myOTDR.dat',
                OpticalPathDistanceStart=fp.LengthMeasure(
                    uom='m',
                    valueOf_=0.0
                ),
                OpticalPathDistanceEnd=fp.LengthMeasure(
                    uom='m',
                    valueOf_=517.43
                ),
                Direction='forward',
                Wavelength=fp.LengthMeasure(
                    uom='nm',
                    valueOf_=1550
                )
            )
        ],
        InstallingVendor=fp.BusinessAssociate(
            Name='Vendor Name',
            Contact=['Mr A Vendor']
        ),
        FacilityIdentifier=fp.FacilityIdentifier(
            uid='',
            Name=fp.NameStruct(
                valueOf_='Well-01'
            )
        )
    ) # TODO nothing is shown inside FacilityIdentifier (generateDS? xsd seems fine)

    fop.set_Citation(
        fp.Citation(
            Title='OptPath1',
            Originator='Source',
            Creation=datetime.datetime.strptime('2005-07-20T01:00:00', '%Y-%m-%dT%H:%M:%S'),
            Format='1',
            Description='FiberOpticalPath DAS worked example'
        )
    )
    return fop


if __name__ == '__main__':
    test_write_initial()
