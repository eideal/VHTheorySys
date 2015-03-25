evgenConfig.description = "POWHEG+Pythia8 W->enuH production and AU2 CT10 tune"
evgenConfig.keywords = ["WH" ,"NLO", "Powheg", "pythia8", "higgs","electron"]
evgenConfig.inputfilecheck = 'WeH_SM_M125' 

include("MC12JobOptions/PowhegPythia8_AU2_CT10_Common.py")
include("MC12JobOptions/Pythia8_Photos.py")

topAlg.Pythia8.Commands += [
                            '25:onMode = off',
                            '25:onIfMatch = 15 15'
                            ]
