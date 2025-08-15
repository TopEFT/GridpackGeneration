################################################################################################################
# This script runs over a gridpack and produces cross-sections at dedicated points (`wcvals`)
# Run inside singularity with:
# cmssw-cc7-condor
# unset PERL5LIB
#
# To run, cd into the gridpack `work` dir
# Example: cd ttlnuJet_Run3_42WCs_SMEFTsim_top_run0/ttlnuJet_Run3_42WCs_SMEFTsim_top_run0_gridpack/work/
# and run `cmsenv` to activate the gridpack's CMSSW environment.
# The run the script by providing the name of the process (just for bookkeeping), the path, and the WC to check
# Example: sh gridpack_scan.sh tllq tllq4fNoSchanWNoHiggs0p_Run3_42WCs_SMEFTsim_top_NewStPt4_0p1_run0 cHt
# This will take some time, so use a stable connection or run in `tmux`
################################################################################################################

#!/bin/bash

proc=$1
path=$2
WC=$3

echo "launch ${path}" > mg_run_scan
echo -e "\n" >> mg_run_scan

wcs=("cbGRe" "ctj1" "cQj31" "ctGRe" "ctj8" "ctHRe" "cQj11" "ctu1" "cHtbRe" "cQj18" "clj1" "cleQt1Re22" "ctu8" "cQj38" "ctb8" "ctd8" "cld" "cleQt3Re11" "ctd1" "cleQt3Re33" "cbWRe" "cHbox" "cleQt3Re22" "cQu1" "cQe" "cQd1" "cHt" "ctWRe" "clu" "cQd8" "cleQt1Re33" "cleQt1Re11" "cHQ3" "cQb8" "cHQ1" "ctBRe" "cQu8" "cte" "ctl" "cQl1" "cbBRe" "cQl3")
#wcvals=(-5 -1 0 1 5)
wcvals=(-15 -5 -1 0 1 5)
for val in "${wcvals[@]}"
do
    echo "launch -n ${WC}=${val}" >> mg_run_scan
    for wc in "${wcs[@]}"
    do
        if [[ "$WC" == "$wc"  ]]; then
            echo "set param_card ${wc} ${val}" >> mg_run_scan
        else
            echo "set param_card ${wc} 0.0" >> mg_run_scan
        fi
    done
    echo -e "\n" >> mg_run_scan
done
eval MG5_aMC_v2_9_18/bin/mg5_aMC mg_run_scan 2>&1 | tee log_${proc}_${WC}
#eval bin/mg5_aMC mg_run_scan 2>&1 | tee log_${proc}_${WC}
