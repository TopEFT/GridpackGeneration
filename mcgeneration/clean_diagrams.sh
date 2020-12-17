#!/bin/bash

clean_diagrams() {
    echo "Old Directory: ${1}"
    if [ ! -d ${2}/${1} ]; then
        mkdir ${2}/${1}
    fi
    cd $1
    for proc in $(ls -d P*); do
        echo "Cleaning: ${proc}"
        sed -i -e 's| FCNC_[Aa-Zz0-9]*=0,||g' ${proc}/matrix*.ps
        sed -i -e 's| DIM6_[Aa-Zz0-9]*=0,||g' ${proc}/matrix*.ps
        sed -i -e 's| FCNC=0,||g' ${proc}/matrix*.ps
        sed -i -e 's|DIM6_||g' ${proc}/matrix*.ps
        sed -i -e 's|DIM6=1, ||g' ${proc}/matrix*.ps
        if [ ! -d ${2}/${1}/${proc} ]; then
            echo "Making new directory ${2}/${1}/${proc}"
            mkdir ${2}/${1}/${proc}
        fi
        cp ${proc}/matrix*.ps ${2}/${1}/${proc}/
    done
    cd -
}

NewDir="/afs/cern.ch/user/a/awightma/www/misc_files"

clean_diagrams "ttH_Diagrams_run0" $NewDir
clean_diagrams "tllq_Diagrams_run0" $NewDir
clean_diagrams "ttll_Diagrams_run0" $NewDir
clean_diagrams "ttlnu_Diagrams_run0" $NewDir
