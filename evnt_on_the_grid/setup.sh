#!/bin/bash
AtlasProdRelease=17.2.13.10,slc5,testarea=/afs/cern.ch/work/i/ideal/evnt_on_the_grid
echo "setting up athena"
export AtlasSetup=/afs/cern.ch/atlas/software/dist/AtlasSetup
source $AtlasSetup/scripts/asetup.sh $AtlasProdRelease