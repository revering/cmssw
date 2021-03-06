import FWCore.ParameterSet.Config as cms

from SimG4Core.Application.hectorParameter_cfi import *

from IOMC.EventVertexGenerators.VtxSmearedParameters_cfi import Realistic25ns13TeV2016CollisionVtxSmearingParameters
from IOMC.EventVertexGenerators.VtxSmearedParameters_cfi import Realistic25ns13TeVEarly2017CollisionVtxSmearingParameters
from IOMC.EventVertexGenerators.VtxSmearedParameters_cfi import Realistic25ns13TeVEarly2018CollisionVtxSmearingParameters


baseHectorParameters = cms.PSet(
                TransportMethod = cms.string('Hector'),
                ApplyZShift = cms.bool(True)
)

Totem_PreTS2_2016 = cms.PSet(
        #TotemBeamLine = cms.bool(True),
        Beam1Filename = cms.string('SimTransport/PPSProtonTransport/data/LHCB1_Beta0.40_6.5TeV_CR191.541_PreTS2_TOTEM.tfs'),
        Beam2Filename = cms.string('SimTransport/PPSProtonTransport/data/LHCB2_Beta0.40_6.5TeV_CR179.394_PreTS2_TOTEM.tfs'),
        halfCrossingAngleSector45  = cms.double(191.541), #in mrad
        halfCrossingAngleSector56  = cms.double(179.394), #in mrad
        BeamEnergyDispersion = cms.double(1.11e-4),     ## beam energy dispersion (GeV); if =0.0 the default(=0.79) is used
        BeamDivergenceX = cms.double(135.071),     ## x angle dispersion at IP (urad); if =0.0 the default(=30.23) is used
        BeamDivergenceY = cms.double(135.071),      ## y angle dispersion at IP (urad); if =0.0 the default(=30.23) is used
        BeamSigmaX  = cms.double(54.03),
        BeamSigmaY  = cms.double(54.03),
        BeamEnergy = cms.double(6500.0),
        BeamXatIP      = cms.untracked.double(0.),
        BeamYatIP      = cms.untracked.double(0.),
        VtxMeanX  = Realistic25ns13TeV2016CollisionVtxSmearingParameters.X0,
        VtxMeanY  = Realistic25ns13TeV2016CollisionVtxSmearingParameters.Y0,
        VtxMeanZ  = Realistic25ns13TeV2016CollisionVtxSmearingParameters.Z0
)
Validated_PreTS2_2016 = cms.PSet(
        #TotemBeamLine = cms.bool(False),
        Beam1Filename = cms.string('SimTransport/PPSProtonTransport/data/LHCB1_Beta0.40_6.5TeV_CR191.541_PreTS2.tfs'),
        Beam2Filename = cms.string('SimTransport/PPSProtonTransport/data/LHCB2_Beta0.40_6.5TeV_CR179.394_PreTS2.tfs'),
        halfCrossingAngleSector45  = cms.double(191.541), #in mrad
        halfCrossingAngleSector56  = cms.double(179.394), #in mrad
        BeamEnergyDispersion = cms.double(1.11e-4),     ## beam energy dispersion (GeV); if =0.0 the default(=0.79) is used
        BeamDivergenceX = cms.double(135.071),     ## x angle dispersion at IP (urad); if =0.0 the default(=30.23) is used
        BeamDivergenceY = cms.double(135.071),      ## y angle dispersion at IP (urad); if =0.0 the default(=30.23) is used
        BeamSigmaX  = cms.double(54.03),
        BeamSigmaY  = cms.double(54.03),
        BeamEnergy = cms.double(6500.0),
        #BeamXatIP = cms.untracked.double(0.499), # if not given, will take the CMS average vertex position
        #BeamYatIP = cms.untracked.double(-0.190), # if not given, will take the CMS average vertex position
        VtxMeanX  = Realistic25ns13TeV2016CollisionVtxSmearingParameters.X0,
        VtxMeanY  = Realistic25ns13TeV2016CollisionVtxSmearingParameters.Y0,
        VtxMeanZ  = Realistic25ns13TeV2016CollisionVtxSmearingParameters.Z0
)

# Beam parameter for Nominal 2017 optics
Nominal_2017_beta40cm = cms.PSet(
        #TotemBeamLine = cms.bool(False),
        Beam1Filename = cms.string('SimTransport/PPSProtonTransport/data/LHCB1_Beta0.40_6.5TeV_CR150_Nominal_2017.tfs'),
        Beam2Filename = cms.string('SimTransport/PPSProtonTransport/data/LHCB2_Beta0.40_6.5TeV_CR150_Nominal_2017.tfs'),
        halfCrossingAngleSector45  = cms.double(150.), #in mrad
        halfCrossingAngleSector56  = cms.double(150.), #in mrad
        BeamEnergyDispersion = cms.double(1.11e-4),     ## beam energy dispersion (GeV); if =0.0 the default(=0.79) is used
        BeamDivergenceX = cms.double(30.04),     ## x angle dispersion at IP (urad); if =0.0 the default(=30.23) is used
        BeamDivergenceY = cms.double(30.04),      ## y angle dispersion at IP (urad); if =0.0 the default(=30.23) is used
        BeamSigmaX  = cms.double(12.01),
        BeamSigmaY  = cms.double(12.01),
        BeamEnergy = cms.double(6500.0),
        BeamXatIP      = cms.untracked.double(0.),
        BeamYatIP      = cms.untracked.double(0.),
        VtxMeanX  = Realistic25ns13TeVEarly2017CollisionVtxSmearingParameters.X0,
        VtxMeanY  = Realistic25ns13TeVEarly2017CollisionVtxSmearingParameters.Y0,
        VtxMeanZ  = Realistic25ns13TeVEarly2017CollisionVtxSmearingParameters.Z0
)
#
Nominal_2017_beta30cm = cms.PSet(
        #TotemBeamLine = cms.bool(False),
        Beam1Filename = cms.string('SimTransport/PPSProtonTransport/data/LHCB1_Beta0.30_6.5TeV_CR175_Nominal_2017.tfs'),
        Beam2Filename = cms.string('SimTransport/PPSProtonTransport/data/LHCB2_Beta0.30_6.5TeV_CR175_Nominal_2017.tfs'),
        halfCrossingAngleSector45  = cms.double(175.), #in mrad
        halfCrossingAngleSector56  = cms.double(175.), #in mrad
        BeamEnergyDispersion = cms.double(1.11e-4),     ## beam energy dispersion (GeV); if =0.0 the default(=0.79) is used
        BeamDivergenceX = cms.double(34.68),     ## x angle dispersion at IP (urad); if =0.0 the default(=30.23) is used
        BeamDivergenceY = cms.double(34.68),      ## y angle dispersion at IP (urad); if =0.0 the default(=30.23) is used
        BeamSigmaX  = cms.double(10.40),
        BeamSigmaY  = cms.double(10.40),
        BeamEnergy = cms.double(6500.0),
        BeamXatIP      = cms.untracked.double(0.),
        BeamYatIP      = cms.untracked.double(0.),
        VtxMeanX  = Realistic25ns13TeVEarly2017CollisionVtxSmearingParameters.X0,
        VtxMeanY  = Realistic25ns13TeVEarly2017CollisionVtxSmearingParameters.Y0,
        VtxMeanZ  = Realistic25ns13TeVEarly2017CollisionVtxSmearingParameters.Z0
)
# Beam parametes for Nominal 2016
Nominal_2016 = cms.PSet(
        #TotemBeamLine = cms.bool(False),
        Beam1Filename = cms.string('SimTransport/PPSProtonTransport/data/LHCB1_Beta0.40_6.5TeV_CR185_Nominal_2016.tfs'),
        Beam2Filename = cms.string('SimTransport/PPSProtonTransport/data/LHCB2_Beta0.40_6.5TeV_CR185_Nominal_2016.tfs'),
        hasfCrossingAngleSector45  = cms.double(185.), #in mrad / Beam 1
        halfCrossingAngleSector56  = cms.double(185.), #in mrad / Beam 2
        BeamEnergyDispersion = cms.double(1.11e-4),     ## beam energy dispersion (GeV); if =0.0 the default(=0.79) is used
        BeamDivergenceX = cms.double(35.54),     ## x angle dispersion at IP (urad); if =0.0 the default(=30.23) is used
        BeamDivergenceY = cms.double(35.54),      ## y angle dispersion at IP (urad); if =0.0 the default(=30.23) is used
        BeamSigmaX  = cms.double(14.22),
        BeamSigmaY  = cms.double(14.22),
        BeamEnergy = cms.double(6500.0),
        BeamXatIP      = cms.untracked.double(0.),
        BeamYatIP      = cms.untracked.double(0.),
        VtxMeanX  = Realistic25ns13TeV2016CollisionVtxSmearingParameters.X0,
        VtxMeanY  = Realistic25ns13TeV2016CollisionVtxSmearingParameters.Y0,
        VtxMeanZ  = Realistic25ns13TeV2016CollisionVtxSmearingParameters.Z0
)

hector_2016 = cms.PSet(
              baseHectorParameters,
              Validated_PreTS2_2016,
)

hector_2017_beta40  = cms.PSet(
              baseHectorParameters,
              Nominal_2017_beta40cm
)

hector_2017_beta30  = cms.PSet(
              baseHectorParameters,
              Nominal_2017_beta30cm
)
