evgenConfig.description = "POWHEG+Jimmy W->eH production and AUET2 CT10 tune"
evgenConfig.keywords = ["WH" ,"NLO", "Powheg", "higgs","electron"]
evgenConfig.inputfilecheck = 'powheg.500001.WeH_SM_M125' 

include("MC12JobOptions/PowhegJimmy_AUET2_CT10_Common.py")
evgenConfig.generators += ["Powheg"]

# ID=1-6 for dd,...,tt, 7-9 for ee,mumu,tautau, 10,11,12 for WW,ZZ,gamgam
# iproc=-100-ID (lhef=-100)
topAlg.Herwig.HerwigCommand += [ "iproc -109" ]
include("MC12JobOptions/Jimmy_Photos.py" )
include("MC12JobOptions/Jimmy_Tauola.py" )
