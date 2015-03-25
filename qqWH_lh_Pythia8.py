import ROOT, sys, math

## Enable the reading of vectors
ROOT.gROOT.ProcessLine(\
    "#include <vector>\n\
    #ifdef __MAKECINT__\n\
    #pragma link C++ class vector<vector<float> >+;\n\
    #pragma link C++ class vector<vector<int> >+;\n\
    #endif")

## Prepare output file
out_ff = ROOT.TFile('histograms.root', 'RECREATE')
out_ff.cd()

## Get access to the trees in the files
print 'Creating TChain...'
tt = ROOT.TChain('truth')

input_files = sys.argv[-1].split(',')
for input_file in input_files:
    print 'Adding file %s to TChain' % input_file
    tt.Add(input_file)


# Define some histograms to write into ROOT file
h_eventcount = ROOT.TH1F('EventCount', 'EventCount', 1, 0, 1)
h_eventcount.SetXTitle('Event Count')
h_leppt = ROOT.TH1F('LeppT', 'LeppT',20, 0, 200000)
h_taupt = ROOT.TH1F('TaupT', 'TaupT',20, 0, 200000)
h_HiggsPt = ROOT.TH1F('H_pT', 'H_pT', 35, 0,350000)


## Print GetEntries()
print 'The number of entries in the tree is %d' % tt.GetEntries()

## Event loop
print 'Starting Event Loop ...'
n = tt.GetEntries()
event_count = 0


for i in range(n):
    tt.GetEntry(i)

    #Define some lists to store the indices of taus and leptons
    elecs = []
    muons = []
    tau_hads = []

    for p in range(tt.mc_n):

      # Taus
      if abs(tt.mc_pdgId[p]) == 15 and tt.mc_status[p] == 2:
        tau_had = False
        child_length = len(tt.mc_child_index[p])
        if child_length != 0:
          for child in range(child_length):
            childId = tt.mc_pdgId[tt.mc_child_index[p][child]]
            if not tt.mc_status[tt.mc_child_index[p][child]] == 1: continue
            if abs(childId) == 211 or abs(childId) == 321: 
              tau_had = True
        if tau_had == True: tau_hads.append(p)

      # Electrons
      if abs(tt.mc_pdgId[p]) == 11 and tt.mc_status[p] == 1:
        ElecPt = tt.mc_pt[p]
        ElecEta = abs(tt.mc_eta[p])
        if ElecPt > 10000:
          if (ElecEta < 1.37 or ElecEta > 1.52) and ElecEta < 2.47:
            elecs.append(p)

      # Muons
      if abs(tt.mc_pdgId[p]) == 13 and tt.mc_status[p] == 1:
        MuonPt = tt.mc_pt[p]
        MuonEta = abs(tt.mc_eta[p])
        if MuonPt > 6000:
          if MuonEta < 2.5:
            muons.append(p)
        
    # Hadronic tau cuts
    tauPass = []
    for t in tau_hads:
      #Define a list of neutrinos for each tau
      neu_vec = []
      tau_vec = ROOT.TLorentzVector()
      tau_vec.SetPtEtaPhiE(tt.mc_pt[t], tt.mc_eta[t], tt.mc_phi[t], tt.mc_E[t])
      child_length = len(tt.mc_child_index[t])
      if child_length != 0:
        for child in range(child_length):
          childIndex = tt.mc_child_index[t][child]
          childId = abs(tt.mc_pdgId[tt.mc_child_index[t][child]])
          if not tt.mc_status[tt.mc_child_index[t][child]] == 1: continue
          if childId == 12 or childId == 14 or childId == 16:
            neu_vec.append(ROOT.TLorentzVector())
            neu_vec[0].SetPtEtaPhiE(tt.mc_pt[childIndex], tt.mc_eta[childIndex], tt.mc_phi[childIndex], tt.mc_E[childIndex])

      # Calculate the visible tau pT
      vis_vec = tau_vec - neu_vec[0]
      vistaupt = vis_vec.Pt()
      if vistaupt < 25000: continue

      if abs(tt.mc_eta[t]) < 2.47:
        tauPass.append(t)


    #Count the number of leptons/taus in the event
    totTaus = len(tauPass)
    totElecs = len(elecs)
    totMuons = len(muons)
    totLeps = totElecs + totMuons
    totLeptons = len(tauPass) + len(elecs) + len(muons)


    ############# WH LEP-HAD SELECTION ####################
    Lepton_list = []
    if not totTaus == 1: continue
    if not totLeps == 2: continue

    for e in elecs:
      Lepton_list.append(e)
    for m in muons:
      Lepton_list.append(m)

    # SS leptons (to remove Z+jets)
    LepCharges = 1
    for l in Lepton_list:
      LepCharges *= tt.mc_charge[l]
    if not LepCharges == 1: continue

    # Associate leptons to H/W, require OS hlep/tau
    # Usually, if the leptons are OS, then check if tau/lep1 are OS,... BUT we are requiring the leps to be SS,
    # therefore, in the CN, the vlep1 is highest pT lepton, hlep is subleading
    Hlep = []
    Vlep = []
    Lep1_pt = tt.mc_pt[Lepton_list[0]]
    Lep2_pt = tt.mc_pt[Lepton_list[1]]
    if Lep1_pt > Lep2_pt:
      Vlep.append(Lepton_list[0])
      Hlep.append(Lepton_list[1])
    if Lep2_pt > Lep1_pt:
      Vlep.append(Lepton_list[1])
      Hlep.append(Lepton_list[0])

    # 26 GeV lepton to ensure trigger
    good_pt = False
    for l in Lepton_list:
      pT = tt.mc_pt[l]
      if pT > 26000: good_pt = True
    if good_pt == False: continue


    # OS hlep/tau
    HlepCharges = 1      
    HlepCharges *= tt.mc_charge[Hlep[0]]
    HlepCharges *= tt.mc_charge[tauPass[0]]
    if not HlepCharges == -1: continue

    ############## WH LEP-HAD SELECTION END ################

    # If the event survives all these cuts, add it to the event_count
    event_count += 1

    for l in Lepton_list:
      pt = tt.mc_pt[l]
      h_leppt.Fill(pt)

    for t in tauPass:
      #Define a list of neutrinos for each tau
      neu_vec = []
      tau_vec = ROOT.TLorentzVector()
      tau_vec.SetPtEtaPhiE(tt.mc_pt[t], tt.mc_eta[t], tt.mc_phi[t], tt.mc_E[t])
      child_length = len(tt.mc_child_index[t])
      if child_length != 0:
        for child in range(child_length):
          childIndex = tt.mc_child_index[t][child]
          childId = abs(tt.mc_pdgId[tt.mc_child_index[t][child]])
          if not tt.mc_status[tt.mc_child_index[t][child]] == 1: continue
          if childId == 12 or childId == 14 or childId == 16:
            neu_vec.append(ROOT.TLorentzVector())
            neu_vec[0].SetPtEtaPhiE(tt.mc_pt[childIndex], tt.mc_eta[childIndex], tt.mc_phi[childIndex], tt.mc_E[childIndex])

      # Calculate the visible tau pT
      vis_vec = tau_vec - neu_vec[0]
      vistaupt = vis_vec.Pt()
      h_taupt.Fill(vistaupt)

    for p in range(tt.mc_n):
      if abs(tt.mc_pdgId[p]) == 25 and tt.mc_status[p] == 62:
        HiggspT = tt.mc_pt[p]
        h_HiggsPt.Fill(HiggspT)



print 'Event count is %d' % event_count


h_eventcount.SetBinContent(1, event_count)

out_ff.Write()
out_ff.Close()


