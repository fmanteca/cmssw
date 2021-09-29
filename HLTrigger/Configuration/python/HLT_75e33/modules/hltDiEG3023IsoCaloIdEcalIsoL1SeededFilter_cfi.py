import FWCore.ParameterSet.Config as cms

hltDiEG3023IsoCaloIdEcalIsoL1SeededFilter = cms.EDFilter("HLTEgammaGenericQuadraticEtaFilter",
    absEtaLowEdges = cms.vdouble(0.0, 1.0, 1.479, 2.1),
    candTag = cms.InputTag("hltDiEG3023IsoCaloIdHEL1SeededFilter"),
    doRhoCorrection = cms.bool(False),
    effectiveAreas = cms.vdouble(0.2, 0.2, 0.25, 0.3),
    energyLowEdges = cms.vdouble(0.0),
    etaBoundaryEB12 = cms.double(1.0),
    etaBoundaryEE12 = cms.double(2.1),
    l1EGCand = cms.InputTag("hltEgammaCandidatesL1Seeded"),
    lessThan = cms.bool(True),
    ncandcut = cms.int32(2),
    rhoMax = cms.double(99999999.0),
    rhoScale = cms.double(1.0),
    rhoTag = cms.InputTag("hltFixedGridRhoFastjetAllCaloForEGamma"),
    saveTags = cms.bool(True),
    thrOverE2EB1 = cms.vdouble(0.0),
    thrOverE2EB2 = cms.vdouble(0.0),
    thrOverE2EE1 = cms.vdouble(0.0),
    thrOverE2EE2 = cms.vdouble(0.0),
    thrOverEEB1 = cms.vdouble(0.02),
    thrOverEEB2 = cms.vdouble(0.02),
    thrOverEEE1 = cms.vdouble(0.02),
    thrOverEEE2 = cms.vdouble(0.02),
    thrRegularEB1 = cms.vdouble(12),
    thrRegularEB2 = cms.vdouble(12),
    thrRegularEE1 = cms.vdouble(12),
    thrRegularEE2 = cms.vdouble(12),
    useEt = cms.bool(True),
    varTag = cms.InputTag("hltEgammaEcalPFClusterIsoL1Seeded")
)
