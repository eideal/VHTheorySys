evgenConfig.description = "POWHEG+Pythia8 Z->ee,H->tautau->hh production and AU2 CT10 tune"
evgenConfig.keywords = ["ZH" ,"NLO", "Powheg", "pythia8", "higgs","electron","hadronic"]
evgenConfig.inputfilecheck = 'powheg.300001.HadHad.ZeeH_SM_M125' 

include("MC12JobOptions/PowhegPythia8_AU2_CT10_Common.py")
include("MC12JobOptions/Pythia8_Photos.py")

topAlg.Pythia8.Commands += [
                            '25:onMode = off',
                            '25:onIfMatch = 15 15'
                            ]

# ... Filter H->tautau->Children
include("MC12JobOptions/XtoVVDecayFilter.py")
topAlg.XtoVVDecayFilter.PDGGrandParent = 25
topAlg.XtoVVDecayFilter.PDGParent = 15
topAlg.XtoVVDecayFilter.StatusParent = 2
topAlg.XtoVVDecayFilter.PDGChild1 = [111,130,211,221,223,310,311,321,323]
topAlg.XtoVVDecayFilter.PDGChild2 = [111,130,211,221,223,310,311,321,323]
