#!/usr/bin/env python

import ROOT

import alphatwirl

from behind_scene import TwilightTree

##__________________________________________________________________||
path = '/Users/sakuma/work/cms/c170327_twirl_tutorial/20170530_top/20170530_01_example_tree/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8_ntuple_test.root'

tfile = ROOT.TFile.Open(path)
tree = tfile.Get('nTupleTree/tree')

twtree = TwilightTree(tree)

##__________________________________________________________________||
RoundLog = alphatwirl.binning.RoundLog
tblcfg = [
    dict(
        keyAttrNames = ('Jets.Pt', ),
        keyIndices = (0, ),
        binnings = (RoundLog(0.1, 100), ),
        keyOutColumnNames = ('jet_pt', ),
    ),
    dict(
        keyAttrNames = ('Muons.Pt', ),
        keyIndices = (0, ),
        binnings = (RoundLog(0.1, 100), ),
        keyOutColumnNames = ('muon_pt', ),
    ),
]

dataframes = twtree.summarize(tblcfg = tblcfg)
df_jet_pt = dataframes[0]
df_muon_pt = dataframes[1]

print
print df_jet_pt.to_string(index = False)
print
print df_muon_pt.to_string(index = False)

##__________________________________________________________________||
