#!/usr/bin/env python

#
# Generated Wed Apr 26 16:56:55 2017 by generateDS.py version 2.25a.
#
# Command line options:
#   ('-o', 'dasprodml/DasAcquisition.py')
#   ('-s', 'dasprodml/DasAcquisitionSub.py')
#   ('--super', 'DasAcquisition')
#   ('-m', '')
#
# Command line arguments:
#   ./energistics/prodml/v2.0/xsd_schemas/DasAcquisition.xsd
#
# Command line:
#   generateDS.py -o "dasprodml/DasAcquisition.py" -s "dasprodml/DasAcquisitionSub.py" --super="DasAcquisition" -m ./energistics/prodml/v2.0/xsd_schemas/DasAcquisition.xsd
#
# Current working directory (os.getcwd()):
#   dasprodml
#

### The EmlMixin class

class EmlMixin(object):
    """Changes xml namespace to 'eml:'.
    """
    def export(self, *args, **kwargs):
        if 'prodml:' in args:
            args = list(args)
            args[args.index('prodml:')] = 'eml:'
        elif not 'eml:' in args:
            kwargs['namespace_'] = 'eml:'
        super().export(*args, **kwargs)

    def exportChildren(self, *args, **kwargs):
        if 'prodml:' in args:
            args = list(args)
            args[args.index('prodml:')] = 'eml:'
        elif not 'eml:' in args:
            kwargs['namespace_'] = 'eml:'
        super().exportChildren(*args, **kwargs)

###

import sys
from lxml import etree as etree_

import dasprodml.DasAcquisition as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'utf-8'

#
# Data representation classes
#


class DasCalibrationSub(supermod.DasCalibration):
    def __init__(self, CalibrationIndex=None, NumberOfCalibrationPoints=None, CalibrationDescription=None, CalibrationOpticalPathDistanceUnit=None, CalibrationFacilityLengthUnit=None, CalibrationDatum=None, FacilityName=None, FacilityKind=None, CalibrationDataPoints=None):
        super(DasCalibrationSub, self).__init__(CalibrationIndex, NumberOfCalibrationPoints, CalibrationDescription, CalibrationOpticalPathDistanceUnit, CalibrationFacilityLengthUnit, CalibrationDatum, FacilityName, FacilityKind, CalibrationDataPoints, )
supermod.DasCalibration.subclass = DasCalibrationSub
# end class DasCalibrationSub


class DasCalibrationPointSub(supermod.DasCalibrationPoint):
    def __init__(self, CalibrationLocusIndex=None, CalibrationOpticalPathDistance=None, CalibrationFacilityLength=None, CalibrationType=None):
        super(DasCalibrationPointSub, self).__init__(CalibrationLocusIndex, CalibrationOpticalPathDistance, CalibrationFacilityLength, CalibrationType, )
supermod.DasCalibrationPoint.subclass = DasCalibrationPointSub
# end class DasCalibrationPointSub


class DasCustomSub(supermod.DasCustom):
    def __init__(self):
        super(DasCustomSub, self).__init__()
supermod.DasCustom.subclass = DasCustomSub
# end class DasCustomSub


class DasFbeSub(supermod.DasFbe):
    def __init__(self, uuid=None, FbeIndex=None, FbeDescription=None, FbeDataUnit=None, OutputDataRate=None, StartLocusIndex=None, NumberOfLoci=None, SpatialSamplingInterval=None, SpatialSamplingIntervalUnit=None, FilterType=None, WindowSize=None, WindowOverlap=None, WindowFunction=None, TransformType=None, TransformSize=None, RawReference=None, SpectraReference=None, FbeData=None, FbeDataTime=None, Custom=None):
        super(DasFbeSub, self).__init__(uuid, FbeIndex, FbeDescription, FbeDataUnit, OutputDataRate, StartLocusIndex, NumberOfLoci, SpatialSamplingInterval, SpatialSamplingIntervalUnit, FilterType, WindowSize, WindowOverlap, WindowFunction, TransformType, TransformSize, RawReference, SpectraReference, FbeData, FbeDataTime, Custom, )
supermod.DasFbe.subclass = DasFbeSub
# end class DasFbeSub


class DasFbeDataSub(supermod.DasFbeData):
    def __init__(self, FbeDataIndex=None, StartFrequency=None, EndFrequency=None, Dimensions=None, FbeDataArray=None):
        super(DasFbeDataSub, self).__init__(FbeDataIndex, StartFrequency, EndFrequency, Dimensions, FbeDataArray, )
supermod.DasFbeData.subclass = DasFbeDataSub
# end class DasFbeDataSub


class DasProcessedSub(supermod.DasProcessed):
    def __init__(self, Fbe=None, Spectra=None):
        super(DasProcessedSub, self).__init__(Fbe, Spectra, )
supermod.DasProcessed.subclass = DasProcessedSub
# end class DasProcessedSub


class DasRawSub(supermod.DasRaw):
    def __init__(self, uuid=None, RawIndex=None, RawDescription=None, RawDataUnit=None, OutputDataRate=None, StartLocusIndex=None, NumberOfLoci=None, RawData=None, RawDataTime=None, RawDataTriggerTime=None, Custom=None):
        super(DasRawSub, self).__init__(uuid, RawIndex, RawDescription, RawDataUnit, OutputDataRate, StartLocusIndex, NumberOfLoci, RawData, RawDataTime, RawDataTriggerTime, Custom, )
supermod.DasRaw.subclass = DasRawSub
# end class DasRawSub


class DasRawDataSub(supermod.DasRawData):
    def __init__(self, Dimensions=None, RawDataArray=None):
        super(DasRawDataSub, self).__init__(Dimensions, RawDataArray, )
supermod.DasRawData.subclass = DasRawDataSub
# end class DasRawDataSub


class DasSpectraSub(supermod.DasSpectra):
    def __init__(self, uuid=None, SpectraIndex=None, SpectraDescription=None, SpectraDataUnit=None, OutputDataRate=None, StartLocusIndex=None, NumberOfLoci=None, SpatialSamplingInterval=None, SpatialSamplingIntervalUnit=None, FilterType=None, WindowSize=None, WindowOverlap=None, WindowFunction=None, TransformType=None, TransformSize=None, RawReference=None, FbeReference=None, SpectraData=None, SpectraDataTime=None, Custom=None):
        super(DasSpectraSub, self).__init__(uuid, SpectraIndex, SpectraDescription, SpectraDataUnit, OutputDataRate, StartLocusIndex, NumberOfLoci, SpatialSamplingInterval, SpatialSamplingIntervalUnit, FilterType, WindowSize, WindowOverlap, WindowFunction, TransformType, TransformSize, RawReference, FbeReference, SpectraData, SpectraDataTime, Custom, )
supermod.DasSpectra.subclass = DasSpectraSub
# end class DasSpectraSub


class DasSpectraDataSub(supermod.DasSpectraData):
    def __init__(self, StartFrequency=None, EndFrequency=None, Dimensions=None, SpectraDataArray=None):
        super(DasSpectraDataSub, self).__init__(StartFrequency, EndFrequency, Dimensions, SpectraDataArray, )
supermod.DasSpectraData.subclass = DasSpectraDataSub
# end class DasSpectraDataSub


class DasTimeArraySub(supermod.DasTimeArray):
    def __init__(self, StartTime=None, EndTime=None, TimeArray=None):
        super(DasTimeArraySub, self).__init__(StartTime, EndTime, TimeArray, )
supermod.DasTimeArray.subclass = DasTimeArraySub
# end class DasTimeArraySub


class AbstractDtsEquipmentSub(supermod.AbstractDtsEquipment):
    def __init__(self, Name=None, Manufacturer=None, ManufacturingDate=None, Type=None, SupplyDate=None, SupplierModelNumber=None, SoftwareVersion=None, Comment=None, Supplier=None, extensiontype_=None):
        super(AbstractDtsEquipmentSub, self).__init__(Name, Manufacturer, ManufacturingDate, Type, SupplyDate, SupplierModelNumber, SoftwareVersion, Comment, Supplier, extensiontype_, )
supermod.AbstractDtsEquipment.subclass = AbstractDtsEquipmentSub
# end class AbstractDtsEquipmentSub


class DtsPatchCordSub(supermod.DtsPatchCord):
    def __init__(self, FiberLength=None, Description=None):
        super(DtsPatchCordSub, self).__init__(FiberLength, Description, )
supermod.DtsPatchCord.subclass = DtsPatchCordSub
# end class DtsPatchCordSub


class InstrumentSub(supermod.Instrument):
    def __init__(self, Name=None, Manufacturer=None, ManufacturingDate=None, Type=None, SupplyDate=None, SupplierModelNumber=None, SoftwareVersion=None, Comment=None, Supplier=None, InstrumentVendor=None, extensiontype_=None):
        super(InstrumentSub, self).__init__(Name, Manufacturer, ManufacturingDate, Type, SupplyDate, SupplierModelNumber, SoftwareVersion, Comment, Supplier, InstrumentVendor, extensiontype_, )
supermod.Instrument.subclass = InstrumentSub
# end class InstrumentSub


class DtsCalibrationSub(supermod.DtsCalibration):
    def __init__(self, uid=None, DTimCalibration=None, CalibratedBy=None, CalibrationProtocol=None, Parameter=None, Remark=None, ExtensionNameValue=None):
        super(DtsCalibrationSub, self).__init__(uid, DTimCalibration, CalibratedBy, CalibrationProtocol, Parameter, Remark, ExtensionNameValue, )
supermod.DtsCalibration.subclass = DtsCalibrationSub
# end class DtsCalibrationSub


class AbstractAttenuationMeasureSub(supermod.AbstractAttenuationMeasure):
    def __init__(self, extensiontype_=None):
        super(AbstractAttenuationMeasureSub, self).__init__(extensiontype_, )
supermod.AbstractAttenuationMeasure.subclass = AbstractAttenuationMeasureSub
# end class AbstractAttenuationMeasureSub


class AbstractCableSub(supermod.AbstractCable):
    def __init__(self, extensiontype_=None):
        super(AbstractCableSub, self).__init__(extensiontype_, )
supermod.AbstractCable.subclass = AbstractCableSub
# end class AbstractCableSub


class AbstractFiberFacilitySub(supermod.AbstractFiberFacility):
    def __init__(self, extensiontype_=None):
        super(AbstractFiberFacilitySub, self).__init__(extensiontype_, )
supermod.AbstractFiberFacility.subclass = AbstractFiberFacilitySub
# end class AbstractFiberFacilitySub


class FiberCommonSub(supermod.FiberCommon):
    def __init__(self, Name=None, Manufacturer=None, ManufacturingDate=None, Type=None, SupplyDate=None, SupplierModelNumber=None, SoftwareVersion=None, Comment=None, Supplier=None, uid=None, Reflectance=None, Loss=None, ReasonForDecommissioning=None, extensiontype_=None):
        super(FiberCommonSub, self).__init__(Name, Manufacturer, ManufacturingDate, Type, SupplyDate, SupplierModelNumber, SoftwareVersion, Comment, Supplier, uid, Reflectance, Loss, ReasonForDecommissioning, extensiontype_, )
supermod.FiberCommon.subclass = FiberCommonSub
# end class FiberCommonSub


class FiberConnectionSub(supermod.FiberConnection):
    def __init__(self, Name=None, Manufacturer=None, ManufacturingDate=None, Type=None, SupplyDate=None, SupplierModelNumber=None, SoftwareVersion=None, Comment=None, Supplier=None, uid=None, Reflectance=None, Loss=None, ReasonForDecommissioning=None, ConnectorType=None, EndType=None):
        super(FiberConnectionSub, self).__init__(Name, Manufacturer, ManufacturingDate, Type, SupplyDate, SupplierModelNumber, SoftwareVersion, Comment, Supplier, uid, Reflectance, Loss, ReasonForDecommissioning, ConnectorType, EndType, )
supermod.FiberConnection.subclass = FiberConnectionSub
# end class FiberConnectionSub


class FiberControlLineSub(supermod.FiberControlLine):
    def __init__(self, downholeControlLineReference=None, Size=None, Material=None, EncapsulationType=None, EncapsulationSize=None, Comment=None, PumpActivity=None):
        super(FiberControlLineSub, self).__init__(downholeControlLineReference, Size, Material, EncapsulationType, EncapsulationSize, Comment, PumpActivity, )
supermod.FiberControlLine.subclass = FiberControlLineSub
# end class FiberControlLineSub


class FiberConveyanceSub(supermod.FiberConveyance):
    def __init__(self, Cable=None):
        super(FiberConveyanceSub, self).__init__(Cable, )
supermod.FiberConveyance.subclass = FiberConveyanceSub
# end class FiberConveyanceSub


class FiberFacilityGenericSub(supermod.FiberFacilityGeneric):
    def __init__(self, FacilityName=None, FacilityKind=None):
        super(FiberFacilityGenericSub, self).__init__(FacilityName, FacilityKind, )
supermod.FiberFacilityGeneric.subclass = FiberFacilityGenericSub
# end class FiberFacilityGenericSub


class FiberFacilityMappingSub(supermod.FiberFacilityMapping):
    def __init__(self, uid=None, TimeStart=None, TimeEnd=None, Comment=None, FiberFacilityMappingPart=None):
        super(FiberFacilityMappingSub, self).__init__(uid, TimeStart, TimeEnd, Comment, FiberFacilityMappingPart, )
supermod.FiberFacilityMapping.subclass = FiberFacilityMappingSub
# end class FiberFacilityMappingSub


class FiberFacilityMappingPartSub(supermod.FiberFacilityMappingPart):
    def __init__(self, uid=None, OpticalPathDistanceStart=None, OpticalPathDistanceEnd=None, FacilityLengthStart=None, FacilityLengthEnd=None, Comment=None, FiberFacility=None):
        super(FiberFacilityMappingPartSub, self).__init__(uid, OpticalPathDistanceStart, OpticalPathDistanceEnd, FacilityLengthStart, FacilityLengthEnd, Comment, FiberFacility, )
supermod.FiberFacilityMappingPart.subclass = FiberFacilityMappingPartSub
# end class FiberFacilityMappingPartSub


class FiberFacilityPipelineSub(supermod.FiberFacilityPipeline):
    def __init__(self, Name=None, DatumPortReference=None, Installation=None, Kind=None, ContextFacility=None):
        super(FiberFacilityPipelineSub, self).__init__(Name, DatumPortReference, Installation, Kind, ContextFacility, )
supermod.FiberFacilityPipeline.subclass = FiberFacilityPipelineSub
# end class FiberFacilityPipelineSub


class FiberFacilityWellSub(supermod.FiberFacilityWell):
    def __init__(self, Name=None, WellDatum=None, WellboreReference=None):
        super(FiberFacilityWellSub, self).__init__(Name, WellDatum, WellboreReference, )
supermod.FiberFacilityWell.subclass = FiberFacilityWellSub
# end class FiberFacilityWellSub


class FiberOneWayAttenuationSub(supermod.FiberOneWayAttenuation):
    def __init__(self, uid=None, Value=None, AttenuationMeasure=None):
        super(FiberOneWayAttenuationSub, self).__init__(uid, Value, AttenuationMeasure, )
supermod.FiberOneWayAttenuation.subclass = FiberOneWayAttenuationSub
# end class FiberOneWayAttenuationSub


class FiberOpticalPathInventorySub(supermod.FiberOpticalPathInventory):
    def __init__(self, Connection=None, Turnaround=None, Segment=None, Terminator=None, Splice=None):
        super(FiberOpticalPathInventorySub, self).__init__(Connection, Turnaround, Segment, Terminator, Splice, )
supermod.FiberOpticalPathInventory.subclass = FiberOpticalPathInventorySub
# end class FiberOpticalPathInventorySub


class FiberOpticalPathNetworkSub(supermod.FiberOpticalPathNetwork):
    def __init__(self, uid=None, Installation=None, ContextFacility=None, DTimStart=None, DTimeEnd=None, ExistenceTime=None, DTimMin=None, DTimMax=None, Comment=None, ExternalConnect=None, Network=None):
        super(FiberOpticalPathNetworkSub, self).__init__(uid, Installation, ContextFacility, DTimStart, DTimeEnd, ExistenceTime, DTimMin, DTimMax, Comment, ExternalConnect, Network, )
supermod.FiberOpticalPathNetwork.subclass = FiberOpticalPathNetworkSub
# end class FiberOpticalPathNetworkSub


class FiberOpticalPathSegmentSub(supermod.FiberOpticalPathSegment):
    def __init__(self, Name=None, Manufacturer=None, ManufacturingDate=None, Type=None, SupplyDate=None, SupplierModelNumber=None, SoftwareVersion=None, Comment=None, Supplier=None, uid=None, Reflectance=None, Loss=None, ReasonForDecommissioning=None, FiberLength=None, OverStuffing=None, CoreDiameter=None, CladdedDiameter=None, OutsideDiameter=None, Mode=None, Coating=None, Jacket=None, CoreType=None, Parameter=None, SpoolNumberTag=None, SpoolLength=None, CableType=None, RefractiveIndex=None, FiberConveyance=None, OneWayAttenuation=None):
        super(FiberOpticalPathSegmentSub, self).__init__(Name, Manufacturer, ManufacturingDate, Type, SupplyDate, SupplierModelNumber, SoftwareVersion, Comment, Supplier, uid, Reflectance, Loss, ReasonForDecommissioning, FiberLength, OverStuffing, CoreDiameter, CladdedDiameter, OutsideDiameter, Mode, Coating, Jacket, CoreType, Parameter, SpoolNumberTag, SpoolLength, CableType, RefractiveIndex, FiberConveyance, OneWayAttenuation, )
supermod.FiberOpticalPathSegment.subclass = FiberOpticalPathSegmentSub
# end class FiberOpticalPathSegmentSub


class FiberOTDRSub(supermod.FiberOTDR):
    def __init__(self, uid=None, Name=None, ReasonForRun=None, DTimRun=None, DataInOTDRFile=None, OTDRImageFile=None, OpticalPathDistanceStart=None, OpticalPathDistanceEnd=None, Direction=None, Wavelength=None, FiberOTDRInstrumentBox=None, MeasurementContact=None, ExtensionNameValue=None):
        super(FiberOTDRSub, self).__init__(uid, Name, ReasonForRun, DTimRun, DataInOTDRFile, OTDRImageFile, OpticalPathDistanceStart, OpticalPathDistanceEnd, Direction, Wavelength, FiberOTDRInstrumentBox, MeasurementContact, ExtensionNameValue, )
supermod.FiberOTDR.subclass = FiberOTDRSub
# end class FiberOTDRSub


class FiberOTDRInstrumentBoxSub(supermod.FiberOTDRInstrumentBox):
    def __init__(self, Name=None, Manufacturer=None, ManufacturingDate=None, Type=None, SupplyDate=None, SupplierModelNumber=None, SoftwareVersion=None, Comment=None, Supplier=None, InstrumentVendor=None):
        super(FiberOTDRInstrumentBoxSub, self).__init__(Name, Manufacturer, ManufacturingDate, Type, SupplyDate, SupplierModelNumber, SoftwareVersion, Comment, Supplier, InstrumentVendor, )
supermod.FiberOTDRInstrumentBox.subclass = FiberOTDRInstrumentBoxSub
# end class FiberOTDRInstrumentBoxSub


class FiberPathDefectSub(supermod.FiberPathDefect):
    def __init__(self, defectID=None, OpticalPathDistanceStart=None, OpticalPathDistanceEnd=None, DefectType=None, TimeStart=None, TimeEnd=None, Comment=None):
        super(FiberPathDefectSub, self).__init__(defectID, OpticalPathDistanceStart, OpticalPathDistanceEnd, DefectType, TimeStart, TimeEnd, Comment, )
supermod.FiberPathDefect.subclass = FiberPathDefectSub
# end class FiberPathDefectSub


class FiberPumpActivitySub(supermod.FiberPumpActivity):
    def __init__(self, uid=None, Name=None, InstalledFiber=None, PumpingDate=None, EngineerName=None, ServiceCompany=None, PumpFluidType=None, ControlLineFluid=None, PumpDirection=None, FiberEndSeal=None, CableMeterType=None, CableMeterSerialNumber=None, CableMeterCalibrationDate=None, ExcessFiberRecovered=None, Comment=None):
        super(FiberPumpActivitySub, self).__init__(uid, Name, InstalledFiber, PumpingDate, EngineerName, ServiceCompany, PumpFluidType, ControlLineFluid, PumpDirection, FiberEndSeal, CableMeterType, CableMeterSerialNumber, CableMeterCalibrationDate, ExcessFiberRecovered, Comment, )
supermod.FiberPumpActivity.subclass = FiberPumpActivitySub
# end class FiberPumpActivitySub


class FiberRefractiveIndexSub(supermod.FiberRefractiveIndex):
    def __init__(self, uid=None, Value=None, Frequency=None, Wavelength=None):
        super(FiberRefractiveIndexSub, self).__init__(uid, Value, Frequency, Wavelength, )
supermod.FiberRefractiveIndex.subclass = FiberRefractiveIndexSub
# end class FiberRefractiveIndexSub


class FiberSpliceSub(supermod.FiberSplice):
    def __init__(self, Name=None, Manufacturer=None, ManufacturingDate=None, Type=None, SupplyDate=None, SupplierModelNumber=None, SoftwareVersion=None, Comment=None, Supplier=None, uid=None, Reflectance=None, Loss=None, ReasonForDecommissioning=None, SpliceEquipmentUsedReference=None, StrippingType=None, ProtectorType=None, FiberSpliceType=None, PressureRating=None, BendAngle=None):
        super(FiberSpliceSub, self).__init__(Name, Manufacturer, ManufacturingDate, Type, SupplyDate, SupplierModelNumber, SoftwareVersion, Comment, Supplier, uid, Reflectance, Loss, ReasonForDecommissioning, SpliceEquipmentUsedReference, StrippingType, ProtectorType, FiberSpliceType, PressureRating, BendAngle, )
supermod.FiberSplice.subclass = FiberSpliceSub
# end class FiberSpliceSub


class FiberTerminatorSub(supermod.FiberTerminator):
    def __init__(self, Name=None, Manufacturer=None, ManufacturingDate=None, Type=None, SupplyDate=None, SupplierModelNumber=None, SoftwareVersion=None, Comment=None, Supplier=None, uid=None, Reflectance=None, Loss=None, ReasonForDecommissioning=None, TerminationType=None):
        super(FiberTerminatorSub, self).__init__(Name, Manufacturer, ManufacturingDate, Type, SupplyDate, SupplierModelNumber, SoftwareVersion, Comment, Supplier, uid, Reflectance, Loss, ReasonForDecommissioning, TerminationType, )
supermod.FiberTerminator.subclass = FiberTerminatorSub
# end class FiberTerminatorSub


class FiberTurnaroundSub(supermod.FiberTurnaround):
    def __init__(self, Name=None, Manufacturer=None, ManufacturingDate=None, Type=None, SupplyDate=None, SupplierModelNumber=None, SoftwareVersion=None, Comment=None, Supplier=None, uid=None, Reflectance=None, Loss=None, ReasonForDecommissioning=None):
        super(FiberTurnaroundSub, self).__init__(Name, Manufacturer, ManufacturingDate, Type, SupplyDate, SupplierModelNumber, SoftwareVersion, Comment, Supplier, uid, Reflectance, Loss, ReasonForDecommissioning, )
supermod.FiberTurnaround.subclass = FiberTurnaroundSub
# end class FiberTurnaroundSub


class FrequencySub(supermod.Frequency):
    def __init__(self, Frequency_member=None):
        super(FrequencySub, self).__init__(Frequency_member, )
supermod.Frequency.subclass = FrequencySub
# end class FrequencySub


class InterventionConveyanceSub(supermod.InterventionConveyance):
    def __init__(self, InterventionConveyanceType=None, Comment=None):
        super(InterventionConveyanceSub, self).__init__(InterventionConveyanceType, Comment, )
supermod.InterventionConveyance.subclass = InterventionConveyanceSub
# end class InterventionConveyanceSub


class PermanentCableSub(supermod.PermanentCable):
    def __init__(self, PermanentCableInstallationType=None, Comment=None):
        super(PermanentCableSub, self).__init__(PermanentCableInstallationType, Comment, )
supermod.PermanentCable.subclass = PermanentCableSub
# end class PermanentCableSub


class WaveLengthSub(supermod.WaveLength):
    def __init__(self, WaveLength_member=None):
        super(WaveLengthSub, self).__init__(WaveLength_member, )
supermod.WaveLength.subclass = WaveLengthSub
# end class WaveLengthSub


class AbstractDateTimeClassSub(supermod.AbstractDateTimeClass):
    def __init__(self, DTime=None, Date=None, Month=None, extensiontype_=None):
        super(AbstractDateTimeClassSub, self).__init__(DTime, Date, Month, extensiontype_, )
supermod.AbstractDateTimeClass.subclass = AbstractDateTimeClassSub
# end class AbstractDateTimeClassSub


class AbstractFluidComponentSub(supermod.AbstractFluidComponent):
    def __init__(self, uid=None, MassFraction=None, MoleFraction=None, extensiontype_=None):
        super(AbstractFluidComponentSub, self).__init__(uid, MassFraction, MoleFraction, extensiontype_, )
supermod.AbstractFluidComponent.subclass = AbstractFluidComponentSub
# end class AbstractFluidComponentSub


class BusinessAssociateSub(supermod.BusinessAssociate):
    def __init__(self, Name=None, Role=None, Alias=None, Address=None, PhoneNumber=None, Email=None, AssociatedWith=None, Contact=None, PersonnelCount=None, PersonName=None):
        super(BusinessAssociateSub, self).__init__(Name, Role, Alias, Address, PhoneNumber, Email, AssociatedWith, Contact, PersonnelCount, PersonName, )
supermod.BusinessAssociate.subclass = BusinessAssociateSub
# end class BusinessAssociateSub


class CalibrationParameterSub(supermod.CalibrationParameter):
    def __init__(self, uom=None, name=None):
        super(CalibrationParameterSub, self).__init__(uom, name, )
supermod.CalibrationParameter.subclass = CalibrationParameterSub
# end class CalibrationParameterSub


class DatedCommentSub(supermod.DatedComment):
    def __init__(self, uid=None, Who=None, Role=None, StartTime=None, EndTime=None, Remark=None):
        super(DatedCommentSub, self).__init__(uid, Who, Role, StartTime, EndTime, Remark, )
supermod.DatedComment.subclass = DatedCommentSub
# end class DatedCommentSub


class EmailQualifierStructSub(supermod.EmailQualifierStruct):
    def __init__(self, qualifier=None):
        super(EmailQualifierStructSub, self).__init__(qualifier, )
supermod.EmailQualifierStruct.subclass = EmailQualifierStructSub
# end class EmailQualifierStructSub


class EndpointQualifiedDateSub(supermod.EndpointQualifiedDate):
    def __init__(self, endpoint=None):
        super(EndpointQualifiedDateSub, self).__init__(endpoint, )
supermod.EndpointQualifiedDate.subclass = EndpointQualifiedDateSub
# end class EndpointQualifiedDateSub


class EndpointQualifiedDateTimeSub(supermod.EndpointQualifiedDateTime):
    def __init__(self, endpoint=None):
        super(EndpointQualifiedDateTimeSub, self).__init__(endpoint, )
supermod.EndpointQualifiedDateTime.subclass = EndpointQualifiedDateTimeSub
# end class EndpointQualifiedDateTimeSub


class FacilityIdentifierSub(supermod.FacilityIdentifier):
    def __init__(self, uid=None, Name=None, Installation=None, Kind=None, ContextFacility=None, BusinessUnit=None, Operator=None, GeographicContext=None, valueOf_=None, mixedclass_=None, content_=None):
        super(FacilityIdentifierSub, self).__init__(uid, Name, Installation, Kind, ContextFacility, BusinessUnit, Operator, GeographicContext, valueOf_, mixedclass_, content_, )
supermod.FacilityIdentifier.subclass = FacilityIdentifierSub
# end class FacilityIdentifierSub


class FacilityIdentifierStructSub(supermod.FacilityIdentifierStruct):
    def __init__(self, kind=None, siteKind=None, namingSystem=None, uidRef=None, valueOf_=None, mixedclass_=None, content_=None):
        super(FacilityIdentifierStructSub, self).__init__(kind, siteKind, namingSystem, uidRef, valueOf_, mixedclass_, content_, )
supermod.FacilityIdentifierStruct.subclass = FacilityIdentifierStructSub
# end class FacilityIdentifierStructSub


class FluidComponentSub(supermod.FluidComponent):
    def __init__(self, fluidComponentReference=None, MassFraction=None, MoleFraction=None, KValue=None):
        super(FluidComponentSub, self).__init__(fluidComponentReference, MassFraction, MoleFraction, KValue, )
supermod.FluidComponent.subclass = FluidComponentSub
# end class FluidComponentSub


class FluidComponentCatalogSub(supermod.FluidComponentCatalog):
    def __init__(self, StockTankOil=None, NaturalGas=None, FormationWater=None, PureFluidComponent=None, PseudoFluidComponent=None, PlusFluidComponent=None):
        super(FluidComponentCatalogSub, self).__init__(StockTankOil, NaturalGas, FormationWater, PureFluidComponent, PseudoFluidComponent, PlusFluidComponent, )
supermod.FluidComponentCatalog.subclass = FluidComponentCatalogSub
# end class FluidComponentCatalogSub


class FormationWaterSub(supermod.FormationWater):
    def __init__(self, uid=None, MassFraction=None, MoleFraction=None, SpecificGravity=None, Salinity=None, Remark=None):
        super(FormationWaterSub, self).__init__(uid, MassFraction, MoleFraction, SpecificGravity, Salinity, Remark, )
supermod.FormationWater.subclass = FormationWaterSub
# end class FormationWaterSub


class GeneralAddressSub(supermod.GeneralAddress):
    def __init__(self, uid=None, kind=None, Name=None, Street=None, City=None, Country=None, County=None, PostalCode=None, State=None, Province=None):
        super(GeneralAddressSub, self).__init__(uid, kind, Name, Street, City, Country, County, PostalCode, State, Province, )
supermod.GeneralAddress.subclass = GeneralAddressSub
# end class GeneralAddressSub


class GeneralMeasureTypeSub(supermod.GeneralMeasureType):
    def __init__(self, uom=None):
        super(GeneralMeasureTypeSub, self).__init__(uom, )
supermod.GeneralMeasureType.subclass = GeneralMeasureTypeSub
# end class GeneralMeasureTypeSub


class GeographicContextSub(supermod.GeographicContext):
    def __init__(self, Country=None, State=None, County=None, Field=None, Comment=None, OffshoreLocation=None):
        super(GeographicContextSub, self).__init__(Country, State, County, Field, Comment, OffshoreLocation, )
supermod.GeographicContext.subclass = GeographicContextSub
# end class GeographicContextSub


class GeologyFeatureSub(supermod.GeologyFeature):
    def __init__(self, uid=None, Name=None, GeologyType=None, MdTop=None, MdBottom=None, TvdTop=None, TvdBottom=None):
        super(GeologyFeatureSub, self).__init__(uid, Name, GeologyType, MdTop, MdBottom, TvdTop, TvdBottom, )
supermod.GeologyFeature.subclass = GeologyFeatureSub
# end class GeologyFeatureSub


class IndexedObjectSub(supermod.IndexedObject):
    def __init__(self, index=None, name=None, uom=None, description=None):
        super(IndexedObjectSub, self).__init__(index, name, uom, description, )
supermod.IndexedObject.subclass = IndexedObjectSub
# end class IndexedObjectSub


class KeywordValueStructSub(supermod.KeywordValueStruct):
    def __init__(self, keyword=None, valueOf_=None):
        super(KeywordValueStructSub, self).__init__(keyword, valueOf_, )
supermod.KeywordValueStruct.subclass = KeywordValueStructSub
# end class KeywordValueStructSub


class LiquidCompositionSub(supermod.LiquidComposition):
    def __init__(self, Remark=None, LiquidComponent=None):
        super(LiquidCompositionSub, self).__init__(Remark, LiquidComponent, )
supermod.LiquidComposition.subclass = LiquidCompositionSub
# end class LiquidCompositionSub


class MeasuredDepthCoordSub(supermod.MeasuredDepthCoord):
    def __init__(self, uom=None, valueOf_=None):
        super(MeasuredDepthCoordSub, self).__init__(uom, valueOf_, )
supermod.MeasuredDepthCoord.subclass = MeasuredDepthCoordSub
# end class MeasuredDepthCoordSub


class MeasureOrQuantitySub(supermod.MeasureOrQuantity):
    def __init__(self, uom=None, valueOf_=None):
        super(MeasureOrQuantitySub, self).__init__(uom, valueOf_, )
supermod.MeasureOrQuantity.subclass = MeasureOrQuantitySub
# end class MeasureOrQuantitySub


class NameStructSub(supermod.NameStruct):
    def __init__(self, authority=None, valueOf_=None):
        super(NameStructSub, self).__init__(authority, valueOf_, )
supermod.NameStruct.subclass = NameStructSub
# end class NameStructSub


class NaturalGasSub(supermod.NaturalGas):
    def __init__(self, uid=None, MassFraction=None, MoleFraction=None, GasGravity=None, MolecularWeight=None, GrossEnergyContentPerUnitMass=None, NetEnergyContentPerUnitMass=None, GrossEnergyContentPerUnitVolume=None, NetEnergyContentPerUnitVolume=None, Remark=None):
        super(NaturalGasSub, self).__init__(uid, MassFraction, MoleFraction, GasGravity, MolecularWeight, GrossEnergyContentPerUnitMass, NetEnergyContentPerUnitMass, GrossEnergyContentPerUnitVolume, NetEnergyContentPerUnitVolume, Remark, )
supermod.NaturalGas.subclass = NaturalGasSub
# end class NaturalGasSub


class NorthSeaOffshoreSub(supermod.NorthSeaOffshore):
    def __init__(self, AreaName=None, Quadrant=None, BlockSuffix=None):
        super(NorthSeaOffshoreSub, self).__init__(AreaName, Quadrant, BlockSuffix, )
supermod.NorthSeaOffshore.subclass = NorthSeaOffshoreSub
# end class NorthSeaOffshoreSub


class OffshoreLocationSub(supermod.OffshoreLocation):
    def __init__(self, AreaName=None, BlockID=None, Comment=None, NorthSeaOffshore=None):
        super(OffshoreLocationSub, self).__init__(AreaName, BlockID, Comment, NorthSeaOffshore, )
supermod.OffshoreLocation.subclass = OffshoreLocationSub
# end class OffshoreLocationSub


class OverallCompositionSub(supermod.OverallComposition):
    def __init__(self, Remark=None, FluidComponent=None):
        super(OverallCompositionSub, self).__init__(Remark, FluidComponent, )
supermod.OverallComposition.subclass = OverallCompositionSub
# end class OverallCompositionSub


class PersonNameSub(supermod.PersonName):
    def __init__(self, Prefix=None, First=None, Middle=None, Last=None, Suffix=None):
        super(PersonNameSub, self).__init__(Prefix, First, Middle, Last, Suffix, )
supermod.PersonName.subclass = PersonNameSub
# end class PersonNameSub


class PhoneNumberStructSub(supermod.PhoneNumberStruct):
    def __init__(self, type_=None, qualifier=None, extension=None, valueOf_=None, mixedclass_=None, content_=None):
        super(PhoneNumberStructSub, self).__init__(type_, qualifier, extension, valueOf_, mixedclass_, content_, )
supermod.PhoneNumberStruct.subclass = PhoneNumberStructSub
# end class PhoneNumberStructSub


class PlusFluidComponentSub(supermod.PlusFluidComponent):
    def __init__(self, uid=None, MassFraction=None, MoleFraction=None, Kind=None, SpecificGravity=None, StartingCarbonNumber=None, StartingBoilingPoint=None, AvgDensity=None, AvgMolecularWeight=None, Remark=None):
        super(PlusFluidComponentSub, self).__init__(uid, MassFraction, MoleFraction, Kind, SpecificGravity, StartingCarbonNumber, StartingBoilingPoint, AvgDensity, AvgMolecularWeight, Remark, )
supermod.PlusFluidComponent.subclass = PlusFluidComponentSub
# end class PlusFluidComponentSub


class ProductFlowExternalReferenceSub(supermod.ProductFlowExternalReference):
    def __init__(self, uid=None, PortReference=None, ConnectedPortReference=None, ConnectedModelReference=None, ConnectedInstallation=None):
        super(ProductFlowExternalReferenceSub, self).__init__(uid, PortReference, ConnectedPortReference, ConnectedModelReference, ConnectedInstallation, )
supermod.ProductFlowExternalReference.subclass = ProductFlowExternalReferenceSub
# end class ProductFlowExternalReferenceSub


class ProductFlowNetworkSub(supermod.ProductFlowNetwork):
    def __init__(self, uid=None, Name=None, PlanName=None, ParentNetworkReference=None, Comment=None, Port=None, Plan=None, ChangeLog=None, Unit=None):
        super(ProductFlowNetworkSub, self).__init__(uid, Name, PlanName, ParentNetworkReference, Comment, Port, Plan, ChangeLog, Unit, )
supermod.ProductFlowNetwork.subclass = ProductFlowNetworkSub
# end class ProductFlowNetworkSub


class PseudoFluidComponentSub(supermod.PseudoFluidComponent):
    def __init__(self, uid=None, MassFraction=None, MoleFraction=None, Kind=None, SpecificGravity=None, StartingCarbonNumber=None, EndingCarbonNumber=None, AvgMolecularWeight=None, AvgDensity=None, StartingBoilingPoint=None, EndingBoilingPoint=None, AvgBoilingPoint=None, Remark=None):
        super(PseudoFluidComponentSub, self).__init__(uid, MassFraction, MoleFraction, Kind, SpecificGravity, StartingCarbonNumber, EndingCarbonNumber, AvgMolecularWeight, AvgDensity, StartingBoilingPoint, EndingBoilingPoint, AvgBoilingPoint, Remark, )
supermod.PseudoFluidComponent.subclass = PseudoFluidComponentSub
# end class PseudoFluidComponentSub


class PureFluidComponentSub(supermod.PureFluidComponent):
    def __init__(self, uid=None, MassFraction=None, MoleFraction=None, Kind=None, MolecularWeight=None, HydrocarbonFlag=None, Remark=None):
        super(PureFluidComponentSub, self).__init__(uid, MassFraction, MoleFraction, Kind, MolecularWeight, HydrocarbonFlag, Remark, )
supermod.PureFluidComponent.subclass = PureFluidComponentSub
# end class PureFluidComponentSub


class StartEndDateSub(supermod.StartEndDate):
    def __init__(self, DTime=None, Date=None, Month=None, DateStart=None, DateEnd=None):
        super(StartEndDateSub, self).__init__(DTime, Date, Month, DateStart, DateEnd, )
supermod.StartEndDate.subclass = StartEndDateSub
# end class StartEndDateSub


class StartEndTimeSub(supermod.StartEndTime):
    def __init__(self, DTime=None, Date=None, Month=None, DTimStart=None, DTimEnd=None):
        super(StartEndTimeSub, self).__init__(DTime, Date, Month, DTimStart, DTimEnd, )
supermod.StartEndTime.subclass = StartEndTimeSub
# end class StartEndTimeSub


class StockTankOilSub(supermod.StockTankOil):
    def __init__(self, uid=None, MassFraction=None, MoleFraction=None, APIGravity=None, MolecularWeight=None, GrossEnergyContentPerUnitMass=None, NetEnergyContentPerUnitMass=None, GrossEnergyContentPerUnitVolume=None, NetEnergyContentPerUnitVolume=None, Remark=None):
        super(StockTankOilSub, self).__init__(uid, MassFraction, MoleFraction, APIGravity, MolecularWeight, GrossEnergyContentPerUnitMass, NetEnergyContentPerUnitMass, GrossEnergyContentPerUnitVolume, NetEnergyContentPerUnitVolume, Remark, )
supermod.StockTankOil.subclass = StockTankOilSub
# end class StockTankOilSub


class VaporCompositionSub(supermod.VaporComposition):
    def __init__(self, Remark=None, VaporComponent=None):
        super(VaporCompositionSub, self).__init__(Remark, VaporComponent, )
supermod.VaporComposition.subclass = VaporCompositionSub
# end class VaporCompositionSub


class VolumeQualifiedMeasureSub(supermod.VolumeQualifiedMeasure):
    def __init__(self, status=None):
        super(VolumeQualifiedMeasureSub, self).__init__(status, )
supermod.VolumeQualifiedMeasure.subclass = VolumeQualifiedMeasureSub
# end class VolumeQualifiedMeasureSub


class WellElevationCoordSub(supermod.WellElevationCoord):
    def __init__(self, uom=None):
        super(WellElevationCoordSub, self).__init__(uom, )
supermod.WellElevationCoord.subclass = WellElevationCoordSub
# end class WellElevationCoordSub


class WellVerticalDepthCoordSub(supermod.WellVerticalDepthCoord):
    def __init__(self, uom=None):
        super(WellVerticalDepthCoordSub, self).__init__(uom, )
supermod.WellVerticalDepthCoord.subclass = WellVerticalDepthCoordSub
# end class WellVerticalDepthCoordSub


class CommonPropertiesProductVolumeSub(supermod.CommonPropertiesProductVolume):
    def __init__(self, Gor=None, GorMTD=None, GasLiquidRatio=None, WaterConcMass=None, WaterConcVol=None, Atmosphere=None, Temp=None, Pres=None, AbsoluteMinPres=None, Mass=None, Work=None, Efficiency=None, Rvp=None, Tvp=None, Bsw=None, BswPrevious=None, DensityFlowRate=None, Concentration=None, MolecularWeight=None, WeightPercent=None, MolePercent=None, MoleAmt=None, Sg=None, HcDewpoint=None, WaterDewpoint=None, WobbeIndex=None, GrossCalorificValueStd=None, RvpStabilizedCrude=None, BswStabilizedCrude=None, DensityStabilizedCrude=None, DensityValue=None, PortDiff=None, VolumeValue=None, FlowRateValue=None):
        super(CommonPropertiesProductVolumeSub, self).__init__(Gor, GorMTD, GasLiquidRatio, WaterConcMass, WaterConcVol, Atmosphere, Temp, Pres, AbsoluteMinPres, Mass, Work, Efficiency, Rvp, Tvp, Bsw, BswPrevious, DensityFlowRate, Concentration, MolecularWeight, WeightPercent, MolePercent, MoleAmt, Sg, HcDewpoint, WaterDewpoint, WobbeIndex, GrossCalorificValueStd, RvpStabilizedCrude, BswStabilizedCrude, DensityStabilizedCrude, DensityValue, PortDiff, VolumeValue, FlowRateValue, )
supermod.CommonPropertiesProductVolume.subclass = CommonPropertiesProductVolumeSub
# end class CommonPropertiesProductVolumeSub


class AbstractMeasureDataTypeSub(supermod.AbstractMeasureDataType):
    def __init__(self, extensiontype_=None):
        super(AbstractMeasureDataTypeSub, self).__init__(extensiontype_, )
supermod.AbstractMeasureDataType.subclass = AbstractMeasureDataTypeSub
# end class AbstractMeasureDataTypeSub


class AbstractRefProductFlowSub(supermod.AbstractRefProductFlow):
    def __init__(self, extensiontype_=None):
        super(AbstractRefProductFlowSub, self).__init__(extensiontype_, )
supermod.AbstractRefProductFlow.subclass = AbstractRefProductFlowSub
# end class AbstractRefProductFlowSub


class AbstractRelatedFacilityObjectSub(supermod.AbstractRelatedFacilityObject):
    def __init__(self, FacilityParent=None, extensiontype_=None):
        super(AbstractRelatedFacilityObjectSub, self).__init__(FacilityParent, extensiontype_, )
supermod.AbstractRelatedFacilityObject.subclass = AbstractRelatedFacilityObjectSub
# end class AbstractRelatedFacilityObjectSub


class CurveDataSub(supermod.CurveData):
    def __init__(self, uid=None, Index=None, Value=None):
        super(CurveDataSub, self).__init__(uid, Index, Value, )
supermod.CurveData.subclass = CurveDataSub
# end class CurveDataSub


class CurveDefinitionSub(supermod.CurveDefinition):
    def __init__(self, uid=None, Order=None, Parameter=None, IsIndex=None, MeasureClass=None, Unit=None):
        super(CurveDefinitionSub, self).__init__(uid, Order, Parameter, IsIndex, MeasureClass, Unit, )
supermod.CurveDefinition.subclass = CurveDefinitionSub
# end class CurveDefinitionSub


class FacilityParentSub(supermod.FacilityParent):
    def __init__(self, FacilityParent=None, Name=None, FacilityParent1=None, FacilityParent2=None):
        super(FacilityParentSub, self).__init__(FacilityParent, Name, FacilityParent1, FacilityParent2, )
supermod.FacilityParent.subclass = FacilityParentSub
# end class FacilityParentSub


class FacilityUnitPortSub(supermod.FacilityUnitPort):
    def __init__(self, FacilityParent=None, PortReference=None, UnitReference=None, NetworkReference=None):
        super(FacilityUnitPortSub, self).__init__(FacilityParent, PortReference, UnitReference, NetworkReference, )
supermod.FacilityUnitPort.subclass = FacilityUnitPortSub
# end class FacilityUnitPortSub


class IntegerDataSub(supermod.IntegerData):
    def __init__(self, IntegerValue=None):
        super(IntegerDataSub, self).__init__(IntegerValue, )
supermod.IntegerData.subclass = IntegerDataSub
# end class IntegerDataSub


class OwnershipBusinessAcctSub(supermod.OwnershipBusinessAcct):
    def __init__(self):
        super(OwnershipBusinessAcctSub, self).__init__()
supermod.OwnershipBusinessAcct.subclass = OwnershipBusinessAcctSub
# end class OwnershipBusinessAcctSub


class ParentfacilitySub(supermod.Parentfacility):
    def __init__(self, ParentfacilityReference=None):
        super(ParentfacilitySub, self).__init__(ParentfacilityReference, )
supermod.Parentfacility.subclass = ParentfacilitySub
# end class ParentfacilitySub


class ProductVolumeAlertSub(supermod.ProductVolumeAlert):
    def __init__(self, Target=None, Level=None, Type=None, Description=None):
        super(ProductVolumeAlertSub, self).__init__(Target, Level, Type, Description, )
supermod.ProductVolumeAlert.subclass = ProductVolumeAlertSub
# end class ProductVolumeAlertSub


class ProductVolumeBalanceDetailSub(supermod.ProductVolumeBalanceDetail):
    def __init__(self, uid=None, Owner=None, SourceUnit=None, Share=None, AccountNumber=None, SampleAnalysisResult=None, ComponentContent=None, Event=None, VolumeValue=None):
        super(ProductVolumeBalanceDetailSub, self).__init__(uid, Owner, SourceUnit, Share, AccountNumber, SampleAnalysisResult, ComponentContent, Event, VolumeValue, )
supermod.ProductVolumeBalanceDetail.subclass = ProductVolumeBalanceDetailSub
# end class ProductVolumeBalanceDetailSub


class ProductVolumeBalanceEventSub(supermod.ProductVolumeBalanceEvent):
    def __init__(self, uid=None, Date=None, Kind=None):
        super(ProductVolumeBalanceEventSub, self).__init__(uid, Date, Kind, )
supermod.ProductVolumeBalanceEvent.subclass = ProductVolumeBalanceEventSub
# end class ProductVolumeBalanceEventSub


class ProductVolumeBalanceSetSub(supermod.ProductVolumeBalanceSet):
    def __init__(self, uid=None, Kind=None, CargoNumber=None, CargoBatchNumber=None, Shipper=None, BalanceDetail=None, Destination=None):
        super(ProductVolumeBalanceSetSub, self).__init__(uid, Kind, CargoNumber, CargoBatchNumber, Shipper, BalanceDetail, Destination, )
supermod.ProductVolumeBalanceSet.subclass = ProductVolumeBalanceSetSub
# end class ProductVolumeBalanceSetSub


class ProductVolumeBusinessSubUnitSub(supermod.ProductVolumeBusinessSubUnit):
    def __init__(self, uid=None, Kind=None, OwnershipBusinessAcct=None):
        super(ProductVolumeBusinessSubUnitSub, self).__init__(uid, Kind, OwnershipBusinessAcct, )
supermod.ProductVolumeBusinessSubUnit.subclass = ProductVolumeBusinessSubUnitSub
# end class ProductVolumeBusinessSubUnitSub


class ProductVolumeBusinessUnitSub(supermod.ProductVolumeBusinessUnit):
    def __init__(self, uid=None, Kind=None, Name=None, Description=None, SubUnit=None):
        super(ProductVolumeBusinessUnitSub, self).__init__(uid, Kind, Name, Description, SubUnit, )
supermod.ProductVolumeBusinessUnit.subclass = ProductVolumeBusinessUnitSub
# end class ProductVolumeBusinessUnitSub


class ProductVolumeComponentContentSub(supermod.ProductVolumeComponentContent):
    def __init__(self, uid=None, Kind=None, ReferenceKind=None, Properties=None):
        super(ProductVolumeComponentContentSub, self).__init__(uid, Kind, ReferenceKind, Properties, )
supermod.ProductVolumeComponentContent.subclass = ProductVolumeComponentContentSub
# end class ProductVolumeComponentContentSub


class ProductVolumeDestinationSub(supermod.ProductVolumeDestination):
    def __init__(self, Name=None, Type=None, Country=None):
        super(ProductVolumeDestinationSub, self).__init__(Name, Type, Country, )
supermod.ProductVolumeDestination.subclass = ProductVolumeDestinationSub
# end class ProductVolumeDestinationSub


class ProductVolumeFacilitySub(supermod.ProductVolumeFacility):
    def __init__(self, uid=None, FacilityParent=None, FacilityParent2=None, FacilityAlias=None, Unit=None, NetWork=None, Name=None, StatusWell=None, FluidWell=None, OperatingMethod=None, WellProducing=None, WellInjecting=None, Capacity=None, OperationTime=None, Flow=None, ParameterSet=None, DowntimeReason=None, Comment=None):
        super(ProductVolumeFacilitySub, self).__init__(uid, FacilityParent, FacilityParent2, FacilityAlias, Unit, NetWork, Name, StatusWell, FluidWell, OperatingMethod, WellProducing, WellInjecting, Capacity, OperationTime, Flow, ParameterSet, DowntimeReason, Comment, )
supermod.ProductVolumeFacility.subclass = ProductVolumeFacilitySub
# end class ProductVolumeFacilitySub


class ProductVolumeFlowSub(supermod.ProductVolumeFlow):
    def __init__(self, uid=None, Name=None, Kind=None, Port=None, Direction=None, Facility=None, FacilityAlias=None, Qualifier=None, SubQualifier=None, Version=None, VersionSource=None, SourceFlow=None, RelatedFacility=None, Product=None, Properties=None):
        super(ProductVolumeFlowSub, self).__init__(uid, Name, Kind, Port, Direction, Facility, FacilityAlias, Qualifier, SubQualifier, Version, VersionSource, SourceFlow, RelatedFacility, Product, Properties, )
supermod.ProductVolumeFlow.subclass = ProductVolumeFlowSub
# end class ProductVolumeFlowSub


class ProductVolumeParameterSetSub(supermod.ProductVolumeParameterSet):
    def __init__(self, uid=None, Name=None, ChildFacilityIdentifier=None, Port=None, MeasureClass=None, CoordinateReferenceSystem=None, Qualifier=None, SubQualifier=None, Version=None, VersionSource=None, Product=None, PeriodKind=None, Comment=None, Parameter=None, CurveDefinition=None):
        super(ProductVolumeParameterSetSub, self).__init__(uid, Name, ChildFacilityIdentifier, Port, MeasureClass, CoordinateReferenceSystem, Qualifier, SubQualifier, Version, VersionSource, Product, PeriodKind, Comment, Parameter, CurveDefinition, )
supermod.ProductVolumeParameterSet.subclass = ProductVolumeParameterSetSub
# end class ProductVolumeParameterSetSub


class ProductVolumeParameterValueSub(supermod.ProductVolumeParameterValue):
    def __init__(self, uid=None, DTim=None, DTimEnd=None, Port=None, Unit=None, Alert=None, MeasureDataType=None):
        super(ProductVolumeParameterValueSub, self).__init__(uid, DTim, DTimEnd, Port, Unit, Alert, MeasureDataType, )
supermod.ProductVolumeParameterValue.subclass = ProductVolumeParameterValueSub
# end class ProductVolumeParameterValueSub


class ProductVolumePeriodSub(supermod.ProductVolumePeriod):
    def __init__(self, uid=None, Kind=None, Comment=None, BalanceSet=None, ComponentContent=None, DateTime=None, Properties=None, Alert=None):
        super(ProductVolumePeriodSub, self).__init__(uid, Kind, Comment, BalanceSet, ComponentContent, DateTime, Properties, Alert, )
supermod.ProductVolumePeriod.subclass = ProductVolumePeriodSub
# end class ProductVolumePeriodSub


class ProductVolumePortDifferenceSub(supermod.ProductVolumePortDifference):
    def __init__(self, uid=None, PortReference=None, PresDiff=None, TempDiff=None, ChokeSize=None, ChokeRelative=None):
        super(ProductVolumePortDifferenceSub, self).__init__(uid, PortReference, PresDiff, TempDiff, ChokeSize, ChokeRelative, )
supermod.ProductVolumePortDifference.subclass = ProductVolumePortDifferenceSub
# end class ProductVolumePortDifferenceSub


class ProductVolumeProductSub(supermod.ProductVolumeProduct):
    def __init__(self, uid=None, Kind=None, Name=None, SplitFactor=None, MassFraction=None, MoleFraction=None, ComponentContent=None, SourceFlow=None, Period=None, Properties=None):
        super(ProductVolumeProductSub, self).__init__(uid, Kind, Name, SplitFactor, MassFraction, MoleFraction, ComponentContent, SourceFlow, Period, Properties, )
supermod.ProductVolumeProduct.subclass = ProductVolumeProductSub
# end class ProductVolumeProductSub


class ProductVolumeRelatedFacilitySub(supermod.ProductVolumeRelatedFacility):
    def __init__(self, Kind=None, RelatedFacilityObject=None):
        super(ProductVolumeRelatedFacilitySub, self).__init__(Kind, RelatedFacilityObject, )
supermod.ProductVolumeRelatedFacility.subclass = ProductVolumeRelatedFacilitySub
# end class ProductVolumeRelatedFacilitySub


class ReferenceFlowSub(supermod.ReferenceFlow):
    def __init__(self, FlowReference=None):
        super(ReferenceFlowSub, self).__init__(FlowReference, )
supermod.ReferenceFlow.subclass = ReferenceFlowSub
# end class ReferenceFlowSub


class StringDataSub(supermod.StringData):
    def __init__(self, StringValue=None):
        super(StringDataSub, self).__init__(StringValue, )
supermod.StringData.subclass = StringDataSub
# end class StringDataSub


class ConnectedNodeSub(supermod.ConnectedNode):
    def __init__(self, uid=None, Node=None, PlanName=None, DTimStart=None, DTimEnd=None, Comment=None):
        super(ConnectedNodeSub, self).__init__(uid, Node, PlanName, DTimStart, DTimEnd, Comment, )
supermod.ConnectedNode.subclass = ConnectedNodeSub
# end class ConnectedNodeSub


class ExpectedFlowQualifierSub(supermod.ExpectedFlowQualifier):
    def __init__(self, extensiontype_=None):
        super(ExpectedFlowQualifierSub, self).__init__(extensiontype_, )
supermod.ExpectedFlowQualifier.subclass = ExpectedFlowQualifierSub
# end class ExpectedFlowQualifierSub


class ProductFlowChangeLogSub(supermod.ProductFlowChangeLog):
    def __init__(self, uid=None, Name=None, DTim=None, Reason=None):
        super(ProductFlowChangeLogSub, self).__init__(uid, Name, DTim, Reason, )
supermod.ProductFlowChangeLog.subclass = ProductFlowChangeLogSub
# end class ProductFlowChangeLogSub


class ProductFlowExpectedUnitPropertySub(supermod.ProductFlowExpectedUnitProperty):
    def __init__(self, uid=None, Property=None, ChildFacilityIdentifier=None, TagAlias=None, Deadband=None, MaximumFrequency=None, Comment=None, ExpectedFlowQualifier=None, ExpectedFlowProduct=None):
        super(ProductFlowExpectedUnitPropertySub, self).__init__(uid, Property, ChildFacilityIdentifier, TagAlias, Deadband, MaximumFrequency, Comment, ExpectedFlowQualifier, ExpectedFlowProduct, )
supermod.ProductFlowExpectedUnitProperty.subclass = ProductFlowExpectedUnitPropertySub
# end class ProductFlowExpectedUnitPropertySub


class ProductFlowExternalPortSub(supermod.ProductFlowExternalPort):
    def __init__(self, uid=None, Name=None, Direction=None, Exposed=None, ConnectedNode=None, Comment=None):
        super(ProductFlowExternalPortSub, self).__init__(uid, Name, Direction, Exposed, ConnectedNode, Comment, )
supermod.ProductFlowExternalPort.subclass = ProductFlowExternalPortSub
# end class ProductFlowExternalPortSub


class ProductFlowNetworkPlanSub(supermod.ProductFlowNetworkPlan):
    def __init__(self, uid=None, Name=None, DTimStart=None, Purpose=None, ChangeLog=None):
        super(ProductFlowNetworkPlanSub, self).__init__(uid, Name, DTimStart, Purpose, ChangeLog, )
supermod.ProductFlowNetworkPlan.subclass = ProductFlowNetworkPlanSub
# end class ProductFlowNetworkPlanSub


class ProductFlowPortSub(supermod.ProductFlowPort):
    def __init__(self, uid=None, Direction=None, Name=None, PlanName=None, Facility=None, FacilityAlias=None, Exposed=None, Comment=None, ExpectedFlowProperty=None, ConnectedNode=None, ExpectedFlowProduct=None):
        super(ProductFlowPortSub, self).__init__(uid, Direction, Name, PlanName, Facility, FacilityAlias, Exposed, Comment, ExpectedFlowProperty, ConnectedNode, ExpectedFlowProduct, )
supermod.ProductFlowPort.subclass = ProductFlowPortSub
# end class ProductFlowPortSub


class ProductFlowQualifierExpectedSub(supermod.ProductFlowQualifierExpected):
    def __init__(self, uid=None, Flow=None, Product=None, Qualifier=None):
        super(ProductFlowQualifierExpectedSub, self).__init__(uid, Flow, Product, Qualifier, )
supermod.ProductFlowQualifierExpected.subclass = ProductFlowQualifierExpectedSub
# end class ProductFlowQualifierExpectedSub


class ProductFlowUnitSub(supermod.ProductFlowUnit):
    def __init__(self, uid=None, Name=None, PlanName=None, InternalNetworkReference=None, Facility=None, FacilityParent1=None, FacilityParent2=None, ContextFacility=None, Comment=None, ExpectedProperty=None, Port=None, RelativeCoordinate=None, FacilityAlias=None):
        super(ProductFlowUnitSub, self).__init__(uid, Name, PlanName, InternalNetworkReference, Facility, FacilityParent1, FacilityParent2, ContextFacility, Comment, ExpectedProperty, Port, RelativeCoordinate, FacilityAlias, )
supermod.ProductFlowUnit.subclass = ProductFlowUnitSub
# end class ProductFlowUnitSub


class QualifierSub(supermod.Qualifier):
    def __init__(self, Qualifier_member=None):
        super(QualifierSub, self).__init__(Qualifier_member, )
supermod.Qualifier.subclass = QualifierSub
# end class QualifierSub


class RelativeCoordinateSub(supermod.RelativeCoordinate):
    def __init__(self, X=None, Y=None, Z=None):
        super(RelativeCoordinateSub, self).__init__(X, Y, Z, )
supermod.RelativeCoordinate.subclass = RelativeCoordinateSub
# end class RelativeCoordinateSub


class AbstractObjectSub(supermod.AbstractObject):
    def __init__(self, objectVersion=None, schemaVersion=None, uuid=None, existenceKind=None, Aliases=None, Citation=None, CustomData=None, ExtensionNameValue=None):
        super(AbstractObjectSub, self).__init__(objectVersion, schemaVersion, uuid, existenceKind, Aliases, Citation, CustomData, ExtensionNameValue, )
supermod.AbstractObject.subclass = AbstractObjectSub
# end class AbstractObjectSub


class CitationSub(EmlMixin, supermod.Citation):
    def __init__(self, Title=None, Originator=None, Creation=None, Format=None, Editor=None, LastUpdate=None, VersionString=None, Description=None, DescriptiveKeywords=None):
        super(CitationSub, self).__init__(Title, Originator, Creation, Format, Editor, LastUpdate, VersionString, Description, DescriptiveKeywords, )
supermod.Citation.subclass = CitationSub
# end class CitationSub


class CustomDataSub(EmlMixin, supermod.CustomData):
    def __init__(self, anytypeobjs_=None):
        super(CustomDataSub, self).__init__(anytypeobjs_, )
supermod.CustomData.subclass = CustomDataSub
# end class CustomDataSub


class ExtensionNameValueSub(EmlMixin, supermod.ExtensionNameValue):
    def __init__(self, Name=None, Value=None, MeasureClass=None, DTim=None, Index=None, Description=None):
        super(ExtensionNameValueSub, self).__init__(Name, Value, MeasureClass, DTim, Index, Description, )
supermod.ExtensionNameValue.subclass = ExtensionNameValueSub
# end class ExtensionNameValueSub


class ObjectAliasSub(EmlMixin, supermod.ObjectAlias):
    def __init__(self, authority=None, Identifier=None, Description=None):
        super(ObjectAliasSub, self).__init__(authority, Identifier, Description, )
supermod.ObjectAlias.subclass = ObjectAliasSub
# end class ObjectAliasSub


class AbstractValueArraySub(supermod.AbstractValueArray):
    def __init__(self, extensiontype_=None):
        super(AbstractValueArraySub, self).__init__(extensiontype_, )
supermod.AbstractValueArray.subclass = AbstractValueArraySub
# end class AbstractValueArraySub


class AuthorityQualifiedNameSub(supermod.AuthorityQualifiedName):
    def __init__(self, authority=None, code=None, valueOf_=None):
        super(AuthorityQualifiedNameSub, self).__init__(authority, code, valueOf_, )
supermod.AuthorityQualifiedName.subclass = AuthorityQualifiedNameSub
# end class AuthorityQualifiedNameSub


class GenericMeasureSub(supermod.GenericMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(GenericMeasureSub, self).__init__(uom, valueOf_, )
supermod.GenericMeasure.subclass = GenericMeasureSub
# end class GenericMeasureSub


class JaggedArraySub(supermod.JaggedArray):
    def __init__(self, Elements=None, CumulativeLength=None):
        super(JaggedArraySub, self).__init__(Elements, CumulativeLength, )
supermod.JaggedArray.subclass = JaggedArraySub
# end class JaggedArraySub


class MdIntervalSub(supermod.MdInterval):
    def __init__(self, datum=None, MdTop=None, MdBase=None):
        super(MdIntervalSub, self).__init__(datum, MdTop, MdBase, )
supermod.MdInterval.subclass = MdIntervalSub
# end class MdIntervalSub


class StringMeasureSub(EmlMixin, supermod.StringMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(StringMeasureSub, self).__init__(uom, valueOf_, )
supermod.StringMeasure.subclass = StringMeasureSub
# end class StringMeasureSub


class TvdIntervalSub(supermod.TvdInterval):
    def __init__(self, datum=None, TvdTop=None, TvdBase=None):
        super(TvdIntervalSub, self).__init__(datum, TvdTop, TvdBase, )
supermod.TvdInterval.subclass = TvdIntervalSub
# end class TvdIntervalSub


class AbsorbedDoseMeasureSub(supermod.AbsorbedDoseMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(AbsorbedDoseMeasureSub, self).__init__(uom, valueOf_, )
supermod.AbsorbedDoseMeasure.subclass = AbsorbedDoseMeasureSub
# end class AbsorbedDoseMeasureSub


class AbsorbedDoseMeasureExtSub(supermod.AbsorbedDoseMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(AbsorbedDoseMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.AbsorbedDoseMeasureExt.subclass = AbsorbedDoseMeasureExtSub
# end class AbsorbedDoseMeasureExtSub


class ActivityOfRadioactivityMeasureSub(supermod.ActivityOfRadioactivityMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ActivityOfRadioactivityMeasureSub, self).__init__(uom, valueOf_, )
supermod.ActivityOfRadioactivityMeasure.subclass = ActivityOfRadioactivityMeasureSub
# end class ActivityOfRadioactivityMeasureSub


class ActivityOfRadioactivityMeasureExtSub(supermod.ActivityOfRadioactivityMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ActivityOfRadioactivityMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ActivityOfRadioactivityMeasureExt.subclass = ActivityOfRadioactivityMeasureExtSub
# end class ActivityOfRadioactivityMeasureExtSub


class AmountOfSubstanceMeasureSub(supermod.AmountOfSubstanceMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(AmountOfSubstanceMeasureSub, self).__init__(uom, valueOf_, )
supermod.AmountOfSubstanceMeasure.subclass = AmountOfSubstanceMeasureSub
# end class AmountOfSubstanceMeasureSub


class AmountOfSubstanceMeasureExtSub(supermod.AmountOfSubstanceMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(AmountOfSubstanceMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.AmountOfSubstanceMeasureExt.subclass = AmountOfSubstanceMeasureExtSub
# end class AmountOfSubstanceMeasureExtSub


class AmountOfSubstancePerAmountOfSubstanceMeasureSub(supermod.AmountOfSubstancePerAmountOfSubstanceMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(AmountOfSubstancePerAmountOfSubstanceMeasureSub, self).__init__(uom, valueOf_, )
supermod.AmountOfSubstancePerAmountOfSubstanceMeasure.subclass = AmountOfSubstancePerAmountOfSubstanceMeasureSub
# end class AmountOfSubstancePerAmountOfSubstanceMeasureSub


class AmountOfSubstancePerAmountOfSubstanceMeasureExtSub(supermod.AmountOfSubstancePerAmountOfSubstanceMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(AmountOfSubstancePerAmountOfSubstanceMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.AmountOfSubstancePerAmountOfSubstanceMeasureExt.subclass = AmountOfSubstancePerAmountOfSubstanceMeasureExtSub
# end class AmountOfSubstancePerAmountOfSubstanceMeasureExtSub


class AmountOfSubstancePerAreaMeasureSub(supermod.AmountOfSubstancePerAreaMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(AmountOfSubstancePerAreaMeasureSub, self).__init__(uom, valueOf_, )
supermod.AmountOfSubstancePerAreaMeasure.subclass = AmountOfSubstancePerAreaMeasureSub
# end class AmountOfSubstancePerAreaMeasureSub


class AmountOfSubstancePerAreaMeasureExtSub(supermod.AmountOfSubstancePerAreaMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(AmountOfSubstancePerAreaMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.AmountOfSubstancePerAreaMeasureExt.subclass = AmountOfSubstancePerAreaMeasureExtSub
# end class AmountOfSubstancePerAreaMeasureExtSub


class AmountOfSubstancePerTimeMeasureSub(supermod.AmountOfSubstancePerTimeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(AmountOfSubstancePerTimeMeasureSub, self).__init__(uom, valueOf_, )
supermod.AmountOfSubstancePerTimeMeasure.subclass = AmountOfSubstancePerTimeMeasureSub
# end class AmountOfSubstancePerTimeMeasureSub


class AmountOfSubstancePerTimeMeasureExtSub(supermod.AmountOfSubstancePerTimeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(AmountOfSubstancePerTimeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.AmountOfSubstancePerTimeMeasureExt.subclass = AmountOfSubstancePerTimeMeasureExtSub
# end class AmountOfSubstancePerTimeMeasureExtSub


class AmountOfSubstancePerTimePerAreaMeasureSub(supermod.AmountOfSubstancePerTimePerAreaMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(AmountOfSubstancePerTimePerAreaMeasureSub, self).__init__(uom, valueOf_, )
supermod.AmountOfSubstancePerTimePerAreaMeasure.subclass = AmountOfSubstancePerTimePerAreaMeasureSub
# end class AmountOfSubstancePerTimePerAreaMeasureSub


class AmountOfSubstancePerTimePerAreaMeasureExtSub(supermod.AmountOfSubstancePerTimePerAreaMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(AmountOfSubstancePerTimePerAreaMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.AmountOfSubstancePerTimePerAreaMeasureExt.subclass = AmountOfSubstancePerTimePerAreaMeasureExtSub
# end class AmountOfSubstancePerTimePerAreaMeasureExtSub


class AmountOfSubstancePerVolumeMeasureSub(supermod.AmountOfSubstancePerVolumeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(AmountOfSubstancePerVolumeMeasureSub, self).__init__(uom, valueOf_, )
supermod.AmountOfSubstancePerVolumeMeasure.subclass = AmountOfSubstancePerVolumeMeasureSub
# end class AmountOfSubstancePerVolumeMeasureSub


class AmountOfSubstancePerVolumeMeasureExtSub(supermod.AmountOfSubstancePerVolumeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(AmountOfSubstancePerVolumeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.AmountOfSubstancePerVolumeMeasureExt.subclass = AmountOfSubstancePerVolumeMeasureExtSub
# end class AmountOfSubstancePerVolumeMeasureExtSub


class AnglePerLengthMeasureSub(supermod.AnglePerLengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(AnglePerLengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.AnglePerLengthMeasure.subclass = AnglePerLengthMeasureSub
# end class AnglePerLengthMeasureSub


class AnglePerLengthMeasureExtSub(supermod.AnglePerLengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(AnglePerLengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.AnglePerLengthMeasureExt.subclass = AnglePerLengthMeasureExtSub
# end class AnglePerLengthMeasureExtSub


class AnglePerVolumeMeasureSub(supermod.AnglePerVolumeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(AnglePerVolumeMeasureSub, self).__init__(uom, valueOf_, )
supermod.AnglePerVolumeMeasure.subclass = AnglePerVolumeMeasureSub
# end class AnglePerVolumeMeasureSub


class AnglePerVolumeMeasureExtSub(supermod.AnglePerVolumeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(AnglePerVolumeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.AnglePerVolumeMeasureExt.subclass = AnglePerVolumeMeasureExtSub
# end class AnglePerVolumeMeasureExtSub


class AngularAccelerationMeasureSub(supermod.AngularAccelerationMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(AngularAccelerationMeasureSub, self).__init__(uom, valueOf_, )
supermod.AngularAccelerationMeasure.subclass = AngularAccelerationMeasureSub
# end class AngularAccelerationMeasureSub


class AngularAccelerationMeasureExtSub(supermod.AngularAccelerationMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(AngularAccelerationMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.AngularAccelerationMeasureExt.subclass = AngularAccelerationMeasureExtSub
# end class AngularAccelerationMeasureExtSub


class AngularVelocityMeasureSub(supermod.AngularVelocityMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(AngularVelocityMeasureSub, self).__init__(uom, valueOf_, )
supermod.AngularVelocityMeasure.subclass = AngularVelocityMeasureSub
# end class AngularVelocityMeasureSub


class AngularVelocityMeasureExtSub(supermod.AngularVelocityMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(AngularVelocityMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.AngularVelocityMeasureExt.subclass = AngularVelocityMeasureExtSub
# end class AngularVelocityMeasureExtSub


class APIGammaRayMeasureSub(supermod.APIGammaRayMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(APIGammaRayMeasureSub, self).__init__(uom, valueOf_, )
supermod.APIGammaRayMeasure.subclass = APIGammaRayMeasureSub
# end class APIGammaRayMeasureSub


class APIGammaRayMeasureExtSub(supermod.APIGammaRayMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(APIGammaRayMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.APIGammaRayMeasureExt.subclass = APIGammaRayMeasureExtSub
# end class APIGammaRayMeasureExtSub


class APIGravityMeasureSub(supermod.APIGravityMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(APIGravityMeasureSub, self).__init__(uom, valueOf_, )
supermod.APIGravityMeasure.subclass = APIGravityMeasureSub
# end class APIGravityMeasureSub


class APIGravityMeasureExtSub(supermod.APIGravityMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(APIGravityMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.APIGravityMeasureExt.subclass = APIGravityMeasureExtSub
# end class APIGravityMeasureExtSub


class APINeutronMeasureSub(supermod.APINeutronMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(APINeutronMeasureSub, self).__init__(uom, valueOf_, )
supermod.APINeutronMeasure.subclass = APINeutronMeasureSub
# end class APINeutronMeasureSub


class APINeutronMeasureExtSub(supermod.APINeutronMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(APINeutronMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.APINeutronMeasureExt.subclass = APINeutronMeasureExtSub
# end class APINeutronMeasureExtSub


class AreaMeasureSub(supermod.AreaMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(AreaMeasureSub, self).__init__(uom, valueOf_, )
supermod.AreaMeasure.subclass = AreaMeasureSub
# end class AreaMeasureSub


class AreaMeasureExtSub(supermod.AreaMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(AreaMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.AreaMeasureExt.subclass = AreaMeasureExtSub
# end class AreaMeasureExtSub


class AreaPerAmountOfSubstanceMeasureSub(supermod.AreaPerAmountOfSubstanceMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(AreaPerAmountOfSubstanceMeasureSub, self).__init__(uom, valueOf_, )
supermod.AreaPerAmountOfSubstanceMeasure.subclass = AreaPerAmountOfSubstanceMeasureSub
# end class AreaPerAmountOfSubstanceMeasureSub


class AreaPerAmountOfSubstanceMeasureExtSub(supermod.AreaPerAmountOfSubstanceMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(AreaPerAmountOfSubstanceMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.AreaPerAmountOfSubstanceMeasureExt.subclass = AreaPerAmountOfSubstanceMeasureExtSub
# end class AreaPerAmountOfSubstanceMeasureExtSub


class AreaPerAreaMeasureSub(supermod.AreaPerAreaMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(AreaPerAreaMeasureSub, self).__init__(uom, valueOf_, )
supermod.AreaPerAreaMeasure.subclass = AreaPerAreaMeasureSub
# end class AreaPerAreaMeasureSub


class AreaPerAreaMeasureExtSub(supermod.AreaPerAreaMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(AreaPerAreaMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.AreaPerAreaMeasureExt.subclass = AreaPerAreaMeasureExtSub
# end class AreaPerAreaMeasureExtSub


class AreaPerCountMeasureSub(supermod.AreaPerCountMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(AreaPerCountMeasureSub, self).__init__(uom, valueOf_, )
supermod.AreaPerCountMeasure.subclass = AreaPerCountMeasureSub
# end class AreaPerCountMeasureSub


class AreaPerCountMeasureExtSub(supermod.AreaPerCountMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(AreaPerCountMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.AreaPerCountMeasureExt.subclass = AreaPerCountMeasureExtSub
# end class AreaPerCountMeasureExtSub


class AreaPerMassMeasureSub(supermod.AreaPerMassMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(AreaPerMassMeasureSub, self).__init__(uom, valueOf_, )
supermod.AreaPerMassMeasure.subclass = AreaPerMassMeasureSub
# end class AreaPerMassMeasureSub


class AreaPerMassMeasureExtSub(supermod.AreaPerMassMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(AreaPerMassMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.AreaPerMassMeasureExt.subclass = AreaPerMassMeasureExtSub
# end class AreaPerMassMeasureExtSub


class AreaPerTimeMeasureSub(supermod.AreaPerTimeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(AreaPerTimeMeasureSub, self).__init__(uom, valueOf_, )
supermod.AreaPerTimeMeasure.subclass = AreaPerTimeMeasureSub
# end class AreaPerTimeMeasureSub


class AreaPerTimeMeasureExtSub(supermod.AreaPerTimeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(AreaPerTimeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.AreaPerTimeMeasureExt.subclass = AreaPerTimeMeasureExtSub
# end class AreaPerTimeMeasureExtSub


class AreaPerVolumeMeasureSub(supermod.AreaPerVolumeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(AreaPerVolumeMeasureSub, self).__init__(uom, valueOf_, )
supermod.AreaPerVolumeMeasure.subclass = AreaPerVolumeMeasureSub
# end class AreaPerVolumeMeasureSub


class AreaPerVolumeMeasureExtSub(supermod.AreaPerVolumeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(AreaPerVolumeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.AreaPerVolumeMeasureExt.subclass = AreaPerVolumeMeasureExtSub
# end class AreaPerVolumeMeasureExtSub


class AttenuationPerFrequencyIntervalMeasureSub(supermod.AttenuationPerFrequencyIntervalMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(AttenuationPerFrequencyIntervalMeasureSub, self).__init__(uom, valueOf_, )
supermod.AttenuationPerFrequencyIntervalMeasure.subclass = AttenuationPerFrequencyIntervalMeasureSub
# end class AttenuationPerFrequencyIntervalMeasureSub


class AttenuationPerFrequencyIntervalMeasureExtSub(supermod.AttenuationPerFrequencyIntervalMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(AttenuationPerFrequencyIntervalMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.AttenuationPerFrequencyIntervalMeasureExt.subclass = AttenuationPerFrequencyIntervalMeasureExtSub
# end class AttenuationPerFrequencyIntervalMeasureExtSub


class CapacitanceMeasureSub(supermod.CapacitanceMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(CapacitanceMeasureSub, self).__init__(uom, valueOf_, )
supermod.CapacitanceMeasure.subclass = CapacitanceMeasureSub
# end class CapacitanceMeasureSub


class CapacitanceMeasureExtSub(supermod.CapacitanceMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(CapacitanceMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.CapacitanceMeasureExt.subclass = CapacitanceMeasureExtSub
# end class CapacitanceMeasureExtSub


class CationExchangeCapacityMeasureSub(supermod.CationExchangeCapacityMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(CationExchangeCapacityMeasureSub, self).__init__(uom, valueOf_, )
supermod.CationExchangeCapacityMeasure.subclass = CationExchangeCapacityMeasureSub
# end class CationExchangeCapacityMeasureSub


class CationExchangeCapacityMeasureExtSub(supermod.CationExchangeCapacityMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(CationExchangeCapacityMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.CationExchangeCapacityMeasureExt.subclass = CationExchangeCapacityMeasureExtSub
# end class CationExchangeCapacityMeasureExtSub


class DataTransferSpeedMeasureSub(supermod.DataTransferSpeedMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(DataTransferSpeedMeasureSub, self).__init__(uom, valueOf_, )
supermod.DataTransferSpeedMeasure.subclass = DataTransferSpeedMeasureSub
# end class DataTransferSpeedMeasureSub


class DataTransferSpeedMeasureExtSub(supermod.DataTransferSpeedMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(DataTransferSpeedMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.DataTransferSpeedMeasureExt.subclass = DataTransferSpeedMeasureExtSub
# end class DataTransferSpeedMeasureExtSub


class DiffusionCoefficientMeasureSub(supermod.DiffusionCoefficientMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(DiffusionCoefficientMeasureSub, self).__init__(uom, valueOf_, )
supermod.DiffusionCoefficientMeasure.subclass = DiffusionCoefficientMeasureSub
# end class DiffusionCoefficientMeasureSub


class DiffusionCoefficientMeasureExtSub(supermod.DiffusionCoefficientMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(DiffusionCoefficientMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.DiffusionCoefficientMeasureExt.subclass = DiffusionCoefficientMeasureExtSub
# end class DiffusionCoefficientMeasureExtSub


class DiffusiveTimeOfFlightMeasureSub(supermod.DiffusiveTimeOfFlightMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(DiffusiveTimeOfFlightMeasureSub, self).__init__(uom, valueOf_, )
supermod.DiffusiveTimeOfFlightMeasure.subclass = DiffusiveTimeOfFlightMeasureSub
# end class DiffusiveTimeOfFlightMeasureSub


class DiffusiveTimeOfFlightMeasureExtSub(supermod.DiffusiveTimeOfFlightMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(DiffusiveTimeOfFlightMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.DiffusiveTimeOfFlightMeasureExt.subclass = DiffusiveTimeOfFlightMeasureExtSub
# end class DiffusiveTimeOfFlightMeasureExtSub


class DigitalStorageMeasureSub(supermod.DigitalStorageMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(DigitalStorageMeasureSub, self).__init__(uom, valueOf_, )
supermod.DigitalStorageMeasure.subclass = DigitalStorageMeasureSub
# end class DigitalStorageMeasureSub


class DigitalStorageMeasureExtSub(supermod.DigitalStorageMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(DigitalStorageMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.DigitalStorageMeasureExt.subclass = DigitalStorageMeasureExtSub
# end class DigitalStorageMeasureExtSub


class DimensionlessMeasureSub(supermod.DimensionlessMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(DimensionlessMeasureSub, self).__init__(uom, valueOf_, )
supermod.DimensionlessMeasure.subclass = DimensionlessMeasureSub
# end class DimensionlessMeasureSub


class DimensionlessMeasureExtSub(supermod.DimensionlessMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(DimensionlessMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.DimensionlessMeasureExt.subclass = DimensionlessMeasureExtSub
# end class DimensionlessMeasureExtSub


class DipoleMomentMeasureSub(supermod.DipoleMomentMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(DipoleMomentMeasureSub, self).__init__(uom, valueOf_, )
supermod.DipoleMomentMeasure.subclass = DipoleMomentMeasureSub
# end class DipoleMomentMeasureSub


class DipoleMomentMeasureExtSub(supermod.DipoleMomentMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(DipoleMomentMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.DipoleMomentMeasureExt.subclass = DipoleMomentMeasureExtSub
# end class DipoleMomentMeasureExtSub


class DoseEquivalentMeasureSub(supermod.DoseEquivalentMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(DoseEquivalentMeasureSub, self).__init__(uom, valueOf_, )
supermod.DoseEquivalentMeasure.subclass = DoseEquivalentMeasureSub
# end class DoseEquivalentMeasureSub


class DoseEquivalentMeasureExtSub(supermod.DoseEquivalentMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(DoseEquivalentMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.DoseEquivalentMeasureExt.subclass = DoseEquivalentMeasureExtSub
# end class DoseEquivalentMeasureExtSub


class DynamicViscosityMeasureSub(supermod.DynamicViscosityMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(DynamicViscosityMeasureSub, self).__init__(uom, valueOf_, )
supermod.DynamicViscosityMeasure.subclass = DynamicViscosityMeasureSub
# end class DynamicViscosityMeasureSub


class DynamicViscosityMeasureExtSub(supermod.DynamicViscosityMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(DynamicViscosityMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.DynamicViscosityMeasureExt.subclass = DynamicViscosityMeasureExtSub
# end class DynamicViscosityMeasureExtSub


class ElectricalResistivityMeasureSub(supermod.ElectricalResistivityMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricalResistivityMeasureSub, self).__init__(uom, valueOf_, )
supermod.ElectricalResistivityMeasure.subclass = ElectricalResistivityMeasureSub
# end class ElectricalResistivityMeasureSub


class ElectricalResistivityMeasureExtSub(supermod.ElectricalResistivityMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricalResistivityMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ElectricalResistivityMeasureExt.subclass = ElectricalResistivityMeasureExtSub
# end class ElectricalResistivityMeasureExtSub


class ElectricChargeMeasureSub(supermod.ElectricChargeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricChargeMeasureSub, self).__init__(uom, valueOf_, )
supermod.ElectricChargeMeasure.subclass = ElectricChargeMeasureSub
# end class ElectricChargeMeasureSub


class ElectricChargeMeasureExtSub(supermod.ElectricChargeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricChargeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ElectricChargeMeasureExt.subclass = ElectricChargeMeasureExtSub
# end class ElectricChargeMeasureExtSub


class ElectricChargePerAreaMeasureSub(supermod.ElectricChargePerAreaMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricChargePerAreaMeasureSub, self).__init__(uom, valueOf_, )
supermod.ElectricChargePerAreaMeasure.subclass = ElectricChargePerAreaMeasureSub
# end class ElectricChargePerAreaMeasureSub


class ElectricChargePerAreaMeasureExtSub(supermod.ElectricChargePerAreaMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricChargePerAreaMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ElectricChargePerAreaMeasureExt.subclass = ElectricChargePerAreaMeasureExtSub
# end class ElectricChargePerAreaMeasureExtSub


class ElectricChargePerMassMeasureSub(supermod.ElectricChargePerMassMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricChargePerMassMeasureSub, self).__init__(uom, valueOf_, )
supermod.ElectricChargePerMassMeasure.subclass = ElectricChargePerMassMeasureSub
# end class ElectricChargePerMassMeasureSub


class ElectricChargePerMassMeasureExtSub(supermod.ElectricChargePerMassMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricChargePerMassMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ElectricChargePerMassMeasureExt.subclass = ElectricChargePerMassMeasureExtSub
# end class ElectricChargePerMassMeasureExtSub


class ElectricChargePerVolumeMeasureSub(supermod.ElectricChargePerVolumeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricChargePerVolumeMeasureSub, self).__init__(uom, valueOf_, )
supermod.ElectricChargePerVolumeMeasure.subclass = ElectricChargePerVolumeMeasureSub
# end class ElectricChargePerVolumeMeasureSub


class ElectricChargePerVolumeMeasureExtSub(supermod.ElectricChargePerVolumeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricChargePerVolumeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ElectricChargePerVolumeMeasureExt.subclass = ElectricChargePerVolumeMeasureExtSub
# end class ElectricChargePerVolumeMeasureExtSub


class ElectricConductanceMeasureSub(supermod.ElectricConductanceMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricConductanceMeasureSub, self).__init__(uom, valueOf_, )
supermod.ElectricConductanceMeasure.subclass = ElectricConductanceMeasureSub
# end class ElectricConductanceMeasureSub


class ElectricConductanceMeasureExtSub(supermod.ElectricConductanceMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricConductanceMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ElectricConductanceMeasureExt.subclass = ElectricConductanceMeasureExtSub
# end class ElectricConductanceMeasureExtSub


class ElectricConductivityMeasureSub(supermod.ElectricConductivityMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricConductivityMeasureSub, self).__init__(uom, valueOf_, )
supermod.ElectricConductivityMeasure.subclass = ElectricConductivityMeasureSub
# end class ElectricConductivityMeasureSub


class ElectricConductivityMeasureExtSub(supermod.ElectricConductivityMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricConductivityMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ElectricConductivityMeasureExt.subclass = ElectricConductivityMeasureExtSub
# end class ElectricConductivityMeasureExtSub


class ElectricCurrentDensityMeasureSub(supermod.ElectricCurrentDensityMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricCurrentDensityMeasureSub, self).__init__(uom, valueOf_, )
supermod.ElectricCurrentDensityMeasure.subclass = ElectricCurrentDensityMeasureSub
# end class ElectricCurrentDensityMeasureSub


class ElectricCurrentDensityMeasureExtSub(supermod.ElectricCurrentDensityMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricCurrentDensityMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ElectricCurrentDensityMeasureExt.subclass = ElectricCurrentDensityMeasureExtSub
# end class ElectricCurrentDensityMeasureExtSub


class ElectricCurrentMeasureSub(supermod.ElectricCurrentMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricCurrentMeasureSub, self).__init__(uom, valueOf_, )
supermod.ElectricCurrentMeasure.subclass = ElectricCurrentMeasureSub
# end class ElectricCurrentMeasureSub


class ElectricCurrentMeasureExtSub(supermod.ElectricCurrentMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricCurrentMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ElectricCurrentMeasureExt.subclass = ElectricCurrentMeasureExtSub
# end class ElectricCurrentMeasureExtSub


class ElectricFieldStrengthMeasureSub(supermod.ElectricFieldStrengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricFieldStrengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.ElectricFieldStrengthMeasure.subclass = ElectricFieldStrengthMeasureSub
# end class ElectricFieldStrengthMeasureSub


class ElectricFieldStrengthMeasureExtSub(supermod.ElectricFieldStrengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricFieldStrengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ElectricFieldStrengthMeasureExt.subclass = ElectricFieldStrengthMeasureExtSub
# end class ElectricFieldStrengthMeasureExtSub


class ElectricPotentialDifferenceMeasureSub(supermod.ElectricPotentialDifferenceMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricPotentialDifferenceMeasureSub, self).__init__(uom, valueOf_, )
supermod.ElectricPotentialDifferenceMeasure.subclass = ElectricPotentialDifferenceMeasureSub
# end class ElectricPotentialDifferenceMeasureSub


class ElectricPotentialDifferenceMeasureExtSub(supermod.ElectricPotentialDifferenceMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricPotentialDifferenceMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ElectricPotentialDifferenceMeasureExt.subclass = ElectricPotentialDifferenceMeasureExtSub
# end class ElectricPotentialDifferenceMeasureExtSub


class ElectricResistanceMeasureSub(supermod.ElectricResistanceMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricResistanceMeasureSub, self).__init__(uom, valueOf_, )
supermod.ElectricResistanceMeasure.subclass = ElectricResistanceMeasureSub
# end class ElectricResistanceMeasureSub


class ElectricResistanceMeasureExtSub(supermod.ElectricResistanceMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricResistanceMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ElectricResistanceMeasureExt.subclass = ElectricResistanceMeasureExtSub
# end class ElectricResistanceMeasureExtSub


class ElectricResistancePerLengthMeasureSub(supermod.ElectricResistancePerLengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricResistancePerLengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.ElectricResistancePerLengthMeasure.subclass = ElectricResistancePerLengthMeasureSub
# end class ElectricResistancePerLengthMeasureSub


class ElectricResistancePerLengthMeasureExtSub(supermod.ElectricResistancePerLengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectricResistancePerLengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ElectricResistancePerLengthMeasureExt.subclass = ElectricResistancePerLengthMeasureExtSub
# end class ElectricResistancePerLengthMeasureExtSub


class ElectromagneticMomentMeasureSub(supermod.ElectromagneticMomentMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectromagneticMomentMeasureSub, self).__init__(uom, valueOf_, )
supermod.ElectromagneticMomentMeasure.subclass = ElectromagneticMomentMeasureSub
# end class ElectromagneticMomentMeasureSub


class ElectromagneticMomentMeasureExtSub(supermod.ElectromagneticMomentMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ElectromagneticMomentMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ElectromagneticMomentMeasureExt.subclass = ElectromagneticMomentMeasureExtSub
# end class ElectromagneticMomentMeasureExtSub


class EnergyLengthPerAreaMeasureSub(supermod.EnergyLengthPerAreaMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(EnergyLengthPerAreaMeasureSub, self).__init__(uom, valueOf_, )
supermod.EnergyLengthPerAreaMeasure.subclass = EnergyLengthPerAreaMeasureSub
# end class EnergyLengthPerAreaMeasureSub


class EnergyLengthPerAreaMeasureExtSub(supermod.EnergyLengthPerAreaMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(EnergyLengthPerAreaMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.EnergyLengthPerAreaMeasureExt.subclass = EnergyLengthPerAreaMeasureExtSub
# end class EnergyLengthPerAreaMeasureExtSub


class EnergyLengthPerTimeAreaTemperatureMeasureSub(supermod.EnergyLengthPerTimeAreaTemperatureMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(EnergyLengthPerTimeAreaTemperatureMeasureSub, self).__init__(uom, valueOf_, )
supermod.EnergyLengthPerTimeAreaTemperatureMeasure.subclass = EnergyLengthPerTimeAreaTemperatureMeasureSub
# end class EnergyLengthPerTimeAreaTemperatureMeasureSub


class EnergyLengthPerTimeAreaTemperatureMeasureExtSub(supermod.EnergyLengthPerTimeAreaTemperatureMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(EnergyLengthPerTimeAreaTemperatureMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.EnergyLengthPerTimeAreaTemperatureMeasureExt.subclass = EnergyLengthPerTimeAreaTemperatureMeasureExtSub
# end class EnergyLengthPerTimeAreaTemperatureMeasureExtSub


class EnergyMeasureSub(supermod.EnergyMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(EnergyMeasureSub, self).__init__(uom, valueOf_, )
supermod.EnergyMeasure.subclass = EnergyMeasureSub
# end class EnergyMeasureSub


class EnergyMeasureExtSub(supermod.EnergyMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(EnergyMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.EnergyMeasureExt.subclass = EnergyMeasureExtSub
# end class EnergyMeasureExtSub


class EnergyPerAreaMeasureSub(supermod.EnergyPerAreaMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(EnergyPerAreaMeasureSub, self).__init__(uom, valueOf_, )
supermod.EnergyPerAreaMeasure.subclass = EnergyPerAreaMeasureSub
# end class EnergyPerAreaMeasureSub


class EnergyPerAreaMeasureExtSub(supermod.EnergyPerAreaMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(EnergyPerAreaMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.EnergyPerAreaMeasureExt.subclass = EnergyPerAreaMeasureExtSub
# end class EnergyPerAreaMeasureExtSub


class EnergyPerLengthMeasureSub(supermod.EnergyPerLengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(EnergyPerLengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.EnergyPerLengthMeasure.subclass = EnergyPerLengthMeasureSub
# end class EnergyPerLengthMeasureSub


class EnergyPerLengthMeasureExtSub(supermod.EnergyPerLengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(EnergyPerLengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.EnergyPerLengthMeasureExt.subclass = EnergyPerLengthMeasureExtSub
# end class EnergyPerLengthMeasureExtSub


class EnergyPerMassMeasureSub(supermod.EnergyPerMassMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(EnergyPerMassMeasureSub, self).__init__(uom, valueOf_, )
supermod.EnergyPerMassMeasure.subclass = EnergyPerMassMeasureSub
# end class EnergyPerMassMeasureSub


class EnergyPerMassMeasureExtSub(supermod.EnergyPerMassMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(EnergyPerMassMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.EnergyPerMassMeasureExt.subclass = EnergyPerMassMeasureExtSub
# end class EnergyPerMassMeasureExtSub


class EnergyPerMassPerTimeMeasureSub(supermod.EnergyPerMassPerTimeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(EnergyPerMassPerTimeMeasureSub, self).__init__(uom, valueOf_, )
supermod.EnergyPerMassPerTimeMeasure.subclass = EnergyPerMassPerTimeMeasureSub
# end class EnergyPerMassPerTimeMeasureSub


class EnergyPerMassPerTimeMeasureExtSub(supermod.EnergyPerMassPerTimeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(EnergyPerMassPerTimeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.EnergyPerMassPerTimeMeasureExt.subclass = EnergyPerMassPerTimeMeasureExtSub
# end class EnergyPerMassPerTimeMeasureExtSub


class EnergyPerVolumeMeasureSub(supermod.EnergyPerVolumeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(EnergyPerVolumeMeasureSub, self).__init__(uom, valueOf_, )
supermod.EnergyPerVolumeMeasure.subclass = EnergyPerVolumeMeasureSub
# end class EnergyPerVolumeMeasureSub


class EnergyPerVolumeMeasureExtSub(supermod.EnergyPerVolumeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(EnergyPerVolumeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.EnergyPerVolumeMeasureExt.subclass = EnergyPerVolumeMeasureExtSub
# end class EnergyPerVolumeMeasureExtSub


class ForceAreaMeasureSub(supermod.ForceAreaMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ForceAreaMeasureSub, self).__init__(uom, valueOf_, )
supermod.ForceAreaMeasure.subclass = ForceAreaMeasureSub
# end class ForceAreaMeasureSub


class ForceAreaMeasureExtSub(supermod.ForceAreaMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ForceAreaMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ForceAreaMeasureExt.subclass = ForceAreaMeasureExtSub
# end class ForceAreaMeasureExtSub


class ForceLengthPerLengthMeasureSub(supermod.ForceLengthPerLengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ForceLengthPerLengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.ForceLengthPerLengthMeasure.subclass = ForceLengthPerLengthMeasureSub
# end class ForceLengthPerLengthMeasureSub


class ForceLengthPerLengthMeasureExtSub(supermod.ForceLengthPerLengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ForceLengthPerLengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ForceLengthPerLengthMeasureExt.subclass = ForceLengthPerLengthMeasureExtSub
# end class ForceLengthPerLengthMeasureExtSub


class ForceMeasureSub(supermod.ForceMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ForceMeasureSub, self).__init__(uom, valueOf_, )
supermod.ForceMeasure.subclass = ForceMeasureSub
# end class ForceMeasureSub


class ForceMeasureExtSub(supermod.ForceMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ForceMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ForceMeasureExt.subclass = ForceMeasureExtSub
# end class ForceMeasureExtSub


class ForcePerForceMeasureSub(supermod.ForcePerForceMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ForcePerForceMeasureSub, self).__init__(uom, valueOf_, )
supermod.ForcePerForceMeasure.subclass = ForcePerForceMeasureSub
# end class ForcePerForceMeasureSub


class ForcePerForceMeasureExtSub(supermod.ForcePerForceMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ForcePerForceMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ForcePerForceMeasureExt.subclass = ForcePerForceMeasureExtSub
# end class ForcePerForceMeasureExtSub


class ForcePerLengthMeasureSub(supermod.ForcePerLengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ForcePerLengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.ForcePerLengthMeasure.subclass = ForcePerLengthMeasureSub
# end class ForcePerLengthMeasureSub


class ForcePerLengthMeasureExtSub(supermod.ForcePerLengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ForcePerLengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ForcePerLengthMeasureExt.subclass = ForcePerLengthMeasureExtSub
# end class ForcePerLengthMeasureExtSub


class ForcePerVolumeMeasureSub(supermod.ForcePerVolumeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ForcePerVolumeMeasureSub, self).__init__(uom, valueOf_, )
supermod.ForcePerVolumeMeasure.subclass = ForcePerVolumeMeasureSub
# end class ForcePerVolumeMeasureSub


class ForcePerVolumeMeasureExtSub(supermod.ForcePerVolumeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ForcePerVolumeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ForcePerVolumeMeasureExt.subclass = ForcePerVolumeMeasureExtSub
# end class ForcePerVolumeMeasureExtSub


class FrequencyIntervalMeasureSub(supermod.FrequencyIntervalMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(FrequencyIntervalMeasureSub, self).__init__(uom, valueOf_, )
supermod.FrequencyIntervalMeasure.subclass = FrequencyIntervalMeasureSub
# end class FrequencyIntervalMeasureSub


class FrequencyIntervalMeasureExtSub(supermod.FrequencyIntervalMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(FrequencyIntervalMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.FrequencyIntervalMeasureExt.subclass = FrequencyIntervalMeasureExtSub
# end class FrequencyIntervalMeasureExtSub


class FrequencyMeasureSub(supermod.FrequencyMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(FrequencyMeasureSub, self).__init__(uom, valueOf_, )
supermod.FrequencyMeasure.subclass = FrequencyMeasureSub
# end class FrequencyMeasureSub


class FrequencyMeasureExtSub(supermod.FrequencyMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(FrequencyMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.FrequencyMeasureExt.subclass = FrequencyMeasureExtSub
# end class FrequencyMeasureExtSub


class HeatCapacityMeasureSub(supermod.HeatCapacityMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(HeatCapacityMeasureSub, self).__init__(uom, valueOf_, )
supermod.HeatCapacityMeasure.subclass = HeatCapacityMeasureSub
# end class HeatCapacityMeasureSub


class HeatCapacityMeasureExtSub(supermod.HeatCapacityMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(HeatCapacityMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.HeatCapacityMeasureExt.subclass = HeatCapacityMeasureExtSub
# end class HeatCapacityMeasureExtSub


class HeatFlowRateMeasureSub(supermod.HeatFlowRateMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(HeatFlowRateMeasureSub, self).__init__(uom, valueOf_, )
supermod.HeatFlowRateMeasure.subclass = HeatFlowRateMeasureSub
# end class HeatFlowRateMeasureSub


class HeatFlowRateMeasureExtSub(supermod.HeatFlowRateMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(HeatFlowRateMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.HeatFlowRateMeasureExt.subclass = HeatFlowRateMeasureExtSub
# end class HeatFlowRateMeasureExtSub


class HeatTransferCoefficientMeasureSub(supermod.HeatTransferCoefficientMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(HeatTransferCoefficientMeasureSub, self).__init__(uom, valueOf_, )
supermod.HeatTransferCoefficientMeasure.subclass = HeatTransferCoefficientMeasureSub
# end class HeatTransferCoefficientMeasureSub


class HeatTransferCoefficientMeasureExtSub(supermod.HeatTransferCoefficientMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(HeatTransferCoefficientMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.HeatTransferCoefficientMeasureExt.subclass = HeatTransferCoefficientMeasureExtSub
# end class HeatTransferCoefficientMeasureExtSub


class IlluminanceMeasureSub(supermod.IlluminanceMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(IlluminanceMeasureSub, self).__init__(uom, valueOf_, )
supermod.IlluminanceMeasure.subclass = IlluminanceMeasureSub
# end class IlluminanceMeasureSub


class IlluminanceMeasureExtSub(supermod.IlluminanceMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(IlluminanceMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.IlluminanceMeasureExt.subclass = IlluminanceMeasureExtSub
# end class IlluminanceMeasureExtSub


class InductanceMeasureSub(supermod.InductanceMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(InductanceMeasureSub, self).__init__(uom, valueOf_, )
supermod.InductanceMeasure.subclass = InductanceMeasureSub
# end class InductanceMeasureSub


class InductanceMeasureExtSub(supermod.InductanceMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(InductanceMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.InductanceMeasureExt.subclass = InductanceMeasureExtSub
# end class InductanceMeasureExtSub


class IsothermalCompressibilityMeasureSub(supermod.IsothermalCompressibilityMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(IsothermalCompressibilityMeasureSub, self).__init__(uom, valueOf_, )
supermod.IsothermalCompressibilityMeasure.subclass = IsothermalCompressibilityMeasureSub
# end class IsothermalCompressibilityMeasureSub


class IsothermalCompressibilityMeasureExtSub(supermod.IsothermalCompressibilityMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(IsothermalCompressibilityMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.IsothermalCompressibilityMeasureExt.subclass = IsothermalCompressibilityMeasureExtSub
# end class IsothermalCompressibilityMeasureExtSub


class KinematicViscosityMeasureSub(supermod.KinematicViscosityMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(KinematicViscosityMeasureSub, self).__init__(uom, valueOf_, )
supermod.KinematicViscosityMeasure.subclass = KinematicViscosityMeasureSub
# end class KinematicViscosityMeasureSub


class KinematicViscosityMeasureExtSub(supermod.KinematicViscosityMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(KinematicViscosityMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.KinematicViscosityMeasureExt.subclass = KinematicViscosityMeasureExtSub
# end class KinematicViscosityMeasureExtSub


class LengthMeasureSub(supermod.LengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(LengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.LengthMeasure.subclass = LengthMeasureSub
# end class LengthMeasureSub


class LengthMeasureExtSub(supermod.LengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(LengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.LengthMeasureExt.subclass = LengthMeasureExtSub
# end class LengthMeasureExtSub


class LengthPerLengthMeasureSub(supermod.LengthPerLengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(LengthPerLengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.LengthPerLengthMeasure.subclass = LengthPerLengthMeasureSub
# end class LengthPerLengthMeasureSub


class LengthPerLengthMeasureExtSub(supermod.LengthPerLengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(LengthPerLengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.LengthPerLengthMeasureExt.subclass = LengthPerLengthMeasureExtSub
# end class LengthPerLengthMeasureExtSub


class LengthPerMassMeasureSub(supermod.LengthPerMassMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(LengthPerMassMeasureSub, self).__init__(uom, valueOf_, )
supermod.LengthPerMassMeasure.subclass = LengthPerMassMeasureSub
# end class LengthPerMassMeasureSub


class LengthPerMassMeasureExtSub(supermod.LengthPerMassMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(LengthPerMassMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.LengthPerMassMeasureExt.subclass = LengthPerMassMeasureExtSub
# end class LengthPerMassMeasureExtSub


class LengthPerPressureMeasureSub(supermod.LengthPerPressureMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(LengthPerPressureMeasureSub, self).__init__(uom, valueOf_, )
supermod.LengthPerPressureMeasure.subclass = LengthPerPressureMeasureSub
# end class LengthPerPressureMeasureSub


class LengthPerPressureMeasureExtSub(supermod.LengthPerPressureMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(LengthPerPressureMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.LengthPerPressureMeasureExt.subclass = LengthPerPressureMeasureExtSub
# end class LengthPerPressureMeasureExtSub


class LengthPerTemperatureMeasureSub(supermod.LengthPerTemperatureMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(LengthPerTemperatureMeasureSub, self).__init__(uom, valueOf_, )
supermod.LengthPerTemperatureMeasure.subclass = LengthPerTemperatureMeasureSub
# end class LengthPerTemperatureMeasureSub


class LengthPerTemperatureMeasureExtSub(supermod.LengthPerTemperatureMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(LengthPerTemperatureMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.LengthPerTemperatureMeasureExt.subclass = LengthPerTemperatureMeasureExtSub
# end class LengthPerTemperatureMeasureExtSub


class LengthPerTimeMeasureSub(supermod.LengthPerTimeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(LengthPerTimeMeasureSub, self).__init__(uom, valueOf_, )
supermod.LengthPerTimeMeasure.subclass = LengthPerTimeMeasureSub
# end class LengthPerTimeMeasureSub


class LengthPerTimeMeasureExtSub(supermod.LengthPerTimeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(LengthPerTimeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.LengthPerTimeMeasureExt.subclass = LengthPerTimeMeasureExtSub
# end class LengthPerTimeMeasureExtSub


class LengthPerVolumeMeasureSub(supermod.LengthPerVolumeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(LengthPerVolumeMeasureSub, self).__init__(uom, valueOf_, )
supermod.LengthPerVolumeMeasure.subclass = LengthPerVolumeMeasureSub
# end class LengthPerVolumeMeasureSub


class LengthPerVolumeMeasureExtSub(supermod.LengthPerVolumeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(LengthPerVolumeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.LengthPerVolumeMeasureExt.subclass = LengthPerVolumeMeasureExtSub
# end class LengthPerVolumeMeasureExtSub


class LightExposureMeasureSub(supermod.LightExposureMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(LightExposureMeasureSub, self).__init__(uom, valueOf_, )
supermod.LightExposureMeasure.subclass = LightExposureMeasureSub
# end class LightExposureMeasureSub


class LightExposureMeasureExtSub(supermod.LightExposureMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(LightExposureMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.LightExposureMeasureExt.subclass = LightExposureMeasureExtSub
# end class LightExposureMeasureExtSub


class LinearAccelerationMeasureSub(supermod.LinearAccelerationMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(LinearAccelerationMeasureSub, self).__init__(uom, valueOf_, )
supermod.LinearAccelerationMeasure.subclass = LinearAccelerationMeasureSub
# end class LinearAccelerationMeasureSub


class LinearAccelerationMeasureExtSub(supermod.LinearAccelerationMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(LinearAccelerationMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.LinearAccelerationMeasureExt.subclass = LinearAccelerationMeasureExtSub
# end class LinearAccelerationMeasureExtSub


class LinearThermalExpansionMeasureSub(supermod.LinearThermalExpansionMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(LinearThermalExpansionMeasureSub, self).__init__(uom, valueOf_, )
supermod.LinearThermalExpansionMeasure.subclass = LinearThermalExpansionMeasureSub
# end class LinearThermalExpansionMeasureSub


class LinearThermalExpansionMeasureExtSub(supermod.LinearThermalExpansionMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(LinearThermalExpansionMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.LinearThermalExpansionMeasureExt.subclass = LinearThermalExpansionMeasureExtSub
# end class LinearThermalExpansionMeasureExtSub


class LogarithmicPowerRatioMeasureSub(supermod.LogarithmicPowerRatioMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(LogarithmicPowerRatioMeasureSub, self).__init__(uom, valueOf_, )
supermod.LogarithmicPowerRatioMeasure.subclass = LogarithmicPowerRatioMeasureSub
# end class LogarithmicPowerRatioMeasureSub


class LogarithmicPowerRatioMeasureExtSub(supermod.LogarithmicPowerRatioMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(LogarithmicPowerRatioMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.LogarithmicPowerRatioMeasureExt.subclass = LogarithmicPowerRatioMeasureExtSub
# end class LogarithmicPowerRatioMeasureExtSub


class LogarithmicPowerRatioPerLengthMeasureSub(supermod.LogarithmicPowerRatioPerLengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(LogarithmicPowerRatioPerLengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.LogarithmicPowerRatioPerLengthMeasure.subclass = LogarithmicPowerRatioPerLengthMeasureSub
# end class LogarithmicPowerRatioPerLengthMeasureSub


class LogarithmicPowerRatioPerLengthMeasureExtSub(supermod.LogarithmicPowerRatioPerLengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(LogarithmicPowerRatioPerLengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.LogarithmicPowerRatioPerLengthMeasureExt.subclass = LogarithmicPowerRatioPerLengthMeasureExtSub
# end class LogarithmicPowerRatioPerLengthMeasureExtSub


class LuminanceMeasureSub(supermod.LuminanceMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(LuminanceMeasureSub, self).__init__(uom, valueOf_, )
supermod.LuminanceMeasure.subclass = LuminanceMeasureSub
# end class LuminanceMeasureSub


class LuminanceMeasureExtSub(supermod.LuminanceMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(LuminanceMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.LuminanceMeasureExt.subclass = LuminanceMeasureExtSub
# end class LuminanceMeasureExtSub


class LuminousEfficacyMeasureSub(supermod.LuminousEfficacyMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(LuminousEfficacyMeasureSub, self).__init__(uom, valueOf_, )
supermod.LuminousEfficacyMeasure.subclass = LuminousEfficacyMeasureSub
# end class LuminousEfficacyMeasureSub


class LuminousEfficacyMeasureExtSub(supermod.LuminousEfficacyMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(LuminousEfficacyMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.LuminousEfficacyMeasureExt.subclass = LuminousEfficacyMeasureExtSub
# end class LuminousEfficacyMeasureExtSub


class LuminousFluxMeasureSub(supermod.LuminousFluxMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(LuminousFluxMeasureSub, self).__init__(uom, valueOf_, )
supermod.LuminousFluxMeasure.subclass = LuminousFluxMeasureSub
# end class LuminousFluxMeasureSub


class LuminousFluxMeasureExtSub(supermod.LuminousFluxMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(LuminousFluxMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.LuminousFluxMeasureExt.subclass = LuminousFluxMeasureExtSub
# end class LuminousFluxMeasureExtSub


class LuminousIntensityMeasureSub(supermod.LuminousIntensityMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(LuminousIntensityMeasureSub, self).__init__(uom, valueOf_, )
supermod.LuminousIntensityMeasure.subclass = LuminousIntensityMeasureSub
# end class LuminousIntensityMeasureSub


class LuminousIntensityMeasureExtSub(supermod.LuminousIntensityMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(LuminousIntensityMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.LuminousIntensityMeasureExt.subclass = LuminousIntensityMeasureExtSub
# end class LuminousIntensityMeasureExtSub


class MagneticDipoleMomentMeasureSub(supermod.MagneticDipoleMomentMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MagneticDipoleMomentMeasureSub, self).__init__(uom, valueOf_, )
supermod.MagneticDipoleMomentMeasure.subclass = MagneticDipoleMomentMeasureSub
# end class MagneticDipoleMomentMeasureSub


class MagneticDipoleMomentMeasureExtSub(supermod.MagneticDipoleMomentMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MagneticDipoleMomentMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MagneticDipoleMomentMeasureExt.subclass = MagneticDipoleMomentMeasureExtSub
# end class MagneticDipoleMomentMeasureExtSub


class MagneticFieldStrengthMeasureSub(supermod.MagneticFieldStrengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MagneticFieldStrengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.MagneticFieldStrengthMeasure.subclass = MagneticFieldStrengthMeasureSub
# end class MagneticFieldStrengthMeasureSub


class MagneticFieldStrengthMeasureExtSub(supermod.MagneticFieldStrengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MagneticFieldStrengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MagneticFieldStrengthMeasureExt.subclass = MagneticFieldStrengthMeasureExtSub
# end class MagneticFieldStrengthMeasureExtSub


class MagneticFluxDensityMeasureSub(supermod.MagneticFluxDensityMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MagneticFluxDensityMeasureSub, self).__init__(uom, valueOf_, )
supermod.MagneticFluxDensityMeasure.subclass = MagneticFluxDensityMeasureSub
# end class MagneticFluxDensityMeasureSub


class MagneticFluxDensityMeasureExtSub(supermod.MagneticFluxDensityMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MagneticFluxDensityMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MagneticFluxDensityMeasureExt.subclass = MagneticFluxDensityMeasureExtSub
# end class MagneticFluxDensityMeasureExtSub


class MagneticFluxDensityPerLengthMeasureSub(supermod.MagneticFluxDensityPerLengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MagneticFluxDensityPerLengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.MagneticFluxDensityPerLengthMeasure.subclass = MagneticFluxDensityPerLengthMeasureSub
# end class MagneticFluxDensityPerLengthMeasureSub


class MagneticFluxDensityPerLengthMeasureExtSub(supermod.MagneticFluxDensityPerLengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MagneticFluxDensityPerLengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MagneticFluxDensityPerLengthMeasureExt.subclass = MagneticFluxDensityPerLengthMeasureExtSub
# end class MagneticFluxDensityPerLengthMeasureExtSub


class MagneticFluxMeasureSub(supermod.MagneticFluxMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MagneticFluxMeasureSub, self).__init__(uom, valueOf_, )
supermod.MagneticFluxMeasure.subclass = MagneticFluxMeasureSub
# end class MagneticFluxMeasureSub


class MagneticFluxMeasureExtSub(supermod.MagneticFluxMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MagneticFluxMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MagneticFluxMeasureExt.subclass = MagneticFluxMeasureExtSub
# end class MagneticFluxMeasureExtSub


class MagneticPermeabilityMeasureSub(supermod.MagneticPermeabilityMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MagneticPermeabilityMeasureSub, self).__init__(uom, valueOf_, )
supermod.MagneticPermeabilityMeasure.subclass = MagneticPermeabilityMeasureSub
# end class MagneticPermeabilityMeasureSub


class MagneticPermeabilityMeasureExtSub(supermod.MagneticPermeabilityMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MagneticPermeabilityMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MagneticPermeabilityMeasureExt.subclass = MagneticPermeabilityMeasureExtSub
# end class MagneticPermeabilityMeasureExtSub


class MagneticVectorPotentialMeasureSub(supermod.MagneticVectorPotentialMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MagneticVectorPotentialMeasureSub, self).__init__(uom, valueOf_, )
supermod.MagneticVectorPotentialMeasure.subclass = MagneticVectorPotentialMeasureSub
# end class MagneticVectorPotentialMeasureSub


class MagneticVectorPotentialMeasureExtSub(supermod.MagneticVectorPotentialMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MagneticVectorPotentialMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MagneticVectorPotentialMeasureExt.subclass = MagneticVectorPotentialMeasureExtSub
# end class MagneticVectorPotentialMeasureExtSub


class MassLengthMeasureSub(supermod.MassLengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MassLengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.MassLengthMeasure.subclass = MassLengthMeasureSub
# end class MassLengthMeasureSub


class MassLengthMeasureExtSub(supermod.MassLengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MassLengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MassLengthMeasureExt.subclass = MassLengthMeasureExtSub
# end class MassLengthMeasureExtSub


class MassMeasureSub(supermod.MassMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MassMeasureSub, self).__init__(uom, valueOf_, )
supermod.MassMeasure.subclass = MassMeasureSub
# end class MassMeasureSub


class MassMeasureExtSub(supermod.MassMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MassMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MassMeasureExt.subclass = MassMeasureExtSub
# end class MassMeasureExtSub


class MassPerAreaMeasureSub(supermod.MassPerAreaMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MassPerAreaMeasureSub, self).__init__(uom, valueOf_, )
supermod.MassPerAreaMeasure.subclass = MassPerAreaMeasureSub
# end class MassPerAreaMeasureSub


class MassPerAreaMeasureExtSub(supermod.MassPerAreaMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MassPerAreaMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MassPerAreaMeasureExt.subclass = MassPerAreaMeasureExtSub
# end class MassPerAreaMeasureExtSub


class MassPerEnergyMeasureSub(supermod.MassPerEnergyMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MassPerEnergyMeasureSub, self).__init__(uom, valueOf_, )
supermod.MassPerEnergyMeasure.subclass = MassPerEnergyMeasureSub
# end class MassPerEnergyMeasureSub


class MassPerEnergyMeasureExtSub(supermod.MassPerEnergyMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MassPerEnergyMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MassPerEnergyMeasureExt.subclass = MassPerEnergyMeasureExtSub
# end class MassPerEnergyMeasureExtSub


class MassPerLengthMeasureSub(supermod.MassPerLengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MassPerLengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.MassPerLengthMeasure.subclass = MassPerLengthMeasureSub
# end class MassPerLengthMeasureSub


class MassPerLengthMeasureExtSub(supermod.MassPerLengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MassPerLengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MassPerLengthMeasureExt.subclass = MassPerLengthMeasureExtSub
# end class MassPerLengthMeasureExtSub


class MassPerMassMeasureSub(supermod.MassPerMassMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MassPerMassMeasureSub, self).__init__(uom, valueOf_, )
supermod.MassPerMassMeasure.subclass = MassPerMassMeasureSub
# end class MassPerMassMeasureSub


class MassPerMassMeasureExtSub(supermod.MassPerMassMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MassPerMassMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MassPerMassMeasureExt.subclass = MassPerMassMeasureExtSub
# end class MassPerMassMeasureExtSub


class MassPerTimeMeasureSub(supermod.MassPerTimeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MassPerTimeMeasureSub, self).__init__(uom, valueOf_, )
supermod.MassPerTimeMeasure.subclass = MassPerTimeMeasureSub
# end class MassPerTimeMeasureSub


class MassPerTimeMeasureExtSub(supermod.MassPerTimeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MassPerTimeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MassPerTimeMeasureExt.subclass = MassPerTimeMeasureExtSub
# end class MassPerTimeMeasureExtSub


class MassPerTimePerAreaMeasureSub(supermod.MassPerTimePerAreaMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MassPerTimePerAreaMeasureSub, self).__init__(uom, valueOf_, )
supermod.MassPerTimePerAreaMeasure.subclass = MassPerTimePerAreaMeasureSub
# end class MassPerTimePerAreaMeasureSub


class MassPerTimePerAreaMeasureExtSub(supermod.MassPerTimePerAreaMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MassPerTimePerAreaMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MassPerTimePerAreaMeasureExt.subclass = MassPerTimePerAreaMeasureExtSub
# end class MassPerTimePerAreaMeasureExtSub


class MassPerTimePerLengthMeasureSub(supermod.MassPerTimePerLengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MassPerTimePerLengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.MassPerTimePerLengthMeasure.subclass = MassPerTimePerLengthMeasureSub
# end class MassPerTimePerLengthMeasureSub


class MassPerTimePerLengthMeasureExtSub(supermod.MassPerTimePerLengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MassPerTimePerLengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MassPerTimePerLengthMeasureExt.subclass = MassPerTimePerLengthMeasureExtSub
# end class MassPerTimePerLengthMeasureExtSub


class MassPerVolumeMeasureSub(supermod.MassPerVolumeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MassPerVolumeMeasureSub, self).__init__(uom, valueOf_, )
supermod.MassPerVolumeMeasure.subclass = MassPerVolumeMeasureSub
# end class MassPerVolumeMeasureSub


class MassPerVolumeMeasureExtSub(supermod.MassPerVolumeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MassPerVolumeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MassPerVolumeMeasureExt.subclass = MassPerVolumeMeasureExtSub
# end class MassPerVolumeMeasureExtSub


class MassPerVolumePerLengthMeasureSub(supermod.MassPerVolumePerLengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MassPerVolumePerLengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.MassPerVolumePerLengthMeasure.subclass = MassPerVolumePerLengthMeasureSub
# end class MassPerVolumePerLengthMeasureSub


class MassPerVolumePerLengthMeasureExtSub(supermod.MassPerVolumePerLengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MassPerVolumePerLengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MassPerVolumePerLengthMeasureExt.subclass = MassPerVolumePerLengthMeasureExtSub
# end class MassPerVolumePerLengthMeasureExtSub


class MassPerVolumePerPressureMeasureSub(supermod.MassPerVolumePerPressureMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MassPerVolumePerPressureMeasureSub, self).__init__(uom, valueOf_, )
supermod.MassPerVolumePerPressureMeasure.subclass = MassPerVolumePerPressureMeasureSub
# end class MassPerVolumePerPressureMeasureSub


class MassPerVolumePerPressureMeasureExtSub(supermod.MassPerVolumePerPressureMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MassPerVolumePerPressureMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MassPerVolumePerPressureMeasureExt.subclass = MassPerVolumePerPressureMeasureExtSub
# end class MassPerVolumePerPressureMeasureExtSub


class MassPerVolumePerTemperatureMeasureSub(supermod.MassPerVolumePerTemperatureMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MassPerVolumePerTemperatureMeasureSub, self).__init__(uom, valueOf_, )
supermod.MassPerVolumePerTemperatureMeasure.subclass = MassPerVolumePerTemperatureMeasureSub
# end class MassPerVolumePerTemperatureMeasureSub


class MassPerVolumePerTemperatureMeasureExtSub(supermod.MassPerVolumePerTemperatureMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MassPerVolumePerTemperatureMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MassPerVolumePerTemperatureMeasureExt.subclass = MassPerVolumePerTemperatureMeasureExtSub
# end class MassPerVolumePerTemperatureMeasureExtSub


class MobilityMeasureSub(supermod.MobilityMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MobilityMeasureSub, self).__init__(uom, valueOf_, )
supermod.MobilityMeasure.subclass = MobilityMeasureSub
# end class MobilityMeasureSub


class MobilityMeasureExtSub(supermod.MobilityMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MobilityMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MobilityMeasureExt.subclass = MobilityMeasureExtSub
# end class MobilityMeasureExtSub


class MolarEnergyMeasureSub(supermod.MolarEnergyMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MolarEnergyMeasureSub, self).__init__(uom, valueOf_, )
supermod.MolarEnergyMeasure.subclass = MolarEnergyMeasureSub
# end class MolarEnergyMeasureSub


class MolarEnergyMeasureExtSub(supermod.MolarEnergyMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MolarEnergyMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MolarEnergyMeasureExt.subclass = MolarEnergyMeasureExtSub
# end class MolarEnergyMeasureExtSub


class MolarHeatCapacityMeasureSub(supermod.MolarHeatCapacityMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MolarHeatCapacityMeasureSub, self).__init__(uom, valueOf_, )
supermod.MolarHeatCapacityMeasure.subclass = MolarHeatCapacityMeasureSub
# end class MolarHeatCapacityMeasureSub


class MolarHeatCapacityMeasureExtSub(supermod.MolarHeatCapacityMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MolarHeatCapacityMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MolarHeatCapacityMeasureExt.subclass = MolarHeatCapacityMeasureExtSub
# end class MolarHeatCapacityMeasureExtSub


class MolarVolumeMeasureSub(supermod.MolarVolumeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MolarVolumeMeasureSub, self).__init__(uom, valueOf_, )
supermod.MolarVolumeMeasure.subclass = MolarVolumeMeasureSub
# end class MolarVolumeMeasureSub


class MolarVolumeMeasureExtSub(supermod.MolarVolumeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MolarVolumeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MolarVolumeMeasureExt.subclass = MolarVolumeMeasureExtSub
# end class MolarVolumeMeasureExtSub


class MolecularWeightMeasureSub(supermod.MolecularWeightMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MolecularWeightMeasureSub, self).__init__(uom, valueOf_, )
supermod.MolecularWeightMeasure.subclass = MolecularWeightMeasureSub
# end class MolecularWeightMeasureSub


class MolecularWeightMeasureExtSub(supermod.MolecularWeightMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MolecularWeightMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MolecularWeightMeasureExt.subclass = MolecularWeightMeasureExtSub
# end class MolecularWeightMeasureExtSub


class MomentOfForceMeasureSub(supermod.MomentOfForceMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MomentOfForceMeasureSub, self).__init__(uom, valueOf_, )
supermod.MomentOfForceMeasure.subclass = MomentOfForceMeasureSub
# end class MomentOfForceMeasureSub


class MomentOfForceMeasureExtSub(supermod.MomentOfForceMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MomentOfForceMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MomentOfForceMeasureExt.subclass = MomentOfForceMeasureExtSub
# end class MomentOfForceMeasureExtSub


class MomentOfInertiaMeasureSub(supermod.MomentOfInertiaMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MomentOfInertiaMeasureSub, self).__init__(uom, valueOf_, )
supermod.MomentOfInertiaMeasure.subclass = MomentOfInertiaMeasureSub
# end class MomentOfInertiaMeasureSub


class MomentOfInertiaMeasureExtSub(supermod.MomentOfInertiaMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MomentOfInertiaMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MomentOfInertiaMeasureExt.subclass = MomentOfInertiaMeasureExtSub
# end class MomentOfInertiaMeasureExtSub


class MomentumMeasureSub(supermod.MomentumMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(MomentumMeasureSub, self).__init__(uom, valueOf_, )
supermod.MomentumMeasure.subclass = MomentumMeasureSub
# end class MomentumMeasureSub


class MomentumMeasureExtSub(supermod.MomentumMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(MomentumMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.MomentumMeasureExt.subclass = MomentumMeasureExtSub
# end class MomentumMeasureExtSub


class NormalizedPowerMeasureSub(supermod.NormalizedPowerMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(NormalizedPowerMeasureSub, self).__init__(uom, valueOf_, )
supermod.NormalizedPowerMeasure.subclass = NormalizedPowerMeasureSub
# end class NormalizedPowerMeasureSub


class NormalizedPowerMeasureExtSub(supermod.NormalizedPowerMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(NormalizedPowerMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.NormalizedPowerMeasureExt.subclass = NormalizedPowerMeasureExtSub
# end class NormalizedPowerMeasureExtSub


class PermeabilityLengthMeasureSub(supermod.PermeabilityLengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(PermeabilityLengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.PermeabilityLengthMeasure.subclass = PermeabilityLengthMeasureSub
# end class PermeabilityLengthMeasureSub


class PermeabilityLengthMeasureExtSub(supermod.PermeabilityLengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(PermeabilityLengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.PermeabilityLengthMeasureExt.subclass = PermeabilityLengthMeasureExtSub
# end class PermeabilityLengthMeasureExtSub


class PermeabilityRockMeasureSub(supermod.PermeabilityRockMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(PermeabilityRockMeasureSub, self).__init__(uom, valueOf_, )
supermod.PermeabilityRockMeasure.subclass = PermeabilityRockMeasureSub
# end class PermeabilityRockMeasureSub


class PermeabilityRockMeasureExtSub(supermod.PermeabilityRockMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(PermeabilityRockMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.PermeabilityRockMeasureExt.subclass = PermeabilityRockMeasureExtSub
# end class PermeabilityRockMeasureExtSub


class PermittivityMeasureSub(supermod.PermittivityMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(PermittivityMeasureSub, self).__init__(uom, valueOf_, )
supermod.PermittivityMeasure.subclass = PermittivityMeasureSub
# end class PermittivityMeasureSub


class PermittivityMeasureExtSub(supermod.PermittivityMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(PermittivityMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.PermittivityMeasureExt.subclass = PermittivityMeasureExtSub
# end class PermittivityMeasureExtSub


class PlaneAngleMeasureSub(supermod.PlaneAngleMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(PlaneAngleMeasureSub, self).__init__(uom, valueOf_, )
supermod.PlaneAngleMeasure.subclass = PlaneAngleMeasureSub
# end class PlaneAngleMeasureSub


class PlaneAngleMeasureExtSub(supermod.PlaneAngleMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(PlaneAngleMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.PlaneAngleMeasureExt.subclass = PlaneAngleMeasureExtSub
# end class PlaneAngleMeasureExtSub


class PotentialDifferencePerPowerDropMeasureSub(supermod.PotentialDifferencePerPowerDropMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(PotentialDifferencePerPowerDropMeasureSub, self).__init__(uom, valueOf_, )
supermod.PotentialDifferencePerPowerDropMeasure.subclass = PotentialDifferencePerPowerDropMeasureSub
# end class PotentialDifferencePerPowerDropMeasureSub


class PotentialDifferencePerPowerDropMeasureExtSub(supermod.PotentialDifferencePerPowerDropMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(PotentialDifferencePerPowerDropMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.PotentialDifferencePerPowerDropMeasureExt.subclass = PotentialDifferencePerPowerDropMeasureExtSub
# end class PotentialDifferencePerPowerDropMeasureExtSub


class PowerMeasureSub(supermod.PowerMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(PowerMeasureSub, self).__init__(uom, valueOf_, )
supermod.PowerMeasure.subclass = PowerMeasureSub
# end class PowerMeasureSub


class PowerMeasureExtSub(supermod.PowerMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(PowerMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.PowerMeasureExt.subclass = PowerMeasureExtSub
# end class PowerMeasureExtSub


class PowerPerAreaMeasureSub(supermod.PowerPerAreaMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(PowerPerAreaMeasureSub, self).__init__(uom, valueOf_, )
supermod.PowerPerAreaMeasure.subclass = PowerPerAreaMeasureSub
# end class PowerPerAreaMeasureSub


class PowerPerAreaMeasureExtSub(supermod.PowerPerAreaMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(PowerPerAreaMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.PowerPerAreaMeasureExt.subclass = PowerPerAreaMeasureExtSub
# end class PowerPerAreaMeasureExtSub


class PowerPerPowerMeasureSub(supermod.PowerPerPowerMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(PowerPerPowerMeasureSub, self).__init__(uom, valueOf_, )
supermod.PowerPerPowerMeasure.subclass = PowerPerPowerMeasureSub
# end class PowerPerPowerMeasureSub


class PowerPerPowerMeasureExtSub(supermod.PowerPerPowerMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(PowerPerPowerMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.PowerPerPowerMeasureExt.subclass = PowerPerPowerMeasureExtSub
# end class PowerPerPowerMeasureExtSub


class PowerPerVolumeMeasureSub(supermod.PowerPerVolumeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(PowerPerVolumeMeasureSub, self).__init__(uom, valueOf_, )
supermod.PowerPerVolumeMeasure.subclass = PowerPerVolumeMeasureSub
# end class PowerPerVolumeMeasureSub


class PowerPerVolumeMeasureExtSub(supermod.PowerPerVolumeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(PowerPerVolumeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.PowerPerVolumeMeasureExt.subclass = PowerPerVolumeMeasureExtSub
# end class PowerPerVolumeMeasureExtSub


class PressureMeasureSub(supermod.PressureMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(PressureMeasureSub, self).__init__(uom, valueOf_, )
supermod.PressureMeasure.subclass = PressureMeasureSub
# end class PressureMeasureSub


class PressureMeasureExtSub(supermod.PressureMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(PressureMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.PressureMeasureExt.subclass = PressureMeasureExtSub
# end class PressureMeasureExtSub


class PressurePerPressureMeasureSub(supermod.PressurePerPressureMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(PressurePerPressureMeasureSub, self).__init__(uom, valueOf_, )
supermod.PressurePerPressureMeasure.subclass = PressurePerPressureMeasureSub
# end class PressurePerPressureMeasureSub


class PressurePerPressureMeasureExtSub(supermod.PressurePerPressureMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(PressurePerPressureMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.PressurePerPressureMeasureExt.subclass = PressurePerPressureMeasureExtSub
# end class PressurePerPressureMeasureExtSub


class PressurePerTimeMeasureSub(supermod.PressurePerTimeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(PressurePerTimeMeasureSub, self).__init__(uom, valueOf_, )
supermod.PressurePerTimeMeasure.subclass = PressurePerTimeMeasureSub
# end class PressurePerTimeMeasureSub


class PressurePerTimeMeasureExtSub(supermod.PressurePerTimeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(PressurePerTimeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.PressurePerTimeMeasureExt.subclass = PressurePerTimeMeasureExtSub
# end class PressurePerTimeMeasureExtSub


class PressurePerVolumeMeasureSub(supermod.PressurePerVolumeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(PressurePerVolumeMeasureSub, self).__init__(uom, valueOf_, )
supermod.PressurePerVolumeMeasure.subclass = PressurePerVolumeMeasureSub
# end class PressurePerVolumeMeasureSub


class PressurePerVolumeMeasureExtSub(supermod.PressurePerVolumeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(PressurePerVolumeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.PressurePerVolumeMeasureExt.subclass = PressurePerVolumeMeasureExtSub
# end class PressurePerVolumeMeasureExtSub


class PressureSquaredMeasureSub(supermod.PressureSquaredMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(PressureSquaredMeasureSub, self).__init__(uom, valueOf_, )
supermod.PressureSquaredMeasure.subclass = PressureSquaredMeasureSub
# end class PressureSquaredMeasureSub


class PressureSquaredMeasureExtSub(supermod.PressureSquaredMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(PressureSquaredMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.PressureSquaredMeasureExt.subclass = PressureSquaredMeasureExtSub
# end class PressureSquaredMeasureExtSub


class PressureSquaredPerForceTimePerAreaMeasureSub(supermod.PressureSquaredPerForceTimePerAreaMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(PressureSquaredPerForceTimePerAreaMeasureSub, self).__init__(uom, valueOf_, )
supermod.PressureSquaredPerForceTimePerAreaMeasure.subclass = PressureSquaredPerForceTimePerAreaMeasureSub
# end class PressureSquaredPerForceTimePerAreaMeasureSub


class PressureSquaredPerForceTimePerAreaMeasureExtSub(supermod.PressureSquaredPerForceTimePerAreaMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(PressureSquaredPerForceTimePerAreaMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.PressureSquaredPerForceTimePerAreaMeasureExt.subclass = PressureSquaredPerForceTimePerAreaMeasureExtSub
# end class PressureSquaredPerForceTimePerAreaMeasureExtSub


class PressureTimePerVolumeMeasureSub(supermod.PressureTimePerVolumeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(PressureTimePerVolumeMeasureSub, self).__init__(uom, valueOf_, )
supermod.PressureTimePerVolumeMeasure.subclass = PressureTimePerVolumeMeasureSub
# end class PressureTimePerVolumeMeasureSub


class PressureTimePerVolumeMeasureExtSub(supermod.PressureTimePerVolumeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(PressureTimePerVolumeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.PressureTimePerVolumeMeasureExt.subclass = PressureTimePerVolumeMeasureExtSub
# end class PressureTimePerVolumeMeasureExtSub


class QuantityOfLightMeasureSub(supermod.QuantityOfLightMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(QuantityOfLightMeasureSub, self).__init__(uom, valueOf_, )
supermod.QuantityOfLightMeasure.subclass = QuantityOfLightMeasureSub
# end class QuantityOfLightMeasureSub


class QuantityOfLightMeasureExtSub(supermod.QuantityOfLightMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(QuantityOfLightMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.QuantityOfLightMeasureExt.subclass = QuantityOfLightMeasureExtSub
# end class QuantityOfLightMeasureExtSub


class RadianceMeasureSub(supermod.RadianceMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(RadianceMeasureSub, self).__init__(uom, valueOf_, )
supermod.RadianceMeasure.subclass = RadianceMeasureSub
# end class RadianceMeasureSub


class RadianceMeasureExtSub(supermod.RadianceMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(RadianceMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.RadianceMeasureExt.subclass = RadianceMeasureExtSub
# end class RadianceMeasureExtSub


class RadiantIntensityMeasureSub(supermod.RadiantIntensityMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(RadiantIntensityMeasureSub, self).__init__(uom, valueOf_, )
supermod.RadiantIntensityMeasure.subclass = RadiantIntensityMeasureSub
# end class RadiantIntensityMeasureSub


class RadiantIntensityMeasureExtSub(supermod.RadiantIntensityMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(RadiantIntensityMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.RadiantIntensityMeasureExt.subclass = RadiantIntensityMeasureExtSub
# end class RadiantIntensityMeasureExtSub


class ReciprocalAreaMeasureSub(supermod.ReciprocalAreaMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ReciprocalAreaMeasureSub, self).__init__(uom, valueOf_, )
supermod.ReciprocalAreaMeasure.subclass = ReciprocalAreaMeasureSub
# end class ReciprocalAreaMeasureSub


class ReciprocalAreaMeasureExtSub(supermod.ReciprocalAreaMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ReciprocalAreaMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ReciprocalAreaMeasureExt.subclass = ReciprocalAreaMeasureExtSub
# end class ReciprocalAreaMeasureExtSub


class ReciprocalElectricPotentialDifferenceMeasureSub(supermod.ReciprocalElectricPotentialDifferenceMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ReciprocalElectricPotentialDifferenceMeasureSub, self).__init__(uom, valueOf_, )
supermod.ReciprocalElectricPotentialDifferenceMeasure.subclass = ReciprocalElectricPotentialDifferenceMeasureSub
# end class ReciprocalElectricPotentialDifferenceMeasureSub


class ReciprocalElectricPotentialDifferenceMeasureExtSub(supermod.ReciprocalElectricPotentialDifferenceMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ReciprocalElectricPotentialDifferenceMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ReciprocalElectricPotentialDifferenceMeasureExt.subclass = ReciprocalElectricPotentialDifferenceMeasureExtSub
# end class ReciprocalElectricPotentialDifferenceMeasureExtSub


class ReciprocalForceMeasureSub(supermod.ReciprocalForceMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ReciprocalForceMeasureSub, self).__init__(uom, valueOf_, )
supermod.ReciprocalForceMeasure.subclass = ReciprocalForceMeasureSub
# end class ReciprocalForceMeasureSub


class ReciprocalForceMeasureExtSub(supermod.ReciprocalForceMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ReciprocalForceMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ReciprocalForceMeasureExt.subclass = ReciprocalForceMeasureExtSub
# end class ReciprocalForceMeasureExtSub


class ReciprocalLengthMeasureSub(supermod.ReciprocalLengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ReciprocalLengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.ReciprocalLengthMeasure.subclass = ReciprocalLengthMeasureSub
# end class ReciprocalLengthMeasureSub


class ReciprocalLengthMeasureExtSub(supermod.ReciprocalLengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ReciprocalLengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ReciprocalLengthMeasureExt.subclass = ReciprocalLengthMeasureExtSub
# end class ReciprocalLengthMeasureExtSub


class ReciprocalMassMeasureSub(supermod.ReciprocalMassMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ReciprocalMassMeasureSub, self).__init__(uom, valueOf_, )
supermod.ReciprocalMassMeasure.subclass = ReciprocalMassMeasureSub
# end class ReciprocalMassMeasureSub


class ReciprocalMassMeasureExtSub(supermod.ReciprocalMassMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ReciprocalMassMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ReciprocalMassMeasureExt.subclass = ReciprocalMassMeasureExtSub
# end class ReciprocalMassMeasureExtSub


class ReciprocalMassTimeMeasureSub(supermod.ReciprocalMassTimeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ReciprocalMassTimeMeasureSub, self).__init__(uom, valueOf_, )
supermod.ReciprocalMassTimeMeasure.subclass = ReciprocalMassTimeMeasureSub
# end class ReciprocalMassTimeMeasureSub


class ReciprocalMassTimeMeasureExtSub(supermod.ReciprocalMassTimeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ReciprocalMassTimeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ReciprocalMassTimeMeasureExt.subclass = ReciprocalMassTimeMeasureExtSub
# end class ReciprocalMassTimeMeasureExtSub


class ReciprocalPressureMeasureSub(supermod.ReciprocalPressureMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ReciprocalPressureMeasureSub, self).__init__(uom, valueOf_, )
supermod.ReciprocalPressureMeasure.subclass = ReciprocalPressureMeasureSub
# end class ReciprocalPressureMeasureSub


class ReciprocalPressureMeasureExtSub(supermod.ReciprocalPressureMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ReciprocalPressureMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ReciprocalPressureMeasureExt.subclass = ReciprocalPressureMeasureExtSub
# end class ReciprocalPressureMeasureExtSub


class ReciprocalTimeMeasureSub(supermod.ReciprocalTimeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ReciprocalTimeMeasureSub, self).__init__(uom, valueOf_, )
supermod.ReciprocalTimeMeasure.subclass = ReciprocalTimeMeasureSub
# end class ReciprocalTimeMeasureSub


class ReciprocalTimeMeasureExtSub(supermod.ReciprocalTimeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ReciprocalTimeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ReciprocalTimeMeasureExt.subclass = ReciprocalTimeMeasureExtSub
# end class ReciprocalTimeMeasureExtSub


class ReciprocalVolumeMeasureSub(supermod.ReciprocalVolumeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ReciprocalVolumeMeasureSub, self).__init__(uom, valueOf_, )
supermod.ReciprocalVolumeMeasure.subclass = ReciprocalVolumeMeasureSub
# end class ReciprocalVolumeMeasureSub


class ReciprocalVolumeMeasureExtSub(supermod.ReciprocalVolumeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ReciprocalVolumeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ReciprocalVolumeMeasureExt.subclass = ReciprocalVolumeMeasureExtSub
# end class ReciprocalVolumeMeasureExtSub


class ReluctanceMeasureSub(supermod.ReluctanceMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ReluctanceMeasureSub, self).__init__(uom, valueOf_, )
supermod.ReluctanceMeasure.subclass = ReluctanceMeasureSub
# end class ReluctanceMeasureSub


class ReluctanceMeasureExtSub(supermod.ReluctanceMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ReluctanceMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ReluctanceMeasureExt.subclass = ReluctanceMeasureExtSub
# end class ReluctanceMeasureExtSub


class SecondMomentOfAreaMeasureSub(supermod.SecondMomentOfAreaMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(SecondMomentOfAreaMeasureSub, self).__init__(uom, valueOf_, )
supermod.SecondMomentOfAreaMeasure.subclass = SecondMomentOfAreaMeasureSub
# end class SecondMomentOfAreaMeasureSub


class SecondMomentOfAreaMeasureExtSub(supermod.SecondMomentOfAreaMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(SecondMomentOfAreaMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.SecondMomentOfAreaMeasureExt.subclass = SecondMomentOfAreaMeasureExtSub
# end class SecondMomentOfAreaMeasureExtSub


class SignalingEventPerTimeMeasureSub(supermod.SignalingEventPerTimeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(SignalingEventPerTimeMeasureSub, self).__init__(uom, valueOf_, )
supermod.SignalingEventPerTimeMeasure.subclass = SignalingEventPerTimeMeasureSub
# end class SignalingEventPerTimeMeasureSub


class SignalingEventPerTimeMeasureExtSub(supermod.SignalingEventPerTimeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(SignalingEventPerTimeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.SignalingEventPerTimeMeasureExt.subclass = SignalingEventPerTimeMeasureExtSub
# end class SignalingEventPerTimeMeasureExtSub


class SolidAngleMeasureSub(supermod.SolidAngleMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(SolidAngleMeasureSub, self).__init__(uom, valueOf_, )
supermod.SolidAngleMeasure.subclass = SolidAngleMeasureSub
# end class SolidAngleMeasureSub


class SolidAngleMeasureExtSub(supermod.SolidAngleMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(SolidAngleMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.SolidAngleMeasureExt.subclass = SolidAngleMeasureExtSub
# end class SolidAngleMeasureExtSub


class SpecificHeatCapacityMeasureSub(supermod.SpecificHeatCapacityMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(SpecificHeatCapacityMeasureSub, self).__init__(uom, valueOf_, )
supermod.SpecificHeatCapacityMeasure.subclass = SpecificHeatCapacityMeasureSub
# end class SpecificHeatCapacityMeasureSub


class SpecificHeatCapacityMeasureExtSub(supermod.SpecificHeatCapacityMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(SpecificHeatCapacityMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.SpecificHeatCapacityMeasureExt.subclass = SpecificHeatCapacityMeasureExtSub
# end class SpecificHeatCapacityMeasureExtSub


class TemperatureIntervalMeasureSub(supermod.TemperatureIntervalMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(TemperatureIntervalMeasureSub, self).__init__(uom, valueOf_, )
supermod.TemperatureIntervalMeasure.subclass = TemperatureIntervalMeasureSub
# end class TemperatureIntervalMeasureSub


class TemperatureIntervalMeasureExtSub(supermod.TemperatureIntervalMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(TemperatureIntervalMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.TemperatureIntervalMeasureExt.subclass = TemperatureIntervalMeasureExtSub
# end class TemperatureIntervalMeasureExtSub


class TemperatureIntervalPerLengthMeasureSub(supermod.TemperatureIntervalPerLengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(TemperatureIntervalPerLengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.TemperatureIntervalPerLengthMeasure.subclass = TemperatureIntervalPerLengthMeasureSub
# end class TemperatureIntervalPerLengthMeasureSub


class TemperatureIntervalPerLengthMeasureExtSub(supermod.TemperatureIntervalPerLengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(TemperatureIntervalPerLengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.TemperatureIntervalPerLengthMeasureExt.subclass = TemperatureIntervalPerLengthMeasureExtSub
# end class TemperatureIntervalPerLengthMeasureExtSub


class TemperatureIntervalPerPressureMeasureSub(supermod.TemperatureIntervalPerPressureMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(TemperatureIntervalPerPressureMeasureSub, self).__init__(uom, valueOf_, )
supermod.TemperatureIntervalPerPressureMeasure.subclass = TemperatureIntervalPerPressureMeasureSub
# end class TemperatureIntervalPerPressureMeasureSub


class TemperatureIntervalPerPressureMeasureExtSub(supermod.TemperatureIntervalPerPressureMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(TemperatureIntervalPerPressureMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.TemperatureIntervalPerPressureMeasureExt.subclass = TemperatureIntervalPerPressureMeasureExtSub
# end class TemperatureIntervalPerPressureMeasureExtSub


class TemperatureIntervalPerTimeMeasureSub(supermod.TemperatureIntervalPerTimeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(TemperatureIntervalPerTimeMeasureSub, self).__init__(uom, valueOf_, )
supermod.TemperatureIntervalPerTimeMeasure.subclass = TemperatureIntervalPerTimeMeasureSub
# end class TemperatureIntervalPerTimeMeasureSub


class TemperatureIntervalPerTimeMeasureExtSub(supermod.TemperatureIntervalPerTimeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(TemperatureIntervalPerTimeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.TemperatureIntervalPerTimeMeasureExt.subclass = TemperatureIntervalPerTimeMeasureExtSub
# end class TemperatureIntervalPerTimeMeasureExtSub


class ThermalConductanceMeasureSub(supermod.ThermalConductanceMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ThermalConductanceMeasureSub, self).__init__(uom, valueOf_, )
supermod.ThermalConductanceMeasure.subclass = ThermalConductanceMeasureSub
# end class ThermalConductanceMeasureSub


class ThermalConductanceMeasureExtSub(supermod.ThermalConductanceMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ThermalConductanceMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ThermalConductanceMeasureExt.subclass = ThermalConductanceMeasureExtSub
# end class ThermalConductanceMeasureExtSub


class ThermalConductivityMeasureSub(supermod.ThermalConductivityMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ThermalConductivityMeasureSub, self).__init__(uom, valueOf_, )
supermod.ThermalConductivityMeasure.subclass = ThermalConductivityMeasureSub
# end class ThermalConductivityMeasureSub


class ThermalConductivityMeasureExtSub(supermod.ThermalConductivityMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ThermalConductivityMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ThermalConductivityMeasureExt.subclass = ThermalConductivityMeasureExtSub
# end class ThermalConductivityMeasureExtSub


class ThermalDiffusivityMeasureSub(supermod.ThermalDiffusivityMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ThermalDiffusivityMeasureSub, self).__init__(uom, valueOf_, )
supermod.ThermalDiffusivityMeasure.subclass = ThermalDiffusivityMeasureSub
# end class ThermalDiffusivityMeasureSub


class ThermalDiffusivityMeasureExtSub(supermod.ThermalDiffusivityMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ThermalDiffusivityMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ThermalDiffusivityMeasureExt.subclass = ThermalDiffusivityMeasureExtSub
# end class ThermalDiffusivityMeasureExtSub


class ThermalInsulanceMeasureSub(supermod.ThermalInsulanceMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ThermalInsulanceMeasureSub, self).__init__(uom, valueOf_, )
supermod.ThermalInsulanceMeasure.subclass = ThermalInsulanceMeasureSub
# end class ThermalInsulanceMeasureSub


class ThermalInsulanceMeasureExtSub(supermod.ThermalInsulanceMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ThermalInsulanceMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ThermalInsulanceMeasureExt.subclass = ThermalInsulanceMeasureExtSub
# end class ThermalInsulanceMeasureExtSub


class ThermalResistanceMeasureSub(supermod.ThermalResistanceMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ThermalResistanceMeasureSub, self).__init__(uom, valueOf_, )
supermod.ThermalResistanceMeasure.subclass = ThermalResistanceMeasureSub
# end class ThermalResistanceMeasureSub


class ThermalResistanceMeasureExtSub(supermod.ThermalResistanceMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ThermalResistanceMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ThermalResistanceMeasureExt.subclass = ThermalResistanceMeasureExtSub
# end class ThermalResistanceMeasureExtSub


class ThermodynamicTemperatureMeasureSub(supermod.ThermodynamicTemperatureMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ThermodynamicTemperatureMeasureSub, self).__init__(uom, valueOf_, )
supermod.ThermodynamicTemperatureMeasure.subclass = ThermodynamicTemperatureMeasureSub
# end class ThermodynamicTemperatureMeasureSub


class ThermodynamicTemperatureMeasureExtSub(supermod.ThermodynamicTemperatureMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ThermodynamicTemperatureMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ThermodynamicTemperatureMeasureExt.subclass = ThermodynamicTemperatureMeasureExtSub
# end class ThermodynamicTemperatureMeasureExtSub


class ThermodynamicTemperaturePerThermodynamicTemperatureMeasureSub(supermod.ThermodynamicTemperaturePerThermodynamicTemperatureMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(ThermodynamicTemperaturePerThermodynamicTemperatureMeasureSub, self).__init__(uom, valueOf_, )
supermod.ThermodynamicTemperaturePerThermodynamicTemperatureMeasure.subclass = ThermodynamicTemperaturePerThermodynamicTemperatureMeasureSub
# end class ThermodynamicTemperaturePerThermodynamicTemperatureMeasureSub


class ThermodynamicTemperaturePerThermodynamicTemperatureMeasureExtSub(supermod.ThermodynamicTemperaturePerThermodynamicTemperatureMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(ThermodynamicTemperaturePerThermodynamicTemperatureMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.ThermodynamicTemperaturePerThermodynamicTemperatureMeasureExt.subclass = ThermodynamicTemperaturePerThermodynamicTemperatureMeasureExtSub
# end class ThermodynamicTemperaturePerThermodynamicTemperatureMeasureExtSub


class TimeMeasureSub(supermod.TimeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(TimeMeasureSub, self).__init__(uom, valueOf_, )
supermod.TimeMeasure.subclass = TimeMeasureSub
# end class TimeMeasureSub


class TimeMeasureExtSub(supermod.TimeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(TimeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.TimeMeasureExt.subclass = TimeMeasureExtSub
# end class TimeMeasureExtSub


class TimePerLengthMeasureSub(supermod.TimePerLengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(TimePerLengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.TimePerLengthMeasure.subclass = TimePerLengthMeasureSub
# end class TimePerLengthMeasureSub


class TimePerLengthMeasureExtSub(supermod.TimePerLengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(TimePerLengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.TimePerLengthMeasureExt.subclass = TimePerLengthMeasureExtSub
# end class TimePerLengthMeasureExtSub


class TimePerMassMeasureSub(supermod.TimePerMassMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(TimePerMassMeasureSub, self).__init__(uom, valueOf_, )
supermod.TimePerMassMeasure.subclass = TimePerMassMeasureSub
# end class TimePerMassMeasureSub


class TimePerMassMeasureExtSub(supermod.TimePerMassMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(TimePerMassMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.TimePerMassMeasureExt.subclass = TimePerMassMeasureExtSub
# end class TimePerMassMeasureExtSub


class TimePerTimeMeasureSub(supermod.TimePerTimeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(TimePerTimeMeasureSub, self).__init__(uom, valueOf_, )
supermod.TimePerTimeMeasure.subclass = TimePerTimeMeasureSub
# end class TimePerTimeMeasureSub


class TimePerTimeMeasureExtSub(supermod.TimePerTimeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(TimePerTimeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.TimePerTimeMeasureExt.subclass = TimePerTimeMeasureExtSub
# end class TimePerTimeMeasureExtSub


class TimePerVolumeMeasureSub(supermod.TimePerVolumeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(TimePerVolumeMeasureSub, self).__init__(uom, valueOf_, )
supermod.TimePerVolumeMeasure.subclass = TimePerVolumeMeasureSub
# end class TimePerVolumeMeasureSub


class TimePerVolumeMeasureExtSub(supermod.TimePerVolumeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(TimePerVolumeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.TimePerVolumeMeasureExt.subclass = TimePerVolumeMeasureExtSub
# end class TimePerVolumeMeasureExtSub


class UnitlessMeasureSub(supermod.UnitlessMeasure):
    def __init__(self, valueOf_=None):
        super(UnitlessMeasureSub, self).__init__(valueOf_, )
supermod.UnitlessMeasure.subclass = UnitlessMeasureSub
# end class UnitlessMeasureSub


class VerticalCoordinateMeasureSub(supermod.VerticalCoordinateMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(VerticalCoordinateMeasureSub, self).__init__(uom, valueOf_, )
supermod.VerticalCoordinateMeasure.subclass = VerticalCoordinateMeasureSub
# end class VerticalCoordinateMeasureSub


class VerticalCoordinateMeasureExtSub(supermod.VerticalCoordinateMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(VerticalCoordinateMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.VerticalCoordinateMeasureExt.subclass = VerticalCoordinateMeasureExtSub
# end class VerticalCoordinateMeasureExtSub


class VolumeFlowRatePerVolumeFlowRateMeasureSub(supermod.VolumeFlowRatePerVolumeFlowRateMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumeFlowRatePerVolumeFlowRateMeasureSub, self).__init__(uom, valueOf_, )
supermod.VolumeFlowRatePerVolumeFlowRateMeasure.subclass = VolumeFlowRatePerVolumeFlowRateMeasureSub
# end class VolumeFlowRatePerVolumeFlowRateMeasureSub


class VolumeFlowRatePerVolumeFlowRateMeasureExtSub(supermod.VolumeFlowRatePerVolumeFlowRateMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumeFlowRatePerVolumeFlowRateMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.VolumeFlowRatePerVolumeFlowRateMeasureExt.subclass = VolumeFlowRatePerVolumeFlowRateMeasureExtSub
# end class VolumeFlowRatePerVolumeFlowRateMeasureExtSub


class VolumeMeasureSub(supermod.VolumeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumeMeasureSub, self).__init__(uom, valueOf_, )
supermod.VolumeMeasure.subclass = VolumeMeasureSub
# end class VolumeMeasureSub


class VolumeMeasureExtSub(supermod.VolumeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.VolumeMeasureExt.subclass = VolumeMeasureExtSub
# end class VolumeMeasureExtSub


class VolumePerAreaMeasureSub(supermod.VolumePerAreaMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerAreaMeasureSub, self).__init__(uom, valueOf_, )
supermod.VolumePerAreaMeasure.subclass = VolumePerAreaMeasureSub
# end class VolumePerAreaMeasureSub


class VolumePerAreaMeasureExtSub(supermod.VolumePerAreaMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerAreaMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.VolumePerAreaMeasureExt.subclass = VolumePerAreaMeasureExtSub
# end class VolumePerAreaMeasureExtSub


class VolumePerLengthMeasureSub(supermod.VolumePerLengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerLengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.VolumePerLengthMeasure.subclass = VolumePerLengthMeasureSub
# end class VolumePerLengthMeasureSub


class VolumePerLengthMeasureExtSub(supermod.VolumePerLengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerLengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.VolumePerLengthMeasureExt.subclass = VolumePerLengthMeasureExtSub
# end class VolumePerLengthMeasureExtSub


class VolumePerMassMeasureSub(supermod.VolumePerMassMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerMassMeasureSub, self).__init__(uom, valueOf_, )
supermod.VolumePerMassMeasure.subclass = VolumePerMassMeasureSub
# end class VolumePerMassMeasureSub


class VolumePerMassMeasureExtSub(supermod.VolumePerMassMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerMassMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.VolumePerMassMeasureExt.subclass = VolumePerMassMeasureExtSub
# end class VolumePerMassMeasureExtSub


class VolumePerPressureMeasureSub(supermod.VolumePerPressureMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerPressureMeasureSub, self).__init__(uom, valueOf_, )
supermod.VolumePerPressureMeasure.subclass = VolumePerPressureMeasureSub
# end class VolumePerPressureMeasureSub


class VolumePerPressureMeasureExtSub(supermod.VolumePerPressureMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerPressureMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.VolumePerPressureMeasureExt.subclass = VolumePerPressureMeasureExtSub
# end class VolumePerPressureMeasureExtSub


class VolumePerRotationMeasureSub(supermod.VolumePerRotationMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerRotationMeasureSub, self).__init__(uom, valueOf_, )
supermod.VolumePerRotationMeasure.subclass = VolumePerRotationMeasureSub
# end class VolumePerRotationMeasureSub


class VolumePerRotationMeasureExtSub(supermod.VolumePerRotationMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerRotationMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.VolumePerRotationMeasureExt.subclass = VolumePerRotationMeasureExtSub
# end class VolumePerRotationMeasureExtSub


class VolumePerTimeLengthMeasureSub(supermod.VolumePerTimeLengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerTimeLengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.VolumePerTimeLengthMeasure.subclass = VolumePerTimeLengthMeasureSub
# end class VolumePerTimeLengthMeasureSub


class VolumePerTimeLengthMeasureExtSub(supermod.VolumePerTimeLengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerTimeLengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.VolumePerTimeLengthMeasureExt.subclass = VolumePerTimeLengthMeasureExtSub
# end class VolumePerTimeLengthMeasureExtSub


class VolumePerTimeMeasureSub(supermod.VolumePerTimeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerTimeMeasureSub, self).__init__(uom, valueOf_, )
supermod.VolumePerTimeMeasure.subclass = VolumePerTimeMeasureSub
# end class VolumePerTimeMeasureSub


class VolumePerTimeMeasureExtSub(supermod.VolumePerTimeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerTimeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.VolumePerTimeMeasureExt.subclass = VolumePerTimeMeasureExtSub
# end class VolumePerTimeMeasureExtSub


class VolumePerTimePerAreaMeasureSub(supermod.VolumePerTimePerAreaMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerTimePerAreaMeasureSub, self).__init__(uom, valueOf_, )
supermod.VolumePerTimePerAreaMeasure.subclass = VolumePerTimePerAreaMeasureSub
# end class VolumePerTimePerAreaMeasureSub


class VolumePerTimePerAreaMeasureExtSub(supermod.VolumePerTimePerAreaMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerTimePerAreaMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.VolumePerTimePerAreaMeasureExt.subclass = VolumePerTimePerAreaMeasureExtSub
# end class VolumePerTimePerAreaMeasureExtSub


class VolumePerTimePerLengthMeasureSub(supermod.VolumePerTimePerLengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerTimePerLengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.VolumePerTimePerLengthMeasure.subclass = VolumePerTimePerLengthMeasureSub
# end class VolumePerTimePerLengthMeasureSub


class VolumePerTimePerLengthMeasureExtSub(supermod.VolumePerTimePerLengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerTimePerLengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.VolumePerTimePerLengthMeasureExt.subclass = VolumePerTimePerLengthMeasureExtSub
# end class VolumePerTimePerLengthMeasureExtSub


class VolumePerTimePerPressureLengthMeasureSub(supermod.VolumePerTimePerPressureLengthMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerTimePerPressureLengthMeasureSub, self).__init__(uom, valueOf_, )
supermod.VolumePerTimePerPressureLengthMeasure.subclass = VolumePerTimePerPressureLengthMeasureSub
# end class VolumePerTimePerPressureLengthMeasureSub


class VolumePerTimePerPressureLengthMeasureExtSub(supermod.VolumePerTimePerPressureLengthMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerTimePerPressureLengthMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.VolumePerTimePerPressureLengthMeasureExt.subclass = VolumePerTimePerPressureLengthMeasureExtSub
# end class VolumePerTimePerPressureLengthMeasureExtSub


class VolumePerTimePerPressureMeasureSub(supermod.VolumePerTimePerPressureMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerTimePerPressureMeasureSub, self).__init__(uom, valueOf_, )
supermod.VolumePerTimePerPressureMeasure.subclass = VolumePerTimePerPressureMeasureSub
# end class VolumePerTimePerPressureMeasureSub


class VolumePerTimePerPressureMeasureExtSub(supermod.VolumePerTimePerPressureMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerTimePerPressureMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.VolumePerTimePerPressureMeasureExt.subclass = VolumePerTimePerPressureMeasureExtSub
# end class VolumePerTimePerPressureMeasureExtSub


class VolumePerTimePerTimeMeasureSub(supermod.VolumePerTimePerTimeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerTimePerTimeMeasureSub, self).__init__(uom, valueOf_, )
supermod.VolumePerTimePerTimeMeasure.subclass = VolumePerTimePerTimeMeasureSub
# end class VolumePerTimePerTimeMeasureSub


class VolumePerTimePerTimeMeasureExtSub(supermod.VolumePerTimePerTimeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerTimePerTimeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.VolumePerTimePerTimeMeasureExt.subclass = VolumePerTimePerTimeMeasureExtSub
# end class VolumePerTimePerTimeMeasureExtSub


class VolumePerTimePerVolumeMeasureSub(supermod.VolumePerTimePerVolumeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerTimePerVolumeMeasureSub, self).__init__(uom, valueOf_, )
supermod.VolumePerTimePerVolumeMeasure.subclass = VolumePerTimePerVolumeMeasureSub
# end class VolumePerTimePerVolumeMeasureSub


class VolumePerTimePerVolumeMeasureExtSub(supermod.VolumePerTimePerVolumeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerTimePerVolumeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.VolumePerTimePerVolumeMeasureExt.subclass = VolumePerTimePerVolumeMeasureExtSub
# end class VolumePerTimePerVolumeMeasureExtSub


class VolumePerVolumeMeasureSub(supermod.VolumePerVolumeMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerVolumeMeasureSub, self).__init__(uom, valueOf_, )
supermod.VolumePerVolumeMeasure.subclass = VolumePerVolumeMeasureSub
# end class VolumePerVolumeMeasureSub


class VolumePerVolumeMeasureExtSub(supermod.VolumePerVolumeMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumePerVolumeMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.VolumePerVolumeMeasureExt.subclass = VolumePerVolumeMeasureExtSub
# end class VolumePerVolumeMeasureExtSub


class VolumetricHeatTransferCoefficientMeasureSub(supermod.VolumetricHeatTransferCoefficientMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumetricHeatTransferCoefficientMeasureSub, self).__init__(uom, valueOf_, )
supermod.VolumetricHeatTransferCoefficientMeasure.subclass = VolumetricHeatTransferCoefficientMeasureSub
# end class VolumetricHeatTransferCoefficientMeasureSub


class VolumetricHeatTransferCoefficientMeasureExtSub(supermod.VolumetricHeatTransferCoefficientMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumetricHeatTransferCoefficientMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.VolumetricHeatTransferCoefficientMeasureExt.subclass = VolumetricHeatTransferCoefficientMeasureExtSub
# end class VolumetricHeatTransferCoefficientMeasureExtSub


class VolumetricThermalExpansionMeasureSub(supermod.VolumetricThermalExpansionMeasure):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumetricThermalExpansionMeasureSub, self).__init__(uom, valueOf_, )
supermod.VolumetricThermalExpansionMeasure.subclass = VolumetricThermalExpansionMeasureSub
# end class VolumetricThermalExpansionMeasureSub


class VolumetricThermalExpansionMeasureExtSub(supermod.VolumetricThermalExpansionMeasureExt):
    def __init__(self, uom=None, valueOf_=None):
        super(VolumetricThermalExpansionMeasureExtSub, self).__init__(uom, valueOf_, )
supermod.VolumetricThermalExpansionMeasureExt.subclass = VolumetricThermalExpansionMeasureExtSub
# end class VolumetricThermalExpansionMeasureExtSub


class DefinitionBaseTypeSub(supermod.DefinitionBaseType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, extensiontype_=None):
        super(DefinitionBaseTypeSub, self).__init__(id, description, descriptionReference, identifier, name, extensiontype_, )
supermod.DefinitionBaseType.subclass = DefinitionBaseTypeSub
# end class DefinitionBaseTypeSub


class AbstractGMLTypeSub(supermod.AbstractGMLType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, extensiontype_=None):
        super(AbstractGMLTypeSub, self).__init__(id, description, descriptionReference, identifier, name, extensiontype_, )
supermod.AbstractGMLType.subclass = AbstractGMLTypeSub
# end class AbstractGMLTypeSub


class StringOrRefTypeSub(supermod.StringOrRefType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, nilReason=None, valueOf_=None):
        super(StringOrRefTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, nilReason, valueOf_, )
supermod.StringOrRefType.subclass = StringOrRefTypeSub
# end class StringOrRefTypeSub


class ReferenceTypeSub(supermod.ReferenceType):
    def __init__(self, owns='false', type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, nilReason=None):
        super(ReferenceTypeSub, self).__init__(owns, type_, href, role, arcrole, title, show, actuate, nilReason, )
supermod.ReferenceType.subclass = ReferenceTypeSub
# end class ReferenceTypeSub


class CodeTypeSub(supermod.CodeType):
    def __init__(self, codeSpace=None, valueOf_=None, extensiontype_=None):
        super(CodeTypeSub, self).__init__(codeSpace, valueOf_, extensiontype_, )
supermod.CodeType.subclass = CodeTypeSub
# end class CodeTypeSub


class domainOfValiditySub(supermod.domainOfValidity):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, nilReason=None, EX_Extent=None):
        super(domainOfValiditySub, self).__init__(type_, href, role, arcrole, title, show, actuate, nilReason, EX_Extent, )
supermod.domainOfValidity.subclass = domainOfValiditySub
# end class domainOfValiditySub


class AbstractTimeObjectTypeSub(supermod.AbstractTimeObjectType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, extensiontype_=None):
        super(AbstractTimeObjectTypeSub, self).__init__(id, description, descriptionReference, identifier, name, extensiontype_, )
supermod.AbstractTimeObjectType.subclass = AbstractTimeObjectTypeSub
# end class AbstractTimeObjectTypeSub


class TimePrimitivePropertyTypeSub(supermod.TimePrimitivePropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, nilReason=None, owns='false', AbstractTimePrimitive=None, extensiontype_=None):
        super(TimePrimitivePropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, nilReason, owns, AbstractTimePrimitive, extensiontype_, )
supermod.TimePrimitivePropertyType.subclass = TimePrimitivePropertyTypeSub
# end class TimePrimitivePropertyTypeSub


class EllipsoidalCSPropertyTypeSub(supermod.EllipsoidalCSPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, nilReason=None, EllipsoidalCS=None):
        super(EllipsoidalCSPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, nilReason, EllipsoidalCS, )
supermod.EllipsoidalCSPropertyType.subclass = EllipsoidalCSPropertyTypeSub
# end class EllipsoidalCSPropertyTypeSub


class CoordinateSystemAxisPropertyTypeSub(supermod.CoordinateSystemAxisPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, nilReason=None, CoordinateSystemAxis=None):
        super(CoordinateSystemAxisPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, nilReason, CoordinateSystemAxis, )
supermod.CoordinateSystemAxisPropertyType.subclass = CoordinateSystemAxisPropertyTypeSub
# end class CoordinateSystemAxisPropertyTypeSub


class CartesianCSPropertyTypeSub(supermod.CartesianCSPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, nilReason=None, CartesianCS=None):
        super(CartesianCSPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, nilReason, CartesianCS, )
supermod.CartesianCSPropertyType.subclass = CartesianCSPropertyTypeSub
# end class CartesianCSPropertyTypeSub


class SphericalCSPropertyTypeSub(supermod.SphericalCSPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, nilReason=None, SphericalCS=None):
        super(SphericalCSPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, nilReason, SphericalCS, )
supermod.SphericalCSPropertyType.subclass = SphericalCSPropertyTypeSub
# end class SphericalCSPropertyTypeSub


class GeodeticDatumPropertyTypeSub(supermod.GeodeticDatumPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, nilReason=None, GeodeticDatum=None):
        super(GeodeticDatumPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, nilReason, GeodeticDatum, )
supermod.GeodeticDatumPropertyType.subclass = GeodeticDatumPropertyTypeSub
# end class GeodeticDatumPropertyTypeSub


class PrimeMeridianPropertyTypeSub(supermod.PrimeMeridianPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, nilReason=None, PrimeMeridian=None):
        super(PrimeMeridianPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, nilReason, PrimeMeridian, )
supermod.PrimeMeridianPropertyType.subclass = PrimeMeridianPropertyTypeSub
# end class PrimeMeridianPropertyTypeSub


class MeasureTypeSub(supermod.MeasureType):
    def __init__(self, valueOf_=None, extensiontype_=None):
        super(MeasureTypeSub, self).__init__(valueOf_, extensiontype_, )
supermod.MeasureType.subclass = MeasureTypeSub
# end class MeasureTypeSub


class EllipsoidPropertyTypeSub(supermod.EllipsoidPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, nilReason=None, Ellipsoid=None):
        super(EllipsoidPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, nilReason, Ellipsoid, )
supermod.EllipsoidPropertyType.subclass = EllipsoidPropertyTypeSub
# end class EllipsoidPropertyTypeSub


class secondDefiningParameterSub(supermod.secondDefiningParameter):
    def __init__(self, SecondDefiningParameter=None):
        super(secondDefiningParameterSub, self).__init__(SecondDefiningParameter, )
supermod.secondDefiningParameter.subclass = secondDefiningParameterSub
# end class secondDefiningParameterSub


class SecondDefiningParameterSub(supermod.SecondDefiningParameter):
    def __init__(self, inverseFlattening=None, semiMinorAxis=None, isSphere='true'):
        super(SecondDefiningParameterSub, self).__init__(inverseFlattening, semiMinorAxis, isSphere, )
supermod.SecondDefiningParameter.subclass = SecondDefiningParameterSub
# end class SecondDefiningParameterSub


class LengthTypeSub(supermod.LengthType):
    def __init__(self, valueOf_=None):
        super(LengthTypeSub, self).__init__(valueOf_, )
supermod.LengthType.subclass = LengthTypeSub
# end class LengthTypeSub


class GeneralConversionPropertyTypeSub(supermod.GeneralConversionPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, nilReason=None, AbstractGeneralConversion=None):
        super(GeneralConversionPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, nilReason, AbstractGeneralConversion, )
supermod.GeneralConversionPropertyType.subclass = GeneralConversionPropertyTypeSub
# end class GeneralConversionPropertyTypeSub


class AbstractGeneralConversionTypeSub(supermod.AbstractGeneralConversionType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, remarks=None, domainOfValidity=None, scope=None, coordinateOperationAccuracy=None):
        super(AbstractGeneralConversionTypeSub, self).__init__(id, description, descriptionReference, identifier, name, remarks, domainOfValidity, scope, coordinateOperationAccuracy, )
supermod.AbstractGeneralConversionType.subclass = AbstractGeneralConversionTypeSub
# end class AbstractGeneralConversionTypeSub


class coordinateOperationAccuracySub(supermod.coordinateOperationAccuracy):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, nilReason=None, AbstractDQ_PositionalAccuracy=None):
        super(coordinateOperationAccuracySub, self).__init__(type_, href, role, arcrole, title, show, actuate, nilReason, AbstractDQ_PositionalAccuracy, )
supermod.coordinateOperationAccuracy.subclass = coordinateOperationAccuracySub
# end class coordinateOperationAccuracySub


class CRSPropertyTypeSub(supermod.CRSPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, nilReason=None, AbstractCRS=None):
        super(CRSPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, nilReason, AbstractCRS, )
supermod.CRSPropertyType.subclass = CRSPropertyTypeSub
# end class CRSPropertyTypeSub


class GeodeticCRSPropertyTypeSub(supermod.GeodeticCRSPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, nilReason=None, GeodeticCRS=None):
        super(GeodeticCRSPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, nilReason, GeodeticCRS, )
supermod.GeodeticCRSPropertyType.subclass = GeodeticCRSPropertyTypeSub
# end class GeodeticCRSPropertyTypeSub


class VerticalCSPropertyTypeSub(supermod.VerticalCSPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, nilReason=None, VerticalCS=None):
        super(VerticalCSPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, nilReason, VerticalCS, )
supermod.VerticalCSPropertyType.subclass = VerticalCSPropertyTypeSub
# end class VerticalCSPropertyTypeSub


class VerticalDatumPropertyTypeSub(supermod.VerticalDatumPropertyType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, nilReason=None, VerticalDatum=None):
        super(VerticalDatumPropertyTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, nilReason, VerticalDatum, )
supermod.VerticalDatumPropertyType.subclass = VerticalDatumPropertyTypeSub
# end class VerticalDatumPropertyTypeSub


class EX_GeographicExtent_PropertyTypeSub(supermod.EX_GeographicExtent_PropertyType):
    def __init__(self, nilReason=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, uuidref=None, AbstractEX_GeographicExtent=None):
        super(EX_GeographicExtent_PropertyTypeSub, self).__init__(nilReason, type_, href, role, arcrole, title, show, actuate, uuidref, AbstractEX_GeographicExtent, )
supermod.EX_GeographicExtent_PropertyType.subclass = EX_GeographicExtent_PropertyTypeSub
# end class EX_GeographicExtent_PropertyTypeSub


class EX_TemporalExtent_PropertyTypeSub(supermod.EX_TemporalExtent_PropertyType):
    def __init__(self, nilReason=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, uuidref=None, EX_TemporalExtent=None):
        super(EX_TemporalExtent_PropertyTypeSub, self).__init__(nilReason, type_, href, role, arcrole, title, show, actuate, uuidref, EX_TemporalExtent, )
supermod.EX_TemporalExtent_PropertyType.subclass = EX_TemporalExtent_PropertyTypeSub
# end class EX_TemporalExtent_PropertyTypeSub


class EX_VerticalExtent_PropertyTypeSub(supermod.EX_VerticalExtent_PropertyType):
    def __init__(self, nilReason=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, uuidref=None, EX_VerticalExtent=None):
        super(EX_VerticalExtent_PropertyTypeSub, self).__init__(nilReason, type_, href, role, arcrole, title, show, actuate, uuidref, EX_VerticalExtent, )
supermod.EX_VerticalExtent_PropertyType.subclass = EX_VerticalExtent_PropertyTypeSub
# end class EX_VerticalExtent_PropertyTypeSub


class MD_Identifier_PropertyTypeSub(supermod.MD_Identifier_PropertyType):
    def __init__(self, nilReason=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, uuidref=None, MD_Identifier=None):
        super(MD_Identifier_PropertyTypeSub, self).__init__(nilReason, type_, href, role, arcrole, title, show, actuate, uuidref, MD_Identifier, )
supermod.MD_Identifier_PropertyType.subclass = MD_Identifier_PropertyTypeSub
# end class MD_Identifier_PropertyTypeSub


class CI_Citation_PropertyTypeSub(supermod.CI_Citation_PropertyType):
    def __init__(self, nilReason=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, uuidref=None, CI_Citation=None):
        super(CI_Citation_PropertyTypeSub, self).__init__(nilReason, type_, href, role, arcrole, title, show, actuate, uuidref, CI_Citation, )
supermod.CI_Citation_PropertyType.subclass = CI_Citation_PropertyTypeSub
# end class CI_Citation_PropertyTypeSub


class CI_Date_PropertyTypeSub(supermod.CI_Date_PropertyType):
    def __init__(self, nilReason=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, uuidref=None, CI_Date=None):
        super(CI_Date_PropertyTypeSub, self).__init__(nilReason, type_, href, role, arcrole, title, show, actuate, uuidref, CI_Date, )
supermod.CI_Date_PropertyType.subclass = CI_Date_PropertyTypeSub
# end class CI_Date_PropertyTypeSub


class CI_DateTypeCode_PropertyTypeSub(supermod.CI_DateTypeCode_PropertyType):
    def __init__(self, nilReason=None, CI_DateTypeCode=None):
        super(CI_DateTypeCode_PropertyTypeSub, self).__init__(nilReason, CI_DateTypeCode, )
supermod.CI_DateTypeCode_PropertyType.subclass = CI_DateTypeCode_PropertyTypeSub
# end class CI_DateTypeCode_PropertyTypeSub


class CI_ResponsibleParty_PropertyTypeSub(supermod.CI_ResponsibleParty_PropertyType):
    def __init__(self, nilReason=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, uuidref=None, CI_ResponsibleParty=None):
        super(CI_ResponsibleParty_PropertyTypeSub, self).__init__(nilReason, type_, href, role, arcrole, title, show, actuate, uuidref, CI_ResponsibleParty, )
supermod.CI_ResponsibleParty_PropertyType.subclass = CI_ResponsibleParty_PropertyTypeSub
# end class CI_ResponsibleParty_PropertyTypeSub


class CI_Contact_PropertyTypeSub(supermod.CI_Contact_PropertyType):
    def __init__(self, nilReason=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, uuidref=None, CI_Contact=None):
        super(CI_Contact_PropertyTypeSub, self).__init__(nilReason, type_, href, role, arcrole, title, show, actuate, uuidref, CI_Contact, )
supermod.CI_Contact_PropertyType.subclass = CI_Contact_PropertyTypeSub
# end class CI_Contact_PropertyTypeSub


class CI_Telephone_PropertyTypeSub(supermod.CI_Telephone_PropertyType):
    def __init__(self, nilReason=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, uuidref=None, CI_Telephone=None):
        super(CI_Telephone_PropertyTypeSub, self).__init__(nilReason, type_, href, role, arcrole, title, show, actuate, uuidref, CI_Telephone, )
supermod.CI_Telephone_PropertyType.subclass = CI_Telephone_PropertyTypeSub
# end class CI_Telephone_PropertyTypeSub


class CI_Address_PropertyTypeSub(supermod.CI_Address_PropertyType):
    def __init__(self, nilReason=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, uuidref=None, CI_Address=None):
        super(CI_Address_PropertyTypeSub, self).__init__(nilReason, type_, href, role, arcrole, title, show, actuate, uuidref, CI_Address, )
supermod.CI_Address_PropertyType.subclass = CI_Address_PropertyTypeSub
# end class CI_Address_PropertyTypeSub


class CI_OnlineResource_PropertyTypeSub(supermod.CI_OnlineResource_PropertyType):
    def __init__(self, nilReason=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, uuidref=None, CI_OnlineResource=None):
        super(CI_OnlineResource_PropertyTypeSub, self).__init__(nilReason, type_, href, role, arcrole, title, show, actuate, uuidref, CI_OnlineResource, )
supermod.CI_OnlineResource_PropertyType.subclass = CI_OnlineResource_PropertyTypeSub
# end class CI_OnlineResource_PropertyTypeSub


class URL_PropertyTypeSub(supermod.URL_PropertyType):
    def __init__(self, nilReason=None, URL=None):
        super(URL_PropertyTypeSub, self).__init__(nilReason, URL, )
supermod.URL_PropertyType.subclass = URL_PropertyTypeSub
# end class URL_PropertyTypeSub


class CI_OnLineFunctionCode_PropertyTypeSub(supermod.CI_OnLineFunctionCode_PropertyType):
    def __init__(self, nilReason=None, CI_OnLineFunctionCode=None):
        super(CI_OnLineFunctionCode_PropertyTypeSub, self).__init__(nilReason, CI_OnLineFunctionCode, )
supermod.CI_OnLineFunctionCode_PropertyType.subclass = CI_OnLineFunctionCode_PropertyTypeSub
# end class CI_OnLineFunctionCode_PropertyTypeSub


class CI_RoleCode_PropertyTypeSub(supermod.CI_RoleCode_PropertyType):
    def __init__(self, nilReason=None, CI_RoleCode=None):
        super(CI_RoleCode_PropertyTypeSub, self).__init__(nilReason, CI_RoleCode, )
supermod.CI_RoleCode_PropertyType.subclass = CI_RoleCode_PropertyTypeSub
# end class CI_RoleCode_PropertyTypeSub


class CI_PresentationFormCode_PropertyTypeSub(supermod.CI_PresentationFormCode_PropertyType):
    def __init__(self, nilReason=None, CI_PresentationFormCode=None):
        super(CI_PresentationFormCode_PropertyTypeSub, self).__init__(nilReason, CI_PresentationFormCode, )
supermod.CI_PresentationFormCode_PropertyType.subclass = CI_PresentationFormCode_PropertyTypeSub
# end class CI_PresentationFormCode_PropertyTypeSub


class CI_Series_PropertyTypeSub(supermod.CI_Series_PropertyType):
    def __init__(self, nilReason=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, uuidref=None, CI_Series=None):
        super(CI_Series_PropertyTypeSub, self).__init__(nilReason, type_, href, role, arcrole, title, show, actuate, uuidref, CI_Series, )
supermod.CI_Series_PropertyType.subclass = CI_Series_PropertyTypeSub
# end class CI_Series_PropertyTypeSub


class DQ_EvaluationMethodTypeCode_PropertyTypeSub(supermod.DQ_EvaluationMethodTypeCode_PropertyType):
    def __init__(self, nilReason=None, DQ_EvaluationMethodTypeCode=None):
        super(DQ_EvaluationMethodTypeCode_PropertyTypeSub, self).__init__(nilReason, DQ_EvaluationMethodTypeCode, )
supermod.DQ_EvaluationMethodTypeCode_PropertyType.subclass = DQ_EvaluationMethodTypeCode_PropertyTypeSub
# end class DQ_EvaluationMethodTypeCode_PropertyTypeSub


class DQ_Result_PropertyTypeSub(supermod.DQ_Result_PropertyType):
    def __init__(self, nilReason=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, uuidref=None, AbstractDQ_Result=None):
        super(DQ_Result_PropertyTypeSub, self).__init__(nilReason, type_, href, role, arcrole, title, show, actuate, uuidref, AbstractDQ_Result, )
supermod.DQ_Result_PropertyType.subclass = DQ_Result_PropertyTypeSub
# end class DQ_Result_PropertyTypeSub


class TM_Primitive_PropertyTypeSub(supermod.TM_Primitive_PropertyType):
    def __init__(self, nilReason=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, uuidref=None, AbstractTimePrimitive=None):
        super(TM_Primitive_PropertyTypeSub, self).__init__(nilReason, type_, href, role, arcrole, title, show, actuate, uuidref, AbstractTimePrimitive, )
supermod.TM_Primitive_PropertyType.subclass = TM_Primitive_PropertyTypeSub
# end class TM_Primitive_PropertyTypeSub


class AbstractObject_TypeSub(supermod.AbstractObject_Type):
    def __init__(self, id=None, uuid=None, extensiontype_=None):
        super(AbstractObject_TypeSub, self).__init__(id, uuid, extensiontype_, )
supermod.AbstractObject_Type.subclass = AbstractObject_TypeSub
# end class AbstractObject_TypeSub


class CharacterString_PropertyTypeSub(supermod.CharacterString_PropertyType):
    def __init__(self, nilReason=None, CharacterString=None):
        super(CharacterString_PropertyTypeSub, self).__init__(nilReason, CharacterString, )
supermod.CharacterString_PropertyType.subclass = CharacterString_PropertyTypeSub
# end class CharacterString_PropertyTypeSub


class Boolean_PropertyTypeSub(supermod.Boolean_PropertyType):
    def __init__(self, nilReason=None, Boolean=None):
        super(Boolean_PropertyTypeSub, self).__init__(nilReason, Boolean, )
supermod.Boolean_PropertyType.subclass = Boolean_PropertyTypeSub
# end class Boolean_PropertyTypeSub


class Real_PropertyTypeSub(supermod.Real_PropertyType):
    def __init__(self, nilReason=None, Real=None):
        super(Real_PropertyTypeSub, self).__init__(nilReason, Real, )
supermod.Real_PropertyType.subclass = Real_PropertyTypeSub
# end class Real_PropertyTypeSub


class Date_PropertyTypeSub(supermod.Date_PropertyType):
    def __init__(self, nilReason=None, Date=None, DateTime=None):
        super(Date_PropertyTypeSub, self).__init__(nilReason, Date, DateTime, )
supermod.Date_PropertyType.subclass = Date_PropertyTypeSub
# end class Date_PropertyTypeSub


class CodeListValue_TypeSub(supermod.CodeListValue_Type):
    def __init__(self, codeList=None, codeListValue=None, codeSpace=None, valueOf_=None):
        super(CodeListValue_TypeSub, self).__init__(codeList, codeListValue, codeSpace, valueOf_, )
supermod.CodeListValue_Type.subclass = CodeListValue_TypeSub
# end class CodeListValue_TypeSub


class DateTime_PropertyTypeSub(supermod.DateTime_PropertyType):
    def __init__(self, nilReason=None, DateTime=None):
        super(DateTime_PropertyTypeSub, self).__init__(nilReason, DateTime, )
supermod.DateTime_PropertyType.subclass = DateTime_PropertyTypeSub
# end class DateTime_PropertyTypeSub


class SC_CRS_PropertyTypeSub(supermod.SC_CRS_PropertyType):
    def __init__(self, nilReason=None, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, uuidref=None, AbstractCRS=None):
        super(SC_CRS_PropertyTypeSub, self).__init__(nilReason, type_, href, role, arcrole, title, show, actuate, uuidref, AbstractCRS, )
supermod.SC_CRS_PropertyType.subclass = SC_CRS_PropertyTypeSub
# end class SC_CRS_PropertyTypeSub


class DataObjectReferenceSub(supermod.DataObjectReference):
    def __init__(self, ContentType=None, Title=None, Uuid=None, UuidAuthority=None, Uri=None, VersionString=None):
        super(DataObjectReferenceSub, self).__init__(ContentType, Title, Uuid, UuidAuthority, Uri, VersionString, )
supermod.DataObjectReference.subclass = DataObjectReferenceSub
# end class DataObjectReferenceSub


class EpcExternalPartReferenceSub(EmlMixin, supermod.EpcExternalPartReference):
    def __init__(self, _uuid, _filename='data.h5', Filename=None, MimeType=None):
        super(EpcExternalPartReferenceSub, self).__init__(Filename, MimeType, )
        self._uuid = _uuid
        self._filename = _filename

supermod.EpcExternalPartReference.subclass = EpcExternalPartReferenceSub
# end class EpcExternalPartReferenceSub


class ExternalDatasetSub(EmlMixin, supermod.ExternalDataset):
    def __init__(self, ExternalFileProxy=None):
        super(ExternalDatasetSub, self).__init__(ExternalFileProxy, )
supermod.ExternalDataset.subclass = ExternalDatasetSub
# end class ExternalDatasetSub


class ExternalDatasetPartSub(EmlMixin, supermod.ExternalDatasetPart):
    def __init__(self, Count=None, PathInExternalFile=None, StartIndex=None, EpcExternalPartReference=None, extensiontype_=None):
        super(ExternalDatasetPartSub, self).__init__(Count, PathInExternalFile, StartIndex, EpcExternalPartReference, extensiontype_, )
supermod.ExternalDatasetPart.subclass = ExternalDatasetPartSub
# end class ExternalDatasetPartSub


class AbstractActivityParameterSub(supermod.AbstractActivityParameter):
    def __init__(self, Title=None, Index=None, Selection=None, Key=None, extensiontype_=None):
        super(AbstractActivityParameterSub, self).__init__(Title, Index, Selection, Key, extensiontype_, )
supermod.AbstractActivityParameter.subclass = AbstractActivityParameterSub
# end class AbstractActivityParameterSub


class AbstractParameterKeySub(supermod.AbstractParameterKey):
    def __init__(self, extensiontype_=None):
        super(AbstractParameterKeySub, self).__init__(extensiontype_, )
supermod.AbstractParameterKey.subclass = AbstractParameterKeySub
# end class AbstractParameterKeySub


class ActivitySub(supermod.Activity):
    def __init__(self, ActivityDescriptor=None, Parent=None, Parameter=None):
        super(ActivitySub, self).__init__(ActivityDescriptor, Parent, Parameter, )
supermod.Activity.subclass = ActivitySub
# end class ActivitySub


class ActivityTemplateSub(supermod.ActivityTemplate):
    def __init__(self, Parameter=None):
        super(ActivityTemplateSub, self).__init__(Parameter, )
supermod.ActivityTemplate.subclass = ActivityTemplateSub
# end class ActivityTemplateSub


class DataObjectParameterSub(supermod.DataObjectParameter):
    def __init__(self, Title=None, Index=None, Selection=None, Key=None, DataObject=None):
        super(DataObjectParameterSub, self).__init__(Title, Index, Selection, Key, DataObject, )
supermod.DataObjectParameter.subclass = DataObjectParameterSub
# end class DataObjectParameterSub


class DoubleQuantityParameterSub(supermod.DoubleQuantityParameter):
    def __init__(self, Title=None, Index=None, Selection=None, Key=None, Value=None, Uom=None, CustomUnitDictionary=None):
        super(DoubleQuantityParameterSub, self).__init__(Title, Index, Selection, Key, Value, Uom, CustomUnitDictionary, )
supermod.DoubleQuantityParameter.subclass = DoubleQuantityParameterSub
# end class DoubleQuantityParameterSub


class IntegerQuantityParameterSub(supermod.IntegerQuantityParameter):
    def __init__(self, Title=None, Index=None, Selection=None, Key=None, Value=None):
        super(IntegerQuantityParameterSub, self).__init__(Title, Index, Selection, Key, Value, )
supermod.IntegerQuantityParameter.subclass = IntegerQuantityParameterSub
# end class IntegerQuantityParameterSub


class ObjectParameterKeySub(supermod.ObjectParameterKey):
    def __init__(self, DataObject=None):
        super(ObjectParameterKeySub, self).__init__(DataObject, )
supermod.ObjectParameterKey.subclass = ObjectParameterKeySub
# end class ObjectParameterKeySub


class ParameterTemplateSub(supermod.ParameterTemplate):
    def __init__(self, AllowedKind=None, IsInput=None, KeyConstraint=None, IsOutput=None, Title=None, DataObjectContentType=None, MaxOccurs=None, MinOccurs=None, Constraint=None, DefaultValue=None):
        super(ParameterTemplateSub, self).__init__(AllowedKind, IsInput, KeyConstraint, IsOutput, Title, DataObjectContentType, MaxOccurs, MinOccurs, Constraint, DefaultValue, )
supermod.ParameterTemplate.subclass = ParameterTemplateSub
# end class ParameterTemplateSub


class StringParameterSub(supermod.StringParameter):
    def __init__(self, Title=None, Index=None, Selection=None, Key=None, Value=None):
        super(StringParameterSub, self).__init__(Title, Index, Selection, Key, Value, )
supermod.StringParameter.subclass = StringParameterSub
# end class StringParameterSub


class TimeIndexParameterSub(supermod.TimeIndexParameter):
    def __init__(self, Title=None, Index=None, Selection=None, Key=None, TimeIndex=None):
        super(TimeIndexParameterSub, self).__init__(Title, Index, Selection, Key, TimeIndex, )
supermod.TimeIndexParameter.subclass = TimeIndexParameterSub
# end class TimeIndexParameterSub


class TimeIndexParameterKeySub(supermod.TimeIndexParameterKey):
    def __init__(self, TimeIndex=None):
        super(TimeIndexParameterKeySub, self).__init__(TimeIndex, )
supermod.TimeIndexParameterKey.subclass = TimeIndexParameterKeySub
# end class TimeIndexParameterKeySub


class GeologicTimeSub(supermod.GeologicTime):
    def __init__(self, AgeOffsetAttribute=None, DateTime=None):
        super(GeologicTimeSub, self).__init__(AgeOffsetAttribute, DateTime, )
supermod.GeologicTime.subclass = GeologicTimeSub
# end class GeologicTimeSub


class PropertyKindSub(supermod.PropertyKind):
    def __init__(self, IsAbstract=None, DeprecationDate=None, QuantityClass=None, Parent=None):
        super(PropertyKindSub, self).__init__(IsAbstract, DeprecationDate, QuantityClass, Parent, )
supermod.PropertyKind.subclass = PropertyKindSub
# end class PropertyKindSub


class PropertyKindDictionarySub(supermod.PropertyKindDictionary):
    def __init__(self, PropertyKind=None):
        super(PropertyKindDictionarySub, self).__init__(PropertyKind, )
supermod.PropertyKindDictionary.subclass = PropertyKindDictionarySub
# end class PropertyKindDictionarySub


class TimeIndexSub(supermod.TimeIndex):
    def __init__(self, Index=None, TimeSeries=None):
        super(TimeIndexSub, self).__init__(Index, TimeSeries, )
supermod.TimeIndex.subclass = TimeIndexSub
# end class TimeIndexSub


class TimeIndicesSub(supermod.TimeIndices):
    def __init__(self, TimeIndexCount=None, TimeIndexStart=None, SimulatorTimeStep=None, UseInterval=None, TimeSeries=None):
        super(TimeIndicesSub, self).__init__(TimeIndexCount, TimeIndexStart, SimulatorTimeStep, UseInterval, TimeSeries, )
supermod.TimeIndices.subclass = TimeIndicesSub
# end class TimeIndicesSub


class TimeSeriesSub(supermod.TimeSeries):
    def __init__(self, Time=None, TimeSeriesParentage=None):
        super(TimeSeriesSub, self).__init__(Time, TimeSeriesParentage, )
supermod.TimeSeries.subclass = TimeSeriesSub
# end class TimeSeriesSub


class TimeSeriesParentageSub(supermod.TimeSeriesParentage):
    def __init__(self, HasOverlap=None, ParentTimeIndex=None):
        super(TimeSeriesParentageSub, self).__init__(HasOverlap, ParentTimeIndex, )
supermod.TimeSeriesParentage.subclass = TimeSeriesParentageSub
# end class TimeSeriesParentageSub


class AbstractPressureValueSub(supermod.AbstractPressureValue):
    def __init__(self, extensiontype_=None):
        super(AbstractPressureValueSub, self).__init__(extensiontype_, )
supermod.AbstractPressureValue.subclass = AbstractPressureValueSub
# end class AbstractPressureValueSub


class AbstractTemperaturePressureSub(supermod.AbstractTemperaturePressure):
    def __init__(self, extensiontype_=None):
        super(AbstractTemperaturePressureSub, self).__init__(extensiontype_, )
supermod.AbstractTemperaturePressure.subclass = AbstractTemperaturePressureSub
# end class AbstractTemperaturePressureSub


class DensityValueSub(supermod.DensityValue):
    def __init__(self, Density=None, MeasurementPressureTemperature=None):
        super(DensityValueSub, self).__init__(Density, MeasurementPressureTemperature, )
supermod.DensityValue.subclass = DensityValueSub
# end class DensityValueSub


class FlowRateValueSub(supermod.FlowRateValue):
    def __init__(self, FlowRate=None, MeasurementPressureTemperature=None):
        super(FlowRateValueSub, self).__init__(FlowRate, MeasurementPressureTemperature, )
supermod.FlowRateValue.subclass = FlowRateValueSub
# end class FlowRateValueSub


class GaugePressureSub(supermod.GaugePressure):
    def __init__(self, GaugePressure_member=None, ReferencePressure=None):
        super(GaugePressureSub, self).__init__(GaugePressure_member, ReferencePressure, )
supermod.GaugePressure.subclass = GaugePressureSub
# end class GaugePressureSub


class PressureValueSub(supermod.PressureValue):
    def __init__(self, AbstractPressureValue=None):
        super(PressureValueSub, self).__init__(AbstractPressureValue, )
supermod.PressureValue.subclass = PressureValueSub
# end class PressureValueSub


class ReferencePressureSub(supermod.ReferencePressure):
    def __init__(self, uom=None, referencePressureKind=None, valueOf_=None):
        super(ReferencePressureSub, self).__init__(uom, referencePressureKind, valueOf_, )
supermod.ReferencePressure.subclass = ReferencePressureSub
# end class ReferencePressureSub


class ReferenceTemperaturePressureSub(supermod.ReferenceTemperaturePressure):
    def __init__(self, ReferenceTempPres=None):
        super(ReferenceTemperaturePressureSub, self).__init__(ReferenceTempPres, )
supermod.ReferenceTemperaturePressure.subclass = ReferenceTemperaturePressureSub
# end class ReferenceTemperaturePressureSub


class RelativePressureSub(supermod.RelativePressure):
    def __init__(self, RelativePressure_member=None, ReferencePressure=None):
        super(RelativePressureSub, self).__init__(RelativePressure_member, ReferencePressure, )
supermod.RelativePressure.subclass = RelativePressureSub
# end class RelativePressureSub


class TemperaturePressureSub(supermod.TemperaturePressure):
    def __init__(self, Temperature=None, Pressure=None):
        super(TemperaturePressureSub, self).__init__(Temperature, Pressure, )
supermod.TemperaturePressure.subclass = TemperaturePressureSub
# end class TemperaturePressureSub


class VolumeValueSub(supermod.VolumeValue):
    def __init__(self, Volume=None, MeasurementPressureTemperature=None):
        super(VolumeValueSub, self).__init__(Volume, MeasurementPressureTemperature, )
supermod.VolumeValue.subclass = VolumeValueSub
# end class VolumeValueSub


class AbstractGeodeticCrsSub(supermod.AbstractGeodeticCrs):
    def __init__(self, extensiontype_=None):
        super(AbstractGeodeticCrsSub, self).__init__(extensiontype_, )
supermod.AbstractGeodeticCrs.subclass = AbstractGeodeticCrsSub
# end class AbstractGeodeticCrsSub


class AbstractProjectedCrsSub(supermod.AbstractProjectedCrs):
    def __init__(self, extensiontype_=None):
        super(AbstractProjectedCrsSub, self).__init__(extensiontype_, )
supermod.AbstractProjectedCrs.subclass = AbstractProjectedCrsSub
# end class AbstractProjectedCrsSub


class AbstractVerticalCrsSub(supermod.AbstractVerticalCrs):
    def __init__(self, extensiontype_=None):
        super(AbstractVerticalCrsSub, self).__init__(extensiontype_, )
supermod.AbstractVerticalCrs.subclass = AbstractVerticalCrsSub
# end class AbstractVerticalCrsSub


class GeodeticCrsSub(supermod.GeodeticCrs):
    def __init__(self, AbstractGeodeticCrs=None):
        super(GeodeticCrsSub, self).__init__(AbstractGeodeticCrs, )
supermod.GeodeticCrs.subclass = GeodeticCrsSub
# end class GeodeticCrsSub


class GeodeticEpsgCrsSub(supermod.GeodeticEpsgCrs):
    def __init__(self, EpsgCode=None):
        super(GeodeticEpsgCrsSub, self).__init__(EpsgCode, )
supermod.GeodeticEpsgCrs.subclass = GeodeticEpsgCrsSub
# end class GeodeticEpsgCrsSub


class GeodeticGmlCrsSub(supermod.GeodeticGmlCrs):
    def __init__(self, GmlProjectedCrsDefinition=None):
        super(GeodeticGmlCrsSub, self).__init__(GmlProjectedCrsDefinition, )
supermod.GeodeticGmlCrs.subclass = GeodeticGmlCrsSub
# end class GeodeticGmlCrsSub


class GeodeticLocalAuthorityCrsSub(supermod.GeodeticLocalAuthorityCrs):
    def __init__(self, LocalAuthorityCrsName=None):
        super(GeodeticLocalAuthorityCrsSub, self).__init__(LocalAuthorityCrsName, )
supermod.GeodeticLocalAuthorityCrs.subclass = GeodeticLocalAuthorityCrsSub
# end class GeodeticLocalAuthorityCrsSub


class GeodeticUnknownCrsSub(supermod.GeodeticUnknownCrs):
    def __init__(self, Unknown=None):
        super(GeodeticUnknownCrsSub, self).__init__(Unknown, )
supermod.GeodeticUnknownCrs.subclass = GeodeticUnknownCrsSub
# end class GeodeticUnknownCrsSub


class GeodeticWktCrsSub(supermod.GeodeticWktCrs):
    def __init__(self, WellKnownText=None):
        super(GeodeticWktCrsSub, self).__init__(WellKnownText, )
supermod.GeodeticWktCrs.subclass = GeodeticWktCrsSub
# end class GeodeticWktCrsSub


class ProjectedCrsSub(supermod.ProjectedCrs):
    def __init__(self, uom=None, AxisOrder=None, AbstractProjectedCrs=None):
        super(ProjectedCrsSub, self).__init__(uom, AxisOrder, AbstractProjectedCrs, )
supermod.ProjectedCrs.subclass = ProjectedCrsSub
# end class ProjectedCrsSub


class ProjectedEpsgCrsSub(supermod.ProjectedEpsgCrs):
    def __init__(self, EpsgCode=None):
        super(ProjectedEpsgCrsSub, self).__init__(EpsgCode, )
supermod.ProjectedEpsgCrs.subclass = ProjectedEpsgCrsSub
# end class ProjectedEpsgCrsSub


class ProjectedGmlCrsSub(supermod.ProjectedGmlCrs):
    def __init__(self, GmlProjectedCrsDefinition=None):
        super(ProjectedGmlCrsSub, self).__init__(GmlProjectedCrsDefinition, )
supermod.ProjectedGmlCrs.subclass = ProjectedGmlCrsSub
# end class ProjectedGmlCrsSub


class ProjectedLocalAuthorityCrsSub(supermod.ProjectedLocalAuthorityCrs):
    def __init__(self, LocalAuthorityCrsName=None):
        super(ProjectedLocalAuthorityCrsSub, self).__init__(LocalAuthorityCrsName, )
supermod.ProjectedLocalAuthorityCrs.subclass = ProjectedLocalAuthorityCrsSub
# end class ProjectedLocalAuthorityCrsSub


class ProjectedUnknownCrsSub(supermod.ProjectedUnknownCrs):
    def __init__(self, Unknown=None):
        super(ProjectedUnknownCrsSub, self).__init__(Unknown, )
supermod.ProjectedUnknownCrs.subclass = ProjectedUnknownCrsSub
# end class ProjectedUnknownCrsSub


class ProjectedWktCrsSub(supermod.ProjectedWktCrs):
    def __init__(self, WellKnownText=None):
        super(ProjectedWktCrsSub, self).__init__(WellKnownText, )
supermod.ProjectedWktCrs.subclass = ProjectedWktCrsSub
# end class ProjectedWktCrsSub


class VerticalCrsSub(supermod.VerticalCrs):
    def __init__(self, uom=None, Direction=None, AbstractVerticalCrs=None):
        super(VerticalCrsSub, self).__init__(uom, Direction, AbstractVerticalCrs, )
supermod.VerticalCrs.subclass = VerticalCrsSub
# end class VerticalCrsSub


class VerticalEpsgCrsSub(supermod.VerticalEpsgCrs):
    def __init__(self, EpsgCode=None):
        super(VerticalEpsgCrsSub, self).__init__(EpsgCode, )
supermod.VerticalEpsgCrs.subclass = VerticalEpsgCrsSub
# end class VerticalEpsgCrsSub


class VerticalGmlCrsSub(supermod.VerticalGmlCrs):
    def __init__(self, GmlVerticalCrsDefinition=None):
        super(VerticalGmlCrsSub, self).__init__(GmlVerticalCrsDefinition, )
supermod.VerticalGmlCrs.subclass = VerticalGmlCrsSub
# end class VerticalGmlCrsSub


class VerticalLocalAuthorityCrsSub(supermod.VerticalLocalAuthorityCrs):
    def __init__(self, LocalAuthorityCrsName=None):
        super(VerticalLocalAuthorityCrsSub, self).__init__(LocalAuthorityCrsName, )
supermod.VerticalLocalAuthorityCrs.subclass = VerticalLocalAuthorityCrsSub
# end class VerticalLocalAuthorityCrsSub


class VerticalUnknownCrsSub(supermod.VerticalUnknownCrs):
    def __init__(self, Unknown=None):
        super(VerticalUnknownCrsSub, self).__init__(Unknown, )
supermod.VerticalUnknownCrs.subclass = VerticalUnknownCrsSub
# end class VerticalUnknownCrsSub


class VerticalWktCrsSub(supermod.VerticalWktCrs):
    def __init__(self, WellKnownText=None):
        super(VerticalWktCrsSub, self).__init__(WellKnownText, )
supermod.VerticalWktCrs.subclass = VerticalWktCrsSub
# end class VerticalWktCrsSub


class DataAssuranceRecordSub(supermod.DataAssuranceRecord):
    def __init__(self, PolicyId=None, PolicyName=None, ReferencedElementName=None, ReferencedElementUid=None, Origin=None, Conformance=None, Date=None, Comment=None, FailingRules=None, IndexRange=None, ReferencedData=None):
        super(DataAssuranceRecordSub, self).__init__(PolicyId, PolicyName, ReferencedElementName, ReferencedElementUid, Origin, Conformance, Date, Comment, FailingRules, IndexRange, ReferencedData, )
supermod.DataAssuranceRecord.subclass = DataAssuranceRecordSub
# end class DataAssuranceRecordSub


class FailingRuleSub(supermod.FailingRule):
    def __init__(self, RuleId=None, RuleName=None, Severity=None, FailingRuleExtensions=None):
        super(FailingRuleSub, self).__init__(RuleId, RuleName, Severity, FailingRuleExtensions, )
supermod.FailingRule.subclass = FailingRuleSub
# end class FailingRuleSub


class IndexRangeSub(supermod.IndexRange):
    def __init__(self, IndexMinimum=None, IndexMaximum=None):
        super(IndexRangeSub, self).__init__(IndexMinimum, IndexMaximum, )
supermod.IndexRange.subclass = IndexRangeSub
# end class IndexRangeSub


class AbstractGraphicalInformationSub(supermod.AbstractGraphicalInformation):
    def __init__(self, TargetObject=None):
        super(AbstractGraphicalInformationSub, self).__init__(TargetObject, )
supermod.AbstractGraphicalInformation.subclass = AbstractGraphicalInformationSub
# end class AbstractGraphicalInformationSub


class GraphicalInformationSetSub(supermod.GraphicalInformationSet):
    def __init__(self, GraphicalInformation=None):
        super(GraphicalInformationSetSub, self).__init__(GraphicalInformation, )
supermod.GraphicalInformationSet.subclass = GraphicalInformationSetSub
# end class GraphicalInformationSetSub


class AbsolutePressureSub(supermod.AbsolutePressure):
    def __init__(self, AbsolutePressure_member=None):
        super(AbsolutePressureSub, self).__init__(AbsolutePressure_member, )
supermod.AbsolutePressure.subclass = AbsolutePressureSub
# end class AbsolutePressureSub


class AbstractDQ_Result_TypeSub(supermod.AbstractDQ_Result_Type):
    def __init__(self, id=None, uuid=None):
        super(AbstractDQ_Result_TypeSub, self).__init__(id, uuid, )
supermod.AbstractDQ_Result_Type.subclass = AbstractDQ_Result_TypeSub
# end class AbstractDQ_Result_TypeSub


class CI_Series_TypeSub(supermod.CI_Series_Type):
    def __init__(self, id=None, uuid=None, name=None, issueIdentification=None, page=None):
        super(CI_Series_TypeSub, self).__init__(id, uuid, name, issueIdentification, page, )
supermod.CI_Series_Type.subclass = CI_Series_TypeSub
# end class CI_Series_TypeSub


class CI_OnlineResource_TypeSub(supermod.CI_OnlineResource_Type):
    def __init__(self, id=None, uuid=None, linkage=None, protocol=None, applicationProfile=None, name=None, description=None, function=None):
        super(CI_OnlineResource_TypeSub, self).__init__(id, uuid, linkage, protocol, applicationProfile, name, description, function, )
supermod.CI_OnlineResource_Type.subclass = CI_OnlineResource_TypeSub
# end class CI_OnlineResource_TypeSub


class CI_Address_TypeSub(supermod.CI_Address_Type):
    def __init__(self, id=None, uuid=None, deliveryPoint=None, city=None, administrativeArea=None, postalCode=None, country=None, electronicMailAddress=None):
        super(CI_Address_TypeSub, self).__init__(id, uuid, deliveryPoint, city, administrativeArea, postalCode, country, electronicMailAddress, )
supermod.CI_Address_Type.subclass = CI_Address_TypeSub
# end class CI_Address_TypeSub


class CI_Telephone_TypeSub(supermod.CI_Telephone_Type):
    def __init__(self, id=None, uuid=None, voice=None, facsimile=None):
        super(CI_Telephone_TypeSub, self).__init__(id, uuid, voice, facsimile, )
supermod.CI_Telephone_Type.subclass = CI_Telephone_TypeSub
# end class CI_Telephone_TypeSub


class CI_Contact_TypeSub(supermod.CI_Contact_Type):
    def __init__(self, id=None, uuid=None, phone=None, address=None, onlineResource=None, hoursOfService=None, contactInstructions=None):
        super(CI_Contact_TypeSub, self).__init__(id, uuid, phone, address, onlineResource, hoursOfService, contactInstructions, )
supermod.CI_Contact_Type.subclass = CI_Contact_TypeSub
# end class CI_Contact_TypeSub


class CI_ResponsibleParty_TypeSub(supermod.CI_ResponsibleParty_Type):
    def __init__(self, id=None, uuid=None, individualName=None, organisationName=None, positionName=None, contactInfo=None, role=None):
        super(CI_ResponsibleParty_TypeSub, self).__init__(id, uuid, individualName, organisationName, positionName, contactInfo, role, )
supermod.CI_ResponsibleParty_Type.subclass = CI_ResponsibleParty_TypeSub
# end class CI_ResponsibleParty_TypeSub


class CI_Date_TypeSub(supermod.CI_Date_Type):
    def __init__(self, id=None, uuid=None, date=None, dateType=None):
        super(CI_Date_TypeSub, self).__init__(id, uuid, date, dateType, )
supermod.CI_Date_Type.subclass = CI_Date_TypeSub
# end class CI_Date_TypeSub


class CI_Citation_TypeSub(supermod.CI_Citation_Type):
    def __init__(self, id=None, uuid=None, title=None, alternateTitle=None, date=None, edition=None, editionDate=None, identifier=None, citedResponsibleParty=None, presentationForm=None, series=None, otherCitationDetails=None, collectiveTitle=None, ISBN=None, ISSN=None):
        super(CI_Citation_TypeSub, self).__init__(id, uuid, title, alternateTitle, date, edition, editionDate, identifier, citedResponsibleParty, presentationForm, series, otherCitationDetails, collectiveTitle, ISBN, ISSN, )
supermod.CI_Citation_Type.subclass = CI_Citation_TypeSub
# end class CI_Citation_TypeSub


class MD_Identifier_TypeSub(supermod.MD_Identifier_Type):
    def __init__(self, id=None, uuid=None, authority=None, code=None):
        super(MD_Identifier_TypeSub, self).__init__(id, uuid, authority, code, )
supermod.MD_Identifier_Type.subclass = MD_Identifier_TypeSub
# end class MD_Identifier_TypeSub


class AbstractDQ_Element_TypeSub(supermod.AbstractDQ_Element_Type):
    def __init__(self, id=None, uuid=None, nameOfMeasure=None, measureIdentification=None, measureDescription=None, evaluationMethodType=None, evaluationMethodDescription=None, evaluationProcedure=None, dateTime=None, result=None, extensiontype_=None):
        super(AbstractDQ_Element_TypeSub, self).__init__(id, uuid, nameOfMeasure, measureIdentification, measureDescription, evaluationMethodType, evaluationMethodDescription, evaluationProcedure, dateTime, result, extensiontype_, )
supermod.AbstractDQ_Element_Type.subclass = AbstractDQ_Element_TypeSub
# end class AbstractDQ_Element_TypeSub


class AbstractDQ_PositionalAccuracy_TypeSub(supermod.AbstractDQ_PositionalAccuracy_Type):
    def __init__(self, id=None, uuid=None, nameOfMeasure=None, measureIdentification=None, measureDescription=None, evaluationMethodType=None, evaluationMethodDescription=None, evaluationProcedure=None, dateTime=None, result=None):
        super(AbstractDQ_PositionalAccuracy_TypeSub, self).__init__(id, uuid, nameOfMeasure, measureIdentification, measureDescription, evaluationMethodType, evaluationMethodDescription, evaluationProcedure, dateTime, result, )
supermod.AbstractDQ_PositionalAccuracy_Type.subclass = AbstractDQ_PositionalAccuracy_TypeSub
# end class AbstractDQ_PositionalAccuracy_TypeSub


class EX_VerticalExtent_TypeSub(supermod.EX_VerticalExtent_Type):
    def __init__(self, id=None, uuid=None, minimumValue=None, maximumValue=None, verticalCRS=None):
        super(EX_VerticalExtent_TypeSub, self).__init__(id, uuid, minimumValue, maximumValue, verticalCRS, )
supermod.EX_VerticalExtent_Type.subclass = EX_VerticalExtent_TypeSub
# end class EX_VerticalExtent_TypeSub


class EX_TemporalExtent_TypeSub(supermod.EX_TemporalExtent_Type):
    def __init__(self, id=None, uuid=None, extent=None):
        super(EX_TemporalExtent_TypeSub, self).__init__(id, uuid, extent, )
supermod.EX_TemporalExtent_Type.subclass = EX_TemporalExtent_TypeSub
# end class EX_TemporalExtent_TypeSub


class AbstractEX_GeographicExtent_TypeSub(supermod.AbstractEX_GeographicExtent_Type):
    def __init__(self, id=None, uuid=None, extentTypeCode=None):
        super(AbstractEX_GeographicExtent_TypeSub, self).__init__(id, uuid, extentTypeCode, )
supermod.AbstractEX_GeographicExtent_Type.subclass = AbstractEX_GeographicExtent_TypeSub
# end class AbstractEX_GeographicExtent_TypeSub


class EX_Extent_TypeSub(supermod.EX_Extent_Type):
    def __init__(self, id=None, uuid=None, description=None, geographicElement=None, temporalElement=None, verticalElement=None):
        super(EX_Extent_TypeSub, self).__init__(id, uuid, description, geographicElement, temporalElement, verticalElement, )
supermod.EX_Extent_Type.subclass = EX_Extent_TypeSub
# end class EX_Extent_TypeSub


class AngleTypeSub(supermod.AngleType):
    def __init__(self, valueOf_=None):
        super(AngleTypeSub, self).__init__(valueOf_, )
supermod.AngleType.subclass = AngleTypeSub
# end class AngleTypeSub


class RelatedTimeTypeSub(supermod.RelatedTimeType):
    def __init__(self, type_=None, href=None, role=None, arcrole=None, title=None, show=None, actuate=None, nilReason=None, owns='false', AbstractTimePrimitive=None, relativePosition=None):
        super(RelatedTimeTypeSub, self).__init__(type_, href, role, arcrole, title, show, actuate, nilReason, owns, AbstractTimePrimitive, relativePosition, )
supermod.RelatedTimeType.subclass = RelatedTimeTypeSub
# end class RelatedTimeTypeSub


class AbstractTimePrimitiveTypeSub(supermod.AbstractTimePrimitiveType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, relatedTime=None):
        super(AbstractTimePrimitiveTypeSub, self).__init__(id, description, descriptionReference, identifier, name, relatedTime, )
supermod.AbstractTimePrimitiveType.subclass = AbstractTimePrimitiveTypeSub
# end class AbstractTimePrimitiveTypeSub


class CodeWithAuthorityTypeSub(supermod.CodeWithAuthorityType):
    def __init__(self, codeSpace=None, valueOf_=None):
        super(CodeWithAuthorityTypeSub, self).__init__(codeSpace, valueOf_, )
supermod.CodeWithAuthorityType.subclass = CodeWithAuthorityTypeSub
# end class CodeWithAuthorityTypeSub


class DefinitionTypeSub(supermod.DefinitionType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, remarks=None, extensiontype_=None):
        super(DefinitionTypeSub, self).__init__(id, description, descriptionReference, identifier, name, remarks, extensiontype_, )
supermod.DefinitionType.subclass = DefinitionTypeSub
# end class DefinitionTypeSub


class IdentifiedObjectTypeSub(supermod.IdentifiedObjectType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, remarks=None, extensiontype_=None):
        super(IdentifiedObjectTypeSub, self).__init__(id, description, descriptionReference, identifier, name, remarks, extensiontype_, )
supermod.IdentifiedObjectType.subclass = IdentifiedObjectTypeSub
# end class IdentifiedObjectTypeSub


class AbstractCRSTypeSub(supermod.AbstractCRSType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, remarks=None, domainOfValidity=None, scope=None, extensiontype_=None):
        super(AbstractCRSTypeSub, self).__init__(id, description, descriptionReference, identifier, name, remarks, domainOfValidity, scope, extensiontype_, )
supermod.AbstractCRSType.subclass = AbstractCRSTypeSub
# end class AbstractCRSTypeSub


class GeodeticCRSTypeSub(supermod.GeodeticCRSType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, remarks=None, domainOfValidity=None, scope=None, ellipsoidalCS=None, cartesianCS=None, sphericalCS=None, geodeticDatum=None):
        super(GeodeticCRSTypeSub, self).__init__(id, description, descriptionReference, identifier, name, remarks, domainOfValidity, scope, ellipsoidalCS, cartesianCS, sphericalCS, geodeticDatum, )
supermod.GeodeticCRSType.subclass = GeodeticCRSTypeSub
# end class GeodeticCRSTypeSub


class AbstractStringArraySub(supermod.AbstractStringArray):
    def __init__(self, extensiontype_=None):
        super(AbstractStringArraySub, self).__init__(extensiontype_, )
supermod.AbstractStringArray.subclass = AbstractStringArraySub
# end class AbstractStringArraySub


class AbstractNumericArraySub(supermod.AbstractNumericArray):
    def __init__(self, extensiontype_=None):
        super(AbstractNumericArraySub, self).__init__(extensiontype_, )
supermod.AbstractNumericArray.subclass = AbstractNumericArraySub
# end class AbstractNumericArraySub


class AbstractIntegerArraySub(supermod.AbstractIntegerArray):
    def __init__(self, extensiontype_=None):
        super(AbstractIntegerArraySub, self).__init__(extensiontype_, )
supermod.AbstractIntegerArray.subclass = AbstractIntegerArraySub
# end class AbstractIntegerArraySub


class AbstractFloatingPointArraySub(supermod.AbstractFloatingPointArray):
    def __init__(self, extensiontype_=None):
        super(AbstractFloatingPointArraySub, self).__init__(extensiontype_, )
supermod.AbstractFloatingPointArray.subclass = AbstractFloatingPointArraySub
# end class AbstractFloatingPointArraySub


class AbstractBooleanArraySub(supermod.AbstractBooleanArray):
    def __init__(self, extensiontype_=None):
        super(AbstractBooleanArraySub, self).__init__(extensiontype_, )
supermod.AbstractBooleanArray.subclass = AbstractBooleanArraySub
# end class AbstractBooleanArraySub


class ProductFlowModelSub(supermod.ProductFlowModel):
    def __init__(self, Installation=None, ContextFacility=None, DTimStart=None, DTimEnd=None, ExistenceTime=None, DTimMin=None, DTimMax=None, Comment=None, ExternalConnect=None, Network=None):
        super(ProductFlowModelSub, self).__init__(Installation, ContextFacility, DTimStart, DTimEnd, ExistenceTime, DTimMin, DTimMax, Comment, ExternalConnect, Network, )
supermod.ProductFlowModel.subclass = ProductFlowModelSub
# end class ProductFlowModelSub


class ProductVolumeSub(supermod.ProductVolume):
    def __init__(self, Installation=None, ContextFacility=None, Kind=None, PeriodKind=None, DTimMin=None, DTimMax=None, DTimCurrent=None, CalculationMethod=None, Operator=None, Title=None, GeographicContext=None, IssueDate=None, IssuedBy=None, ApprovalDate=None, Approver=None, StandardTempPres=None, ProductFlowModel=None, DateTime=None, Facility=None, BusinessUnit=None):
        super(ProductVolumeSub, self).__init__(Installation, ContextFacility, Kind, PeriodKind, DTimMin, DTimMax, DTimCurrent, CalculationMethod, Operator, Title, GeographicContext, IssueDate, IssuedBy, ApprovalDate, Approver, StandardTempPres, ProductFlowModel, DateTime, Facility, BusinessUnit, )
supermod.ProductVolume.subclass = ProductVolumeSub
# end class ProductVolumeSub


class KindQualifiedStringSub(supermod.KindQualifiedString):
    def __init__(self, status=None):
        super(KindQualifiedStringSub, self).__init__(status, )
supermod.KindQualifiedString.subclass = KindQualifiedStringSub
# end class KindQualifiedStringSub


class IntegerQualifiedCountSub(supermod.IntegerQualifiedCount):
    def __init__(self, status=None):
        super(IntegerQualifiedCountSub, self).__init__(status, )
supermod.IntegerQualifiedCount.subclass = IntegerQualifiedCountSub
# end class IntegerQualifiedCountSub


class GeneralQualifiedMeasureSub(supermod.GeneralQualifiedMeasure):
    def __init__(self, status=None, componentReference=None, uom=None):
        super(GeneralQualifiedMeasureSub, self).__init__(status, componentReference, uom, )
supermod.GeneralQualifiedMeasure.subclass = GeneralQualifiedMeasureSub
# end class GeneralQualifiedMeasureSub


class FiberOpticalPathSub(supermod.FiberOpticalPath):
    def __init__(self, Inventory=None, OpticalPathNetwork=None, FacilityMapping=None, Defect=None, Otdr=None, InstallingVendor=None, FacilityIdentifier=None):
        super(FiberOpticalPathSub, self).__init__(Inventory, OpticalPathNetwork, FacilityMapping, Defect, Otdr, InstallingVendor, FacilityIdentifier, )
supermod.FiberOpticalPath.subclass = FiberOpticalPathSub
# end class FiberOpticalPathSub


class DtsInstalledSystemSub(supermod.DtsInstalledSystem):
    def __init__(self, DateMin=None, DateMax=None, OpticalPathLength=None, OpticalBudget=None, OpticalPathReference=None, InstrumentBoxReference=None, Comment=None, FacilityIdentifier=None, DtsCalibration=None):
        super(DtsInstalledSystemSub, self).__init__(DateMin, DateMax, OpticalPathLength, OpticalBudget, OpticalPathReference, InstrumentBoxReference, Comment, FacilityIdentifier, DtsCalibration, )
supermod.DtsInstalledSystem.subclass = DtsInstalledSystemSub
# end class DtsInstalledSystemSub


class DtsInstrumentBoxSub(supermod.DtsInstrumentBox):
    def __init__(self, SerialNumber=None, InternalOvenLocationNear=None, InternalOvenLocationFar=None, ReferenceCoilTemperature=None, Parameter=None, WarmupTime=None, StartupTime=None, FacilityIdentifier=None, DtsPatchCord=None, InstrumentCalibration=None, Instrument=None):
        super(DtsInstrumentBoxSub, self).__init__(SerialNumber, InternalOvenLocationNear, InternalOvenLocationFar, ReferenceCoilTemperature, Parameter, WarmupTime, StartupTime, FacilityIdentifier, DtsPatchCord, InstrumentCalibration, Instrument, )
supermod.DtsInstrumentBox.subclass = DtsInstrumentBoxSub
# end class DtsInstrumentBoxSub


class DasInstrumentBoxSub(supermod.DasInstrumentBox):
    def __init__(self, SerialNumber=None, Parameter=None, FacilityIdentifier=None, Instrument=None, FirmwareVersion=None, PatchCord=None, InstrumentBoxDescription=None):
        super(DasInstrumentBoxSub, self).__init__(SerialNumber, Parameter, FacilityIdentifier, Instrument, FirmwareVersion, PatchCord, InstrumentBoxDescription, )
supermod.DasInstrumentBox.subclass = DasInstrumentBoxSub
# end class DasInstrumentBoxSub


class DasExternalDatasetPartSub(EmlMixin, supermod.DasExternalDatasetPart):
    def __init__(self, Count=None, PathInExternalFile=None, StartIndex=None, EpcExternalPartReference=None, PartStartTime=None, PartEndTime=None):
        super(DasExternalDatasetPartSub, self).__init__(Count, PathInExternalFile, StartIndex, EpcExternalPartReference, PartStartTime, PartEndTime, )
        self.extensiontype_='prodml:DasExternalDatasetPart'
supermod.DasExternalDatasetPart.subclass = DasExternalDatasetPartSub
# end class DasExternalDatasetPartSub


class DasAcquisitionSub(supermod.DasAcquisition):
    def __init__(self, AcquisitionId=None, AcquisitionDescription=None, OpticalPath=None, DasInstrumentBox=None, FacilityId=None, VendorCode=None, PulseRate=None, PulseWidth=None, GaugeLength=None, GaugeLengthUnit=None, SpatialSamplingInterval=None, SpatialSamplingIntervalUnit=None, MinimumFrequency=None, MaximumFrequency=None, NumberOfLoci=None, StartLocusIndex=None, MeasurementStartTime=None, TriggeredMeasurement=None, PulseWidthUnit=None, Raw=None, Custom=None, Calibration=None, Processed=None):
        super(DasAcquisitionSub, self).__init__(AcquisitionId, AcquisitionDescription, OpticalPath, DasInstrumentBox, FacilityId, VendorCode, PulseRate, PulseWidth, GaugeLength, GaugeLengthUnit, SpatialSamplingInterval, SpatialSamplingIntervalUnit, MinimumFrequency, MaximumFrequency, NumberOfLoci, StartLocusIndex, MeasurementStartTime, TriggeredMeasurement, PulseWidthUnit, Raw, Custom, Calibration, Processed, )
supermod.DasAcquisition.subclass = DasAcquisitionSub
# end class DasAcquisitionSub


class VerticalCRSTypeSub(supermod.VerticalCRSType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, remarks=None, domainOfValidity=None, scope=None, verticalCS=None, verticalDatum=None):
        super(VerticalCRSTypeSub, self).__init__(id, description, descriptionReference, identifier, name, remarks, domainOfValidity, scope, verticalCS, verticalDatum, )
supermod.VerticalCRSType.subclass = VerticalCRSTypeSub
# end class VerticalCRSTypeSub


class AbstractCoordinateOperationTypeSub(supermod.AbstractCoordinateOperationType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, remarks=None, domainOfValidity=None, scope=None, operationVersion=None, coordinateOperationAccuracy=None, sourceCRS=None, targetCRS=None):
        super(AbstractCoordinateOperationTypeSub, self).__init__(id, description, descriptionReference, identifier, name, remarks, domainOfValidity, scope, operationVersion, coordinateOperationAccuracy, sourceCRS, targetCRS, )
supermod.AbstractCoordinateOperationType.subclass = AbstractCoordinateOperationTypeSub
# end class AbstractCoordinateOperationTypeSub


class AbstractGeneralDerivedCRSTypeSub(supermod.AbstractGeneralDerivedCRSType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, remarks=None, domainOfValidity=None, scope=None, conversion=None, extensiontype_=None):
        super(AbstractGeneralDerivedCRSTypeSub, self).__init__(id, description, descriptionReference, identifier, name, remarks, domainOfValidity, scope, conversion, extensiontype_, )
supermod.AbstractGeneralDerivedCRSType.subclass = AbstractGeneralDerivedCRSTypeSub
# end class AbstractGeneralDerivedCRSTypeSub


class ProjectedCRSTypeSub(supermod.ProjectedCRSType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, remarks=None, domainOfValidity=None, scope=None, conversion=None, baseGeodeticCRS=None, cartesianCS=None):
        super(ProjectedCRSTypeSub, self).__init__(id, description, descriptionReference, identifier, name, remarks, domainOfValidity, scope, conversion, baseGeodeticCRS, cartesianCS, )
supermod.ProjectedCRSType.subclass = ProjectedCRSTypeSub
# end class ProjectedCRSTypeSub


class EllipsoidTypeSub(supermod.EllipsoidType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, remarks=None, semiMajorAxis=None, secondDefiningParameter=None):
        super(EllipsoidTypeSub, self).__init__(id, description, descriptionReference, identifier, name, remarks, semiMajorAxis, secondDefiningParameter, )
supermod.EllipsoidType.subclass = EllipsoidTypeSub
# end class EllipsoidTypeSub


class PrimeMeridianTypeSub(supermod.PrimeMeridianType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, remarks=None, greenwichLongitude=None):
        super(PrimeMeridianTypeSub, self).__init__(id, description, descriptionReference, identifier, name, remarks, greenwichLongitude, )
supermod.PrimeMeridianType.subclass = PrimeMeridianTypeSub
# end class PrimeMeridianTypeSub


class AbstractDatumTypeSub(supermod.AbstractDatumType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, remarks=None, domainOfValidity=None, scope=None, anchorDefinition=None, realizationEpoch=None, extensiontype_=None):
        super(AbstractDatumTypeSub, self).__init__(id, description, descriptionReference, identifier, name, remarks, domainOfValidity, scope, anchorDefinition, realizationEpoch, extensiontype_, )
supermod.AbstractDatumType.subclass = AbstractDatumTypeSub
# end class AbstractDatumTypeSub


class GeodeticDatumTypeSub(supermod.GeodeticDatumType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, remarks=None, domainOfValidity=None, scope=None, anchorDefinition=None, realizationEpoch=None, primeMeridian=None, ellipsoid=None):
        super(GeodeticDatumTypeSub, self).__init__(id, description, descriptionReference, identifier, name, remarks, domainOfValidity, scope, anchorDefinition, realizationEpoch, primeMeridian, ellipsoid, )
supermod.GeodeticDatumType.subclass = GeodeticDatumTypeSub
# end class GeodeticDatumTypeSub


class CoordinateSystemAxisTypeSub(supermod.CoordinateSystemAxisType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, remarks=None, axisAbbrev=None, axisDirection=None, minimumValue=None, maximumValue=None, rangeMeaning=None):
        super(CoordinateSystemAxisTypeSub, self).__init__(id, description, descriptionReference, identifier, name, remarks, axisAbbrev, axisDirection, minimumValue, maximumValue, rangeMeaning, )
supermod.CoordinateSystemAxisType.subclass = CoordinateSystemAxisTypeSub
# end class CoordinateSystemAxisTypeSub


class AbstractCoordinateSystemTypeSub(supermod.AbstractCoordinateSystemType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, remarks=None, aggregationType=None, axis=None, extensiontype_=None):
        super(AbstractCoordinateSystemTypeSub, self).__init__(id, description, descriptionReference, identifier, name, remarks, aggregationType, axis, extensiontype_, )
supermod.AbstractCoordinateSystemType.subclass = AbstractCoordinateSystemTypeSub
# end class AbstractCoordinateSystemTypeSub


class EllipsoidalCSTypeSub(supermod.EllipsoidalCSType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, remarks=None, aggregationType=None, axis=None):
        super(EllipsoidalCSTypeSub, self).__init__(id, description, descriptionReference, identifier, name, remarks, aggregationType, axis, )
supermod.EllipsoidalCSType.subclass = EllipsoidalCSTypeSub
# end class EllipsoidalCSTypeSub


class StringExternalArraySub(supermod.StringExternalArray):
    def __init__(self, Values=None):
        super(StringExternalArraySub, self).__init__(Values, )
supermod.StringExternalArray.subclass = StringExternalArraySub
# end class StringExternalArraySub


class StringConstantArraySub(supermod.StringConstantArray):
    def __init__(self, Value=None, Count=None):
        super(StringConstantArraySub, self).__init__(Value, Count, )
supermod.StringConstantArray.subclass = StringConstantArraySub
# end class StringConstantArraySub


class IntegerRangeArraySub(supermod.IntegerRangeArray):
    def __init__(self, Count=None, Value=None):
        super(IntegerRangeArraySub, self).__init__(Count, Value, )
supermod.IntegerRangeArray.subclass = IntegerRangeArraySub
# end class IntegerRangeArraySub


class IntegerLatticeArraySub(supermod.IntegerLatticeArray):
    def __init__(self, StartValue=None, Offset=None):
        super(IntegerLatticeArraySub, self).__init__(StartValue, Offset, )
supermod.IntegerLatticeArray.subclass = IntegerLatticeArraySub
# end class IntegerLatticeArraySub


class IntegerExternalArraySub(EmlMixin, supermod.IntegerExternalArray):
    def __init__(self, NullValue=None, Values=None):
        super(IntegerExternalArraySub, self).__init__(NullValue, Values, )
supermod.IntegerExternalArray.subclass = IntegerExternalArraySub
# end class IntegerExternalArraySub


class IntegerConstantArraySub(supermod.IntegerConstantArray):
    def __init__(self, Value=None, Count=None):
        super(IntegerConstantArraySub, self).__init__(Value, Count, )
supermod.IntegerConstantArray.subclass = IntegerConstantArraySub
# end class IntegerConstantArraySub


class IntegerArrayFromBooleanMaskArraySub(supermod.IntegerArrayFromBooleanMaskArray):
    def __init__(self, TotalIndexCount=None, Mask=None):
        super(IntegerArrayFromBooleanMaskArraySub, self).__init__(TotalIndexCount, Mask, )
supermod.IntegerArrayFromBooleanMaskArray.subclass = IntegerArrayFromBooleanMaskArraySub
# end class IntegerArrayFromBooleanMaskArraySub


class FloatingPointLatticeArraySub(supermod.FloatingPointLatticeArray):
    def __init__(self, StartValue=None, Offset=None):
        super(FloatingPointLatticeArraySub, self).__init__(StartValue, Offset, )
supermod.FloatingPointLatticeArray.subclass = FloatingPointLatticeArraySub
# end class FloatingPointLatticeArraySub


class FloatingPointExternalArraySub(supermod.FloatingPointExternalArray):
    def __init__(self, Values=None, extensiontype_=None):
        super(FloatingPointExternalArraySub, self).__init__(Values, extensiontype_, )
supermod.FloatingPointExternalArray.subclass = FloatingPointExternalArraySub
# end class FloatingPointExternalArraySub


class FloatingPointConstantArraySub(supermod.FloatingPointConstantArray):
    def __init__(self, Value=None, Count=None):
        super(FloatingPointConstantArraySub, self).__init__(Value, Count, )
supermod.FloatingPointConstantArray.subclass = FloatingPointConstantArraySub
# end class FloatingPointConstantArraySub


class FloatExternalArraySub(supermod.FloatExternalArray):
    def __init__(self, Values=None):
        super(FloatExternalArraySub, self).__init__(Values, )
supermod.FloatExternalArray.subclass = FloatExternalArraySub
# end class FloatExternalArraySub


class DoubleExternalArraySub(supermod.DoubleExternalArray):
    def __init__(self, Values=None):
        super(DoubleExternalArraySub, self).__init__(Values, )
        self.extensiontype_='eml:DoubleExternalArray'
supermod.DoubleExternalArray.subclass = DoubleExternalArraySub
# end class DoubleExternalArraySub


class BooleanExternalArraySub(supermod.BooleanExternalArray):
    def __init__(self, Values=None):
        super(BooleanExternalArraySub, self).__init__(Values, )
supermod.BooleanExternalArray.subclass = BooleanExternalArraySub
# end class BooleanExternalArraySub


class BooleanConstantArraySub(supermod.BooleanConstantArray):
    def __init__(self, Value=None, Count=None):
        super(BooleanConstantArraySub, self).__init__(Value, Count, )
supermod.BooleanConstantArray.subclass = BooleanConstantArraySub
# end class BooleanConstantArraySub


class BooleanArrayFromIndexArraySub(supermod.BooleanArrayFromIndexArray):
    def __init__(self, Count=None, Indices=None, IndexIsTrue=None):
        super(BooleanArrayFromIndexArraySub, self).__init__(Count, Indices, IndexIsTrue, )
supermod.BooleanArrayFromIndexArray.subclass = BooleanArrayFromIndexArraySub
# end class BooleanArrayFromIndexArraySub


class VerticalDatumTypeSub(supermod.VerticalDatumType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, remarks=None, domainOfValidity=None, scope=None, anchorDefinition=None, realizationEpoch=None):
        super(VerticalDatumTypeSub, self).__init__(id, description, descriptionReference, identifier, name, remarks, domainOfValidity, scope, anchorDefinition, realizationEpoch, )
supermod.VerticalDatumType.subclass = VerticalDatumTypeSub
# end class VerticalDatumTypeSub


class VerticalCSTypeSub(supermod.VerticalCSType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, remarks=None, aggregationType=None, axis=None):
        super(VerticalCSTypeSub, self).__init__(id, description, descriptionReference, identifier, name, remarks, aggregationType, axis, )
supermod.VerticalCSType.subclass = VerticalCSTypeSub
# end class VerticalCSTypeSub


class SphericalCSTypeSub(supermod.SphericalCSType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, remarks=None, aggregationType=None, axis=None):
        super(SphericalCSTypeSub, self).__init__(id, description, descriptionReference, identifier, name, remarks, aggregationType, axis, )
supermod.SphericalCSType.subclass = SphericalCSTypeSub
# end class SphericalCSTypeSub


class CartesianCSTypeSub(supermod.CartesianCSType):
    def __init__(self, id=None, description=None, descriptionReference=None, identifier=None, name=None, remarks=None, aggregationType=None, axis=None):
        super(CartesianCSTypeSub, self).__init__(id, description, descriptionReference, identifier, name, remarks, aggregationType, axis, )
supermod.CartesianCSType.subclass = CartesianCSTypeSub
# end class CartesianCSTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DasAcquisition'
        rootClass = supermod.DasAcquisition
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:prodml="http://www.energistics.org/energyml/data/prodmlv2"',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DasAcquisition'
        rootClass = supermod.DasAcquisition
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DasAcquisition'
        rootClass = supermod.DasAcquisition
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='xmlns:prodml="http://www.energistics.org/energyml/data/prodmlv2"')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DasAcquisition'
        rootClass = supermod.DasAcquisition
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from DasAcquisition import *\n\n')
        sys.stdout.write('import DasAcquisition as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
