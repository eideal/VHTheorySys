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
h_Zmass = ROOT.TH1F('Zmass','Zmass', 15, 60000, 120000)


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

      if abs(tt.mc_pdgId[p]) == 15 and tt.mc_status[p] == 195:
        tau_lep = False
        child_length = len(tt.mc_child_index[p])

        if child_length != 0:
          for child in range(child_length):
            childId = abs(tt.mc_pdgId[tt.mc_child_index[p][child]])
            if abs(tt.mc_pdgId[tt.mc_child_index[p][child]]) == 11 or abs(tt.mc_pdgId[tt.mc_child_index[p][child]]) == 13:
              tau_lep = True
              
        if tau_lep == False: tau_hads.append(p)


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

      # Calculate the visible tau pT and require > 20000
      vis_vec = tau_vec - neu_vec[0]
      vistaupt = vis_vec.Pt()
      if vistaupt < 20000: continue

      if abs(tt.mc_eta[t]) < 2.47:
        tauPass.append(t)


    #Count the number of leptons/taus in the event
    totTaus = len(tauPass)
    totElecs = len(elecs)
    totMuons = len(muons)
    totLeps = totElecs + totMuons
    totLeptons = len(tauPass) + len(elecs) + len(muons)


    ############# ZH HAD-HAD SELECTION
    Lepton_list = []
    if not totTaus == 2: continue
    if not totLeps == 2: continue

    # SF leptons
    if not totMuons == 2:
      if not totElecs == 2: continue


    if totElecs == 2: Lepton_list = elecs
    if totMuons == 2: Lepton_list = muons

    # 26 GeV lepton to ensure trigger
    good_pt = False
    for l in Lepton_list:
      pT = tt.mc_pt[l]
      if pT > 26000: good_pt = True
    if good_pt == False: continue

        
    # OS leptons
    totCharge = 1
    for l in Lepton_list:
      totCharge *= tt.mc_charge[l]

    if not totCharge == -1: continue

    # Reconstruct the Z mass peak
    first_lep_vec = ROOT.TLorentzVector()
    sec_lep_vec = ROOT.TLorentzVector()
    first_lep_vec.SetPtEtaPhiE(tt.mc_pt[Lepton_list[0]], tt.mc_eta[Lepton_list[0]], tt.mc_phi[Lepton_list[0]], tt.mc_E[Lepton_list[0]])
    sec_lep_vec.SetPtEtaPhiE(tt.mc_pt[Lepton_list[1]], tt.mc_eta[Lepton_list[1]], tt.mc_phi[Lepton_list[1]], tt.mc_E[Lepton_list[1]])

    Mass = (first_lep_vec + sec_lep_vec).M()

    if not Mass < 120000: continue
    if not Mass > 60000: continue
    h_Zmass.Fill(Mass)
    
    # OS taus
    TauCharges = 1
    for t in tauPass:
      TauCharges *= tt.mc_charge[t]

    if not TauCharges == -1: continue


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

print 'Event count is %d' % event_count


h_eventcount.SetBinContent(1, event_count)

out_ff.Write()
out_ff.Close()    


