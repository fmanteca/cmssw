import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018
process = cms.Process("AlCaHEMuon",Run2_2018)

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.AlCaRecoStreams_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.autoCond import autoCond
process.GlobalTag.globaltag=autoCond['run2_data']

process.load("RecoLocalCalo.EcalRecAlgos.EcalSeverityLevelESProducer_cfi")

if hasattr(process,'MessageLogger'):
    process.MessageLogger.HBHEMuon=dict()

process.maxEvents = cms.untracked.PSet( 
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
        'file:/eos/cms/store/group/dpg_hcal/comm_hcal/AmanKaur/HLTPhysics/RawtoReco_HLTPhysics/210910_053130/0000/RECO_RAW2DIGI_L1Reco_RECO_ALCA_1.root',
        'file:/eos/cms/store/group/dpg_hcal/comm_hcal/AmanKaur/HLTPhysics/RawtoReco_HLTPhysics/210910_053130/0000/RECO_RAW2DIGI_L1Reco_RECO_ALCA_2.root',
        )
)

process.ALCARECOStreamHcalCalHEMuon = cms.OutputModule("PoolOutputModule",
                                                         SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOHcalCalHEMuonProducerFilter')
        ),
                                                         dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('ALCARECOHcalCalHEMuonProducerFilter')
        ),
                                                         eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
                                                         outputCommands = process.OutALCARECOHcalCalHEMuonProducerFilter.outputCommands,
                                                         fileName = cms.untracked.string('OutputHEMuonProducerFilter.root'),
                                      )

process.alcaHcalHBHEMuonProducer.triggers = []

# Path and EndPath definitions
process.endjob_step = cms.EndPath(process.endOfProcess)
process.ALCARECOStreamHcalCalHEMuonProducerFilterOutPath = cms.EndPath(process.ALCARECOStreamHcalCalHEMuon)

# Schedule definition
process.schedule = cms.Schedule(process.pathALCARECOHcalCalHEMuonProducerFilter,process.endjob_step,process.ALCARECOStreamHcalCalHEMuonProducerFilterOutPath)
