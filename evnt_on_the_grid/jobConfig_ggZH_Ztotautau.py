evgenConfig.description = "POWHEG+Pythia8 Z->tautauH production and AU2 CT10 tune"
evgenConfig.keywords = ["ZH" ,"NLO", "Powheg", "pythia8", "higgs","tau"]
evgenConfig.inputfilecheck = 'powheg.300003.ZtautauH_SM_M125' 

include("MC12JobOptions/PowhegPythia8_AU2_CT10_Common.py")
include("MC12JobOptions/Pythia8_Photos.py")

topAlg.Pythia8.Commands += [
                            '25:onMode = off',
                            '25:onIfMatch = 15 15'
                            ]