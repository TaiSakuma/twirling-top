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
        valAttrNames = ('Event.Run', 'Event.LumiSection', 'Event.Number'),
        valOutColumnNames = ('run', 'lumi', 'event'),
        valIndices = (None, None, None)
    ),
    dict(
        valAttrNames = ('Event.Run', 'Event.LumiSection', 'Event.Number', 'Jets.Pt', 'Jets.Eta'),
        valOutColumnNames = ('run', 'lumi', 'event', 'jet_pt', 'jet_eta'),
        valIndices = (None, None, None, '(*)', '\\1')
    ),
]

dataframes = twtree.scan(tblcfg = tblcfg, max_events = 10)

for df in dataframes:
    print df.to_string(index = False)

##__________________________________________________________________||
