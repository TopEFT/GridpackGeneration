#!/bin/bash

### settings to modify 
# define pathes (can be kept as is)
EFTMCPATH=`pwd -P`
# path should end with genproductions 
GENPRODPATH=${EFTMCPATH}/../../genproductions
if [ "$(hostname)" == "cmscon.hep.wisc.edu" ]; then
    # path for cmsconnect submit node
    GENPRODPATH="/home/${USER}/genproductions_dim6top_run3"/genproductions
elif [ "$(hostname)" == "condor.crc.nd.edu" ]; then
    GENPRODPATH="/scratch365/${USER}"/genproductions
fi
### end of settings 

### check out official genproduction repo, currently branch 2.6 
if [ -d "$GENPRODPATH" ]; then
    echo "Directory ${GENPRODPATH} shouldn't exist at this point"
    echo " We are going to set it up"
    echo " Please remove it and start over again"
    exit 0
else 
    mkdir -p ${GENPRODPATH}
    cd ${GENPRODPATH}/..
    git clone -b master https://github.com/cms-sw/genproductions.git genproductions 
    cd ${GENPRODPATH}
    # Checkout the repo so that it corresponds to some fixed point in development
    git checkout bc6b1f8d5
    # Copy relevant code  
    for FILE in Utilities patches addons helpers scanfiles gridpack_generation.sh diagram_generation.sh clean_diagrams.sh submit_madpack_ttbareft.sh configure_gridpack.py transfer_gridpacks.py transfer_diagrams.py submit_cmsconnect_gridpack_generation.sh submit_glados_condor_gridpack_generation.sh ; do 
    #for FILE in addons helpers scanfiles diagram_generation.sh clean_diagrams.sh submit_madpack_ttbareft.sh configure_gridpack.py transfer_gridpacks.py transfer_diagrams.py ; do 
	cp -r ${EFTMCPATH}/${FILE} ${GENPRODPATH}/bin/MadGraph5_aMCatNLO/.
    done
    cp -r ${EFTMCPATH}/PLUGIN ${GENPRODPATH}/bin/MadGraph5_aMCatNLO/.
    chmod 755 ${GENPRODPATH}/bin/MadGraph5_aMCatNLO/submit_cmsconnect_gridpack_generation.sh
    chmod 755 ${GENPRODPATH}/bin/MadGraph5_aMCatNLO/submit_glados_condor_gridpack_generation.sh
    cd ${GENPRODPATH}/.
    echo "You are done with setting up genproduction for EFT gridpack generation!"
fi                           

