evgenConfig.description = "POWHEG+Pythia8 Z->eeH production and AU2 CT10 tune"
evgenConfig.keywords = ["ZH" ,"NLO", "Powheg", "pythia8", "higgs","electron"]
evgenConfig.inputfilecheck = 'ZeeH_SM_M125' 

include("MC12JobOptions/PowhegPythia8_AU2_CT10_Common.py")
include("MC12JobOptions/Pythia8_Photos.py")

topAlg.Pythia8.Commands += [
                            '25:onMode = off',
                            '25:onIfMatch = 15 15'
                            ]
