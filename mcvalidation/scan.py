'''
Bulk CRAB submission script
This script is used to validate multiple gridpacks (e.g. single WC scans, or multiple starting points).
First, make sure your girdpack(s) are in a publicly accessible area for XRootD
such as CERNBox or any server with a XRootD URL.

This script has a few blocks you can modify:
fragments - These are the Pythia shower settings to use. Our Run 3 fragments are in the mgprod repo https://github.com/TopEFT/mgprod/tree/Run3/lobster_workflow/fragments/run3
gridpack_name - These are the list of gridpacks to use, by default they take dynamic tags for easier parsing
wc_dict - This was intended to store the completed WCs for each process, but feel free to just run over all WCs if you have them
tag - The tag you used when making your gridpack (e.g. `Run3Dim6TopWithTOP22006AxisScan`)
wc_tag - An optional tag to help differentiate batches of gridpacks (e.g. `7pts_500`), feel free to remove

The script will loop over all processes and check if the gridpack exists (make sure you have a copy locally or at least `touch <gp_name>`.
Next, it checks for existing scripts to make sure it doesn't resubmit a process. If you need to rerun a process/WC, remove those scripts first.
Since this uses CRAB, make sure you have a proper voms-proxy configured!
This script can be run from anywhere that has access to the CMS Grid: lxplus, glados, Nebraska, etc.
'''

import subprocess
import os

setup = '''\
#!/bin/bash

xrdcp root://cmsxrootd.crc.nd.edu///store/user/byates2/Run3_gridpacks/{gridpack} gridpack.xz

p=`pwd`
cmsDriver.py Configuration/GenProduction/python/{fragment} \\
    --python_filename nanogen_cfg.py --eventcontent NANOAODGEN \\
    --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAOD \\
    --fileout file:nanogen_123.root --conditions 130X_mcRun3_2022_realistic_v5 \\
    --step LHE,GEN,NANOGEN --geometry DB:Extended --era Run3 --no_exec --mc -n {n_env} \\
    --customise_commands='process.RandomNumberGeneratorService.externalLHEProducer.initialSeed='$RANDOM'\\nprocess.externalLHEProducer.args = cms.vstring("'$p'/gridpack.xz")'
#CRAB wasn't randomizing the seed, so using $RANDOM now
echo "named_weights = [" >> nanogen_cfg.py
tar xf gridpack.xz InputCards
cat InputCards/*reweight_card.dat | grep launch | sed 's/launch --rwgt_name=/"/' | sed 's/$/",/' >> nanogen_cfg.py
echo -e "]\nprocess.genWeightsTable.namedWeightIDs = named_weights\nprocess.genWeightsTable.namedWeightLabels = named_weights" >> nanogen_cfg.py
cmsRun -j FrameworkJobReport.xml nanogen_cfg.py
'''

NANO = '''\
from WMCore.Configuration import Configuration
import os
config = Configuration()
config.section_("General")
config.General.requestName = "{proc}_nanoGEN_{wc}_{wc_tag}_Run3_{run}"
config.General.workArea = "grid"
config.General.transferOutputs=True
config.General.transferLogs=True
config.section_("JobType")
config.JobType.scriptExe = '{script}'
config.JobType.pluginName = "PrivateMC"
config.JobType.psetName = "/users/byates2/mgprod/lobster_workflow/CMSSW_13_2_9/src/gridpack_validation/nanogen_cfg.py"
config.JobType.disableAutomaticOutputCollection = False
config.section_("Data")
config.Data.outputPrimaryDataset = "{proc}_LO_EFT"
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
NJOBS = 100
# NJOBS = 900
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.ignoreLocality = False
config.Data.outLFNDirBase = '/store/user/byates/{proc}/nanoGEN_Run3/2022'
config.section_("Site")
config.Site.storageSite = "T3_US_NotreDame"
'''


fragments = {
    'ttll': 'ttlnuJets_custom_ND-fragment.py',
    'ttH': 'ttHJets_custom_ND-fragment.py',
    'ttA': 'ttgamma_custom_ND-fragment.py',
    'ttlnu': 'ttlnuJets_custom_ND-fragment.py',
    'tllq': 'tllq4f_custom_ND-fragment.py',
    'tHq': 'tllq4f_custom_ND-fragment.py',
    'tttt': 'tttt_custom_ND-fragment.py',
    'tWZ': 'ttlnu_custom_ND-fragment.py',
    'tWZll': 'ttlnu_custom_ND-fragment.py',
}
gridpack_name = {
    'tttt': 'tttt_{wc}Run3_52WCs_SMEFTsim_top_masslessAxisScan_run0_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
    'tttt': 'tttt_{wc}Run3With52WCsSMEFTsimTopMasslessTOP22006AxisScan_{run}_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
    'tttt': 'tttt_{wc}Run3With52WCsSMEFTsimTopMasslessAxisScan_{run}_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
    'tttt': 'tttt_{wc}{tag}_{run}_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
    'ttH': 'ttHJet_{wc}Run3_52WCs_SMEFTsim_top_masslessAxisScan_run0_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
    'ttH': 'ttHJet_{wc}Run3With52WCsSMEFTsimTopMasslessAxisScan_run0_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
    'ttH': 'ttHJet_{wc}Run3With52WCsSMEFTsimTopMasslessTOP22006AxisScan_{run}_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
    'ttH': 'ttHJet_{wc}Run3With52WCsSMEFTsimTopMasslessAxisScan_{run}_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
    'ttH': 'ttHJet_{wc}{tag}_{run}_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
    'tllq': 'tllq4fNoSchanWNoHiggs0p_{wc}Run3_52WCs_SMEFTsim_top_masslessAxisScan_run0_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
    'tllq': 'tllq4fNoSchanWNoHiggs0p_{wc}Run3With52WCsSMEFTsimTopMasslessTOP22006AxisScan_run3_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
    'tllq': 'tllq4fNoSchanWNoHiggs0p_{wc}{tag}_run3_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
    'tHq': 'tHq4f_{wc}Run3_52WCs_SMEFTsim_top_masslessAxisScan_run0_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
    'tHq': 'tHq4f_{wc}Run3With52WCsSMEFTsimTopMasslessTOP22006AxisScan_run3_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
    'tHq': 'tHq4f_{wc}{tag}_run3_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
    'ttll': 'ttllNuNuJetNoHiggs_{wc}Run3_52WCs_SMEFTsim_top_masslessAxisScan_run3_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
    'ttll': 'ttllNuNuJetNoHiggs_{wc}Run3With52WCsSMEFTsimTopMasslessTOP22006AxisScan_{run}_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
    'ttll': 'ttllNuNuJetNoHiggs_{wc}Run3With52WCsSMEFTsimTopMasslessAxisScan_{run}_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
    'ttll': 'ttllNuNuJetNoHiggs_{wc}{tag}_{run}_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
    'ttlnu': 'ttlnuJet_{wc}Run3With52WCsSMEFTsimTopMasslessTOP22006AxisScan_run3_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
    'ttlnu': 'ttlnuJet_{wc}{tag}_run3_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
    'tWZ': 'tWZ_{wc}{tag}_{run}_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
    'tWZll': 'tWZll_{wc}{tag}_{run}_slc7_amd64_gcc10_CMSSW_12_4_8_tarball.tar.xz',
}
wc_dict = {
    'tttt': ['cHQ1', 'cHQ3', 'cHbox', 'cHt', 'cHtbRe', 'cQQ1', 'cQb8', 'cQd1', 'cQd8', 'cQe1', 'cQe2', 'cQe3', 'cQj11', 'cQj18', 'cQj31', 'cQj38', 'cQl11', 'cQl12', 'cQl31', 'cQl32', 'cQl33', 'cQt1', 'cQt8', 'cQu1', 'cQu8', 'cbBRe', 'cbWRe', 'cld', 'cleQt1Re11', 'cleQt1Re22', 'cleQt1Re33', 'cleQt3Re11', 'cleQt3Re22', 'cleQt3Re33', 'clj1', 'clu', 'ctBRe', 'ctGRe', 'ctHRe', 'ctWRe', 'ctb8', 'ctd1', 'ctd8', 'cte1', 'cte2', 'cte3', 'ctj1', 'ctj8', 'ctl1', 'ctl2', 'ctt', 'ctu1', 'ctu8'],
    'ttH': ['cHQ1', 'cHQ3', 'cHbox', 'cHt', 'cHtbRe', 'cQb8', 'cQd1', 'cQd8', 'cQe1', 'cQe2', 'cQe3', 'cQj11', 'cQj18', 'cQj31', 'cQj38', 'cQl11', 'cQl12', 'cQl31', 'cQl32', 'cQl33', 'cQu1', 'cQu8', 'cbBRe', 'cbWRe', 'cld', 'cleQt1Re11', 'cleQt1Re22', 'cleQt1Re33', 'cleQt3Re11', 'cleQt3Re22', 'cleQt3Re33', 'clj1', 'clu', 'ctBRe', 'ctGRe', 'ctHRe', 'ctWRe', 'ctb8', 'ctd1', 'ctd8', 'cte1', 'cte2', 'cte3', 'ctj1', 'ctj8', 'ctl1', 'ctl2', 'ctu1', 'ctu8'],
    'ttll': ['cHQ1', 'cHQ3', 'cHbox', 'cHt', 'cHtbRe', 'cQb8', 'cQd1', 'cQd8', 'cQe1', 'cQe2', 'cQe3', 'cQj11', 'cQj18', 'cQj31', 'cQj38', 'cQl11', 'cQl12', 'cQl31', 'cQl32', 'cQl33', 'cQu1', 'cQu8', 'cbBRe', 'cbWRe', 'cld', 'cleQt1Re11', 'cleQt1Re22', 'cleQt1Re33', 'cleQt3Re11', 'cleQt3Re22', 'cleQt3Re33', 'clj1', 'clu', 'ctBRe', 'ctGRe', 'ctHRe', 'ctWRe', 'ctb8', 'ctd1', 'ctd8', 'cte1', 'cte2', 'cte3', 'ctj1', 'ctj8', 'ctl1', 'ctl2', 'ctu1', 'ctu8'],
    'ttlnu': ['cHQ1', 'cHQ3', 'cHbox', 'cHt', 'cHtbRe', 'cQb8', 'cQd1', 'cQd8', 'cQe1', 'cQe2', 'cQe3', 'cQj11', 'cQj18', 'cQj31', 'cQj38', 'cQl11', 'cQl12', 'cQl31', 'cQl32', 'cQl33', 'cQu1', 'cQu8', 'cbBRe', 'cbWRe', 'cld', 'cleQt1Re11', 'cleQt1Re22', 'cleQt1Re33', 'cleQt3Re11', 'cleQt3Re22', 'cleQt3Re33', 'clj1', 'clu', 'ctBRe', 'ctGRe', 'ctHRe', 'ctWRe', 'ctb8', 'ctd1', 'ctd8', 'cte1', 'cte2', 'cte3', 'ctj1', 'ctj8', 'ctl1', 'ctl2', 'ctu1', 'ctu8'],
    'tllq': ['cHQ1', 'cHQ3', 'cHbox', 'cHt', 'cHtbRe', 'cQb8', 'cQd1', 'cQd8', 'cQe1', 'cQe2', 'cQe3', 'cQj11', 'cQj18', 'cQj31', 'cQj38', 'cQl11', 'cQl12', 'cQl31', 'cQl32', 'cQl33', 'cQu1', 'cQu8', 'cbBRe', 'cbWRe', 'cld', 'cleQt1Re11', 'cleQt1Re22', 'cleQt1Re33', 'cleQt3Re11', 'cleQt3Re22', 'cleQt3Re33', 'clj1', 'clu', 'ctBRe', 'ctGRe', 'ctHRe', 'ctWRe', 'ctb8', 'ctd1', 'ctd8', 'cte1', 'cte2', 'cte3', 'ctj1', 'ctj8', 'ctl1', 'ctl2', 'ctu1', 'ctu8'],
    'tHq': ['cHQ1', 'cHQ3', 'cHbox', 'cHt', 'cHtbRe', 'cQb8', 'cQd1', 'cQd8', 'cQe1', 'cQe2', 'cQe3', 'cQj11', 'cQj18', 'cQj31', 'cQj38', 'cQl11', 'cQl12', 'cQl31', 'cQl32', 'cQl33', 'cQu1', 'cQu8', 'cbBRe', 'cbWRe', 'cld', 'cleQt1Re11', 'cleQt1Re22', 'cleQt1Re33', 'cleQt3Re11', 'cleQt3Re22', 'cleQt3Re33', 'clj1', 'clu', 'ctBRe', 'ctGRe', 'ctHRe', 'ctWRe', 'ctb8', 'ctd1', 'ctd8', 'cte1', 'cte2', 'cte3', 'ctj1', 'ctj8', 'ctl1', 'ctl2', 'ctu1', 'ctu8'],
    'tWZ': ['cHQ1', 'cHQ3', 'cHbox', 'cHt', 'cHtbRe', 'cQb8', 'cQd1', 'cQd8', 'cQe1', 'cQe2', 'cQe3', 'cQj11', 'cQj18', 'cQj31', 'cQj38', 'cQl11', 'cQl12', 'cQl31', 'cQl32', 'cQl33', 'cQu1', 'cQu8', 'cbBRe', 'cbWRe', 'cld', 'cleQt1Re11', 'cleQt1Re22', 'cleQt1Re33', 'cleQt3Re11', 'cleQt3Re22', 'cleQt3Re33', 'clj1', 'clu', 'ctBRe', 'ctGRe', 'ctHRe', 'ctWRe', 'ctb8', 'ctd1', 'ctd8', 'cte1', 'cte2', 'cte3', 'ctj1', 'ctj8', 'ctl1', 'ctl2', 'ctu1', 'ctu8'],
    'tWZll': ['cbW', 'cpQ3', 'cpQM', 'cpt', 'cptb', 'cQb8', 'cQd1', 'cQd8', 'cQei', 'cQl3i', 'cQlMi', 'cQq11', 'cQq13', 'cQq81', 'cQq83', 'cQu1', 'cQu8', 'ctb8', 'ctd1', 'ctd8', 'ctei', 'ctG', 'ctli', 'ctlSi', 'ctlTi', 'ctp', 'ctq1', 'ctq8', 'ctu1', 'ctu8', 'ctW', 'ctZ'],
}
done = {
    'ttH': [],
    'tttt': [],
    'ttH': [],
}
done = {'ttH': {'run0': ['cHQ1', 'cHQ3', 'cHbox', 'cHt', 'cHtbRe', 'cQb8', 'cQd1', 'cQd8', 'cQe1', 'cQe2', 'cQe3', 'cQj11', 'cQj18', 'cQj31', 'cQj38', 'cQl11', 'cQl12', 'cQl31', 'cQl32', 'cQl33', 'cQu1', 'cQu8', 'cbBRe', 'cbWRe', 'cld', 'cleQt1Re33', 'cleQt3Re11', 'cleQt3Re22', 'cleQt3Re33', 'clj1', 'clu', 'ctBRe', 'ctGRe', 'ctHRe', 'ctWRe', 'ctb8', 'ctd1', 'ctd8', 'cte1', 'cte2', 'cte3', 'ctj1', 'ctj8', 'ctl1', 'ctl2', 'ctu1', 'ctu8'], 'run1': ['cHQ1', 'cHQ3', 'cHbox', 'cHt', 'cHtbRe', 'cQb8', 'cQd1', 'cQd8', 'cQe1', 'cQe2', 'cQe3', 'cQj11', 'cQj18', 'cQj31', 'cQj38', 'cQl11', 'cQl12', 'cQl31', 'cQl32', 'cQl33', 'cQu1', 'cQu8', 'cbBRe', 'cbWRe', 'cld', 'cleQt1Re33', 'cleQt3Re11', 'cleQt3Re22', 'cleQt3Re33', 'clj1', 'clu', 'ctBRe', 'ctGRe', 'ctHRe', 'ctWRe', 'ctb8', 'ctd1', 'ctd8', 'cte1', 'cte2', 'cte3', 'ctj1', 'ctj8', 'ctl1', 'ctl2', 'ctu1', 'ctu8'], 'run2': ['cHQ1', 'cHQ3', 'cHbox', 'cHt', 'cHtbRe', 'cQb8', 'cQd1', 'cQd8', 'cQe1', 'cQe2', 'cQe3', 'cQj11', 'cQj18', 'cQj31', 'cQj38', 'cQl11', 'cQl12', 'cQl31', 'cQl32', 'cQl33', 'cQu1', 'cQu8', 'cbBRe', 'cbWRe', 'cld', 'cleQt1Re33', 'cleQt3Re11', 'cleQt3Re22', 'cleQt3Re33', 'clj1', 'clu', 'ctBRe', 'ctGRe', 'ctHRe', 'ctWRe', 'ctb8', 'ctd1', 'ctd8', 'cte1', 'cte2', 'cte3', 'ctj1', 'ctj8', 'ctl1', 'ctl2', 'ctu1', 'ctu8'], 'run3': ['cHQ1', 'cHQ3', 'cHbox', 'cHt', 'cHtbRe', 'cQb8', 'cQd1', 'cQd8', 'cQe1', 'cQe2', 'cQe3', 'cQj11', 'cQj18', 'cQj31', 'cQj38', 'cQl11', 'cQl12', 'cQl31', 'cQl32', 'cQl33', 'cQu1', 'cQu8', 'cbBRe', 'cbWRe', 'cld', 'cleQt1Re33', 'cleQt3Re11', 'cleQt3Re22', 'cleQt3Re33', 'clj1', 'clu', 'ctBRe', 'ctGRe', 'ctHRe', 'ctWRe', 'ctb8', 'ctd1', 'ctd8', 'cte1', 'cte2', 'cte3', 'ctj1', 'ctj8', 'ctl1', 'ctl2', 'ctu1', 'ctu8'], 'run4': ['cHQ1', 'cHQ3', 'cHbox', 'cHt', 'cHtbRe', 'cQb8', 'cQd1', 'cQd8', 'cQe1', 'cQe2', 'cQe3', 'cQj11', 'cQj18', 'cQj31', 'cQj38', 'cQl11', 'cQl12', 'cQl31', 'cQl32', 'cQl33', 'cQu1', 'cQu8', 'cbBRe', 'cbWRe', 'cld', 'cleQt1Re33', 'cleQt3Re11', 'cleQt3Re22', 'cleQt3Re33', 'clj1', 'clu', 'ctBRe', 'ctGRe', 'ctHRe', 'ctWRe', 'ctb8', 'ctd1', 'ctd8', 'cte1', 'cte2', 'cte3', 'ctj1', 'ctj8', 'ctl1', 'ctl2', 'ctu1', 'ctu8'], 'run5': ['cHQ1', 'cHQ3', 'cHbox', 'cHt', 'cHtbRe', 'cQb8', 'cQd1', 'cQd8', 'cQe1', 'cQe2', 'cQe3', 'cQj11', 'cQj18', 'cQj31', 'cQj38', 'cQl11', 'cQl12', 'cQl31', 'cQl32', 'cQl33', 'cQu1', 'cQu8', 'cbBRe', 'cbWRe', 'cld', 'cleQt1Re33', 'cleQt3Re11', 'cleQt3Re22', 'cleQt3Re33', 'clj1', 'clu', 'ctBRe', 'ctGRe', 'ctHRe', 'ctWRe', 'ctb8', 'ctd1', 'ctd8', 'cte1', 'cte2', 'cte3', 'ctj1', 'ctj8', 'ctl1', 'ctl2', 'ctu1', 'ctu8'], 'run6': ['cHQ1', 'cHQ3', 'cHbox', 'cHt', 'cHtbRe', 'cQb8', 'cQd1', 'cQd8', 'cQe1', 'cQe2', 'cQe3', 'cQj11', 'cQj18', 'cQj31', 'cQj38', 'cQl11', 'cQl12', 'cQl31', 'cQl32', 'cQl33', 'cQu1', 'cQu8', 'cbBRe', 'cbWRe', 'cld', 'cleQt1Re33', 'cleQt3Re11', 'cleQt3Re22', 'cleQt3Re33', 'clj1', 'clu', 'ctBRe', 'ctGRe', 'ctHRe', 'ctWRe', 'ctb8', 'ctd1', 'ctd8', 'cte1', 'cte2', 'cte3', 'ctj1', 'ctj8', 'ctl1', 'ctl2', 'ctu1', 'ctu8']}}

tag = 'Run3With52WCsSMEFTsimTopMasslessAxisScan'
tag = 'Run3Dim6TopWithTOP22006AxisScan'
wc_tag = '7pts_500'

for irun in range(7): #['run0', 'run1', 'run2', 'run3']:
    run = f'run{irun}'
    for proc in wc_dict:
        # if proc != 'ttH': continue
        #if proc != 'tWZll': continue
        for wc in wc_dict[proc]:
            #if wc not in ['ctHRe', 'ctBRe', 'ctGRe']: continue
            #if proc not in done:
            #    done[proc] = []
            #if wc in done[proc]:
            #    continue
            #if wc in done[proc][run]:
            #    continue
            gridpack = gridpack_name[proc].format(wc=wc, run=run, tag=tag)
            if not os.path.exists(f'/cms/cephfs/data/store/user/byates2/Run3_gridpacks/{gridpack}'):
                #print('Missing gridpack', proc, wc, irun, gridpack)
                continue
            script = f'scripts/setup_nano_{proc}_{wc}_{wc_tag}_{run}.sh'.format(proc=proc, wc=wc)
            if os.path.exists(script):
                continue
            with open(script, 'w') as fout:
                fout.write(setup.format(gridpack=gridpack, fragment=fragments[proc], n_env=int(500./.3))) # ttH 30% matching efficiency
            nano = f'scripts/NANOGEN_{proc}_{wc}_{wc_tag}_{run}.py'.format(proc=proc+'_restrict', wc=wc)
            with open(nano, 'w') as fout:
                fout.write(NANO.format(script=script, wc=wc, proc=proc, wc_tag=wc_tag, run=run))
            cmd = ['crab', 'submit', '-c', nano]
            print(' '.join(cmd))
            subprocess.run(cmd)
            subprocess.run('find grid/crab_* -type f -name "*.tgz" -mmin +2 -size +10M -delete',shell=True)  # Cleanup CRAB stuff
