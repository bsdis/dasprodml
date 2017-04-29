#!/bin/bash
# This script creates python modules with classes representing prodml schemas.
generateDS.py -o dasprodml/DasAcquisition.py -s dasprodml/DasAcquisitionSub.py --super=dasprodml.DasAcquisition -m ./energistics/prodml/v2.0/xsd_schemas/DasAcquisition.xsd
generateDS.py -o dasprodml/FiberOpticalPath.py -s dasprodml/FiberOpticalPathSub.py --super=dasprodml.FiberOpticalPath -m ./energistics/prodml/v2.0/xsd_schemas/FiberOpticalPath.xsd
