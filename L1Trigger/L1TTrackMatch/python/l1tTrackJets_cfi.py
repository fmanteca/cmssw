import FWCore.ParameterSet.Config as cms

l1tTrackJets = cms.EDProducer('L1TrackJetProducer',
	L1TrackInputTag= cms.InputTag("l1tTTTracksFromTrackletEmulation", "Level1TTTracks"),
	L1PVertexCollection = cms.InputTag("l1tVertexProducer", "l1vertices"),
	MaxDzTrackPV = cms.double( 1.0 ),
	trk_zMax = cms.double (15.) ,    # maximum track z
	trk_ptMax = cms.double(200.),    # maximumum track pT before saturation [GeV]
	trk_ptMin = cms.double(3.0),     # minimum track pt [GeV]
   	trk_etaMax = cms.double(2.4),    # maximum track eta
	nStubs4PromptChi2=cms.double(5.0), #Prompt track quality flags for loose/tight
        nStubs4PromptBend=cms.double(1.7),
        nStubs5PromptChi2=cms.double(2.75),
        nStubs5PromptBend=cms.double(3.5),
	trk_nPSStubMin=cms.int32(-1),    # minimum PS stubs, -1 means no cut
	minTrkJetpT=cms.double(-1.),     # min track jet pt to be considered for most energetic zbin finding 
	etaBins=cms.int32(24),
	phiBins=cms.int32(27),
	zBins=cms.int32(1),
	d0_cutNStubs4=cms.double(-1),
	d0_cutNStubs5=cms.double(-1),
	lowpTJetMinTrackMultiplicity=cms.int32(2),
	highpTJetMinTrackMultiplicity=cms.int32(3),
	displaced=cms.bool(False), #Flag for displaced tracks
	nStubs4DisplacedChi2=cms.double(5.0), #Displaced track quality flags for loose/tight
	nStubs4DisplacedBend=cms.double(1.7),
	nStubs5DisplacedChi2=cms.double(2.75),
	nStubs5DisplacedBend=cms.double(3.5),
        nDisplacedTracks=cms.int32(2)
)

l1tTrackJetsExtended = cms.EDProducer('L1TrackJetProducer',
	L1TrackInputTag= cms.InputTag("l1tTTTracksFromExtendedTrackletEmulation", "Level1TTTracks"),
	L1PVertexCollection = cms.InputTag("l1tVertexProducer", "l1vertices"),
	MaxDzTrackPV = cms.double( 5.0 ), # tracks with dz(trk,PV)>cut excluded
	trk_zMax = cms.double (15.) ,    # max track z
	trk_ptMax = cms.double(200.),    # maxi track pT before saturation
	trk_ptMin = cms.double(3.0),     # min track pt 
   	trk_etaMax = cms.double(2.4),    # max track eta
        nStubs4PromptChi2=cms.double(5.0), #Prompt track quality flags for loose/tight
        nStubs4PromptBend=cms.double(1.7),
        nStubs5PromptChi2=cms.double(2.75),
        nStubs5PromptBend=cms.double(3.5),
	trk_nPSStubMin=cms.int32(-1),    # min # PS stubs, -1 means no cut
	minTrkJetpT=cms.double(5.),      # min track jet pt to be considered for most energetic zbin finding
	etaBins=cms.int32(24), #number of eta bins
	phiBins=cms.int32(27), #number of phi bins
	zBins=cms.int32(1),    #number of z bins
	d0_cutNStubs4=cms.double(-1),    # -1 excludes nstub=4 from disp tag
	d0_cutNStubs5=cms.double(0.22),  # -1 excludes nstub>4 from disp tag
	lowpTJetMinTrackMultiplicity=cms.int32(2),  #used only on zbin finding
	highpTJetMinTrackMultiplicity=cms.int32(3), #used only on zbin finding
	displaced=cms.bool(True), #Flag for displaced tracks
	nStubs4DisplacedChi2=cms.double(3.3), #Disp tracks selection [trk<cut]
	nStubs4DisplacedBend=cms.double(2.3),
	nStubs5DisplacedChi2=cms.double(11.3),
	nStubs5DisplacedBend=cms.double(9.8),
        nDisplacedTracks=cms.int32(3) #min Ntracks to tag a jet as displaced
)


# selection as presented in the GTT for reference
# d0_cutNStubs4=cms.double(-1),    # -1 excludes nstub=4 from disp tag
# d0_cutNStubs5=cms.double(0.22),  # -1 excludes nstub>4 from disp tag
# lowpTJetMinTrackMultiplicity=cms.int32(2),  #used only on zbin finding
# highpTJetMinTrackMultiplicity=cms.int32(3), #used only on zbin finding
# displaced=cms.bool(True), #Flag for displaced tracks
# nStubs4DisplacedChi2=cms.double(3.3), #Disp tracks selection [trk<cut]
# nStubs4Displacedbend=cms.double(2.3),
# nStubs5DisplacedChi2=cms.double(11.3),
# nStubs5Displacedbend=cms.double(9.8),
# nDisplacedTracks=cms.int32(3) #min Ntracks to tag a jet as displaced
