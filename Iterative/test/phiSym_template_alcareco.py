import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras
process = cms.Process("PHASEHFX",eras.Run2_2018)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32 (-1)
)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000
process.MessageLogger.cerr.default.limit = 1000

process.load('Configuration.StandardSequences.Services_cff')
process.load("Configuration.StandardSequences.GeometryDB_cff")


#--- Global Tag conditions                                                                                                                                                      
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = '101X_dataRun2_Prompt_v9'


process.phaseHF = cms.EDAnalyzer ("phiSym",
                                  textFile = cms.untracked.string(OUTPUTFILE2),
                                  hfreco =  cms.InputTag("hfreco"),
                                  hbhereco = cms.InputTag("hbhereco")
 )

process.TFileService = cms.Service("TFileService",
    fileName = cms.string(OUTPUTFILE1),
)

#----------------------------
# Paths/Sequences Definitions
#----------------------------
process.p = cms.Path(
    process.phaseHF
)

process.source = cms.Source ("PoolSource" ,
                             fileNames=cms.untracked.vstring(INPUTLIST)
)
