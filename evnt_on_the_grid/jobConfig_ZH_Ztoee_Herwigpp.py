evgenConfig.description = "POWHEG+Herwig++ Z->eeH production and AU2 CT10 tune"
evgenConfig.keywords = ["ZH" ,"NLO", "Powheg", "herwig", "higgs","electron"]
evgenConfig.inputfilecheck = 'powheg.400001.ZeeH_SM_M125' 

include("MC12JobOptions/Herwigpp_UEEE3_CTEQ6L1_CT10ME_LHEF_Common.py")
cmds = """ 
set /Herwig/Particles/h0/h0->W+,W-;:OnOff 0 
set /Herwig/Particles/h0/h0->Z0,Z0;:OnOff 0 
set /Herwig/Particles/h0/h0->b,bbar;:OnOff 0
set /Herwig/Particles/h0/h0->c,cbar;:OnOff 0 
set /Herwig/Particles/h0/h0->g,g;:OnOff 0
set /Herwig/Particles/h0/h0->gamma,gamma;:OnOff 0 
set /Herwig/Particles/h0/h0->mu-,mu+;:OnOff 0
set /Herwig/Particles/h0/h0->t,tbar;:OnOff 0 
set /Herwig/Particles/h0/h0->tau-,tau+;:OnOff 1 
"""
topAlg.Herwigpp.Commands += cmds.splitlines()
