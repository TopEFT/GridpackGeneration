#!/bin/bash

##########################################################################################
#GENERAL INSTRUCTIONS:                                                                   #
#You should take care of having the following ingredients in order to have this recipe   #
#working: run card and proc card (in a "cards" folder), MadGraph release, this script    #
#all in the same folder!                                                                 #
#Important: Param card is not mandatory for this script                                  #
##########################################################################################


##########################################################################################
#For runnning, the following command should be used                                      #
#./create_gridpack_template.sh NAME_OF_PRODCUTION RELATIVE_PATH_TO_CARDS QUEUE_SELECTION #
#by NAME_OF_PRODUCTION you should use the names of run and proc card                     #
#for example if the cards are bb_100_250_proc_card_mg5.dat and bb_100_250_run_card.dat   #
#NAME_OF_PRODUCTION should be bb_100_250                                                 #
#for QUEUE_SELECTION is commonly used 1nd, but you can take another choice from bqueues  #
#If QUEUE_SELECTION is omitted, then run on local machine only (using multiple cores)    #
##########################################################################################

make_gridpack () {
    echo "Starting job on " `date` #Only to display the starting of production date
    echo "Running on " `uname -a` #Only to display the machine where the job is running
    echo "System release " `cat /etc/redhat-release` #And the system release
    
    echo "name: ${name}"
    echo "carddir: ${carddir}"
    echo "queue: ${queue}"
    echo "scram_arch: ${scram_arch}"
    echo "cmssw_version: ${cmssw_version}"
    
    # CMS Connect runs git status inside its own script.
    if [ $iscmsconnect -eq 0 ]; then
      cd $PRODHOME
      git status
      echo "Current git revision is:"
      git rev-parse HEAD
      #git diff | cat
      cd -
    fi
    
    # where to find the madgraph tarred distribution
    MGBASEDIR=mgbasedir
    
    MG_EXT=".tar.gz"
    MG=MG5_aMC_v2.6.0$MG_EXT
    MGSOURCE=https://cms-project-generators.web.cern.ch/cms-project-generators/$MG
    
    MGBASEDIRORIG=$(echo ${MG%$MG_EXT} | tr "." "_")
    isscratchspace=0
    
    if [ ! -d ${GEN_FOLDER}/${name}_gridpack ]; then
      #directory doesn't exist, create it and set up environment
      
      if [ ! -d ${GEN_FOLDER} ]; then
        mkdir ${GEN_FOLDER}
      fi
    
      cd $GEN_FOLDER
    
      #export SCRAM_ARCH=slc6_amd64_gcc472 #Here one should select the correct architechture corresponding with the CMSSW release
      #export RELEASE=CMSSW_5_3_32_patch3
    
      export SCRAM_ARCH=${scram_arch}
      export RELEASE=${cmssw_version}
    
      ############################
      #Create a workplace to work#
      ############################
      scram project -n ${name}_gridpack CMSSW ${RELEASE} ;
      if [ ! -d ${name}_gridpack ]; then  
        if [ "${BASH_SOURCE[0]}" != "${0}" ]; then echo "yes here"; return 1; else exit 1; fi
      fi
      
      cd ${name}_gridpack ; mkdir -p work ; cd work
      WORKDIR=`pwd`
      eval `scram runtime -sh`
    
    
      #############################################
      #Copy, Unzip and Delete the MadGraph tarball#
      #############################################
      wget --no-check-certificate ${MGSOURCE}
      tar xzf ${MG}
      rm "$MG"

      # agrohsje 
      cp -rp ${PRODHOME}/addons/models/* ${MGBASEDIRORIG}/models/.
    
      #############################################
      #Apply any necessary patches on top of official release
      #############################################
    
      cd $MGBASEDIRORIG
      cat $PRODHOME/patches/*.patch | patch -p1
    
      # Intended for expert use only!
      if ls $CARDSDIR/${name}*.patch; then
        echo "    WARNING: Applying custom user patch. I hope you know what you're doing!"
        cat $CARDSDIR/${name}*.patch | patch -p1
      fi
    
      LHAPDFCONFIG=`echo "$LHAPDF_DATA_PATH/../../bin/lhapdf-config"`
    
      LHAPDFINCLUDES=`$LHAPDFCONFIG --incdir`
      LHAPDFLIBS=`$LHAPDFCONFIG --libdir`
      export BOOSTINCLUDES=`scram tool tag boost INCLUDE`
    
      echo "set auto_update 0" > mgconfigscript
      echo "set automatic_html_opening False" >> mgconfigscript
      if [ $iscmsconnect -gt 0 ]; then
        echo "set output_dependencies internal" >> mgconfigscript
      fi
      #echo "set output_dependencies internal" >> mgconfigscript
      echo "set lhapdf $LHAPDFCONFIG" >> mgconfigscript
      #echo "set ninja $PWD/HEPTools/lib" >> mgconfigscript
    
      if [ "$queue" == "local" ]; then
          echo "set run_mode 2" >> mgconfigscript
      else
          #suppress lsf emails
          export LSB_JOB_REPORT_MAIL="N"
      
          echo "set run_mode  1" >> mgconfigscript
          if [ "$queue" == "condor" ]; then
            echo "set cluster_type cms_condor" >> mgconfigscript
            echo "set cluster_queue None" >> mgconfigscript
          elif [ "$queue" == "condor_spool" ]; then
            echo "set cluster_type cms_condor_spool" >> mgconfigscript
            echo "set cluster_queue None" >> mgconfigscript
          else
            echo "set cluster_type cms_lsf" >> mgconfigscript
            #*FIXME* broken in mg_amc 2.4.0
            #echo "set cluster_queue $queue" >> mgconfigscript
          fi 
          if [ $iscmsconnect -gt 0 ]; then
            n_retries=10
            long_wait=300
            short_wait=120
          else
            n_retries=3
            long_wait=60
            short_wait=30
          fi
          echo "set cluster_status_update $long_wait $short_wait" >> mgconfigscript
          echo "set cluster_nb_retry $n_retries" >> mgconfigscript
          echo "set cluster_retry_wait 300" >> mgconfigscript
          #echo "set cluster_local_path `${LHAPDFCONFIG} --datadir`" >> mgconfigscript 
          if [[ ! "$RUNHOME" =~ ^/afs/.* ]]; then
              echo "local path is not an afs path, batch jobs will use worker node scratch space instead of afs"
              #*FIXME* broken in mg_amc 2.4.0
              #echo "set cluster_temp_path `echo $RUNHOME`" >> mgconfigscript 
              echo "set cluster_retry_wait 30" >> mgconfigscript 
              isscratchspace=1
          fi      
      fi
    
      echo "save options" >> mgconfigscript
    
      ./bin/mg5_aMC mgconfigscript
    
      #load extra models if needed
      if [ -e $CARDSDIR/${name}_extramodels.dat ]; then
        echo "Loading extra models specified in $CARDSDIR/${name}_extramodels.dat"
        #strip comments
        sed 's:#.*$::g' $CARDSDIR/${name}_extramodels.dat | while read model
        do
          #get needed BSM model
          if [[ $model = *[!\ ]* ]]; then
            echo "Loading extra model $model"
            wget --no-check-certificate https://cms-project-generators.web.cern.ch/cms-project-generators/$model    
            cd models
            if [[ $model == *".zip"* ]]; then
              unzip ../$model
            elif [[ $model == *".tgz"* ]]; then
              tar zxvf ../$model
            elif [[ $model == *".tar"* ]]; then
              tar xavf ../$model
            else 
              echo "A BSM model is specified but it is not in a standard archive (.zip or .tar)"
            fi
            cd ..
          fi
        done
      fi
    
      cd $WORKDIR
      
      if [ "$name" == "interactive" ]; then
        set +e
        set +u
        if [ "${BASH_SOURCE[0]}" != "${0}" ]; then return 0; else exit 0; fi
      fi
    
      echo `pwd`
    
    
      if [ -z ${carddir} ]; then
        echo "Card directory not provided"
        if [ "${BASH_SOURCE[0]}" != "${0}" ]; then return 1; else exit 1; fi
      fi
    
      if [ ! -d $CARDSDIR ]; then
        echo $CARDSDIR " does not exist!"
        if [ "${BASH_SOURCE[0]}" != "${0}" ]; then return 1; else exit 1; fi
      fi  
      
      ########################
      #Locating the proc card#
      ########################
      if [ ! -e $CARDSDIR/${name}_proc_card.dat ]; then
        echo $CARDSDIR/${name}_proc_card.dat " does not exist!"
        if [ "${BASH_SOURCE[0]}" != "${0}" ]; then return 1; else exit 1; fi
      fi
    
      if [ ! -e $CARDSDIR/${name}_run_card.dat ]; then
        echo $CARDSDIR/${name}_run_card.dat " does not exist!"
        if [ "${BASH_SOURCE[0]}" != "${0}" ]; then return 1; else exit 1; fi
      fi  
      
      cp $CARDSDIR/${name}_proc_card.dat ${name}_proc_card.dat
      
      #*FIXME* workaround for broken cluster_local_path handling. 
      # This needs to happen before the code-generation step, as fortran templates
      # are modified based on this parameter.
      echo "cluster_local_path = `${LHAPDFCONFIG} --datadir`" >> ./$MGBASEDIRORIG/input/mg5_configuration.txt 
    
      ########################
      #Run the code-generation step to create the process directory
      ########################
    
      sed -i '$ a display multiparticles' ${name}_proc_card.dat
      ./$MGBASEDIRORIG/bin/mg5_aMC ${name}_proc_card.dat
    
      is5FlavorScheme=0
      if tail -n 20 $LOGFILE | grep -q -e "^p *=.*b\~.*b" -e "^p *=.*b.*b\~"; then 
        is5FlavorScheme=1
      fi
    
      #*FIXME* workaround for broken set cluster_queue and run_mode handling
      if [ "$queue" != "condor" ]; then
        echo "cluster_queue = $queue" >> ./$MGBASEDIRORIG/input/mg5_configuration.txt
        if [ "$isscratchspace" -gt "0" ]; then
            echo "cluster_temp_path = `echo $RUNHOME`" >> ./$MGBASEDIRORIG/input/mg5_configuration.txt
        fi
      elif [ "$queue" == "condor" ]; then
        echo "cluster_queue = None" >> ./$MGBASEDIRORIG/input/mg5_configuration.txt
        echo "run_mode = 1" >> ./$MGBASEDIRORIG/input/mg5_configuration.txt
        echo "cluster_type = cms_condor" >> ./$MGBASEDIRORIG/input/mg5_configuration.txt
      elif [ "$queue" == "condor_spool" ]; then
        echo "cluster_queue = None" >> ./$MGBASEDIRORIG/input/mg5_configuration.txt
        echo "run_mode = 1" >> ./$MGBASEDIRORIG/input/mg5_configuration.txt
        echo "cluster_type = cms_condor_spool" >> ./$MGBASEDIRORIG/input/mg5_configuration.txt
      fi
    
      # Previous cluster_local_path setting  gets erased after
      # code-generation mg5_aMC execution, set it up again before the integrate step.
      echo "cluster_local_path = `${LHAPDFCONFIG} --datadir`" >> ./$MGBASEDIRORIG/input/mg5_configuration.txt    
      
      if [ -e $CARDSDIR/${name}_patch_me.sh ]; then
          echo "Patching generated matrix element code with " $CARDSDIR/${name}_patch_me.sh
          /bin/bash "$CARDSDIR/${name}_patch_me.sh" "$WORKDIR/$MGBASEDIRORIG"
      fi;
      
      if [ "${jobstep}" = "CODEGEN" ]; then
          echo "job finished step ${jobstep}, exiting now."
          if [ "${BASH_SOURCE[0]}" != "${0}" ]; then return 0; else exit 0; fi
      fi
    
    elif [ "${jobstep}" = "INTEGRATE" ] || [ "${jobstep}" = "ALL" ]; then  
      echo "Reusing existing directory assuming generated code already exists"
      echo "WARNING: If you changed the process card you need to clean the folder and run from scratch"
    
      if [ "$is5FlavorScheme" -eq -1 ]; then
        if cat $LOGFILE_NAME*.log | grep -q -e "^p *=.*b\~.*b" -e "^p *=.*b.*b\~"; then 
            is5FlavorScheme=1
        else
            is5FlavorScheme=0
        fi 
      fi
      
      cd $GEN_FOLDER
      
      if [ ! -d ${WORKDIR} ]; then
        echo "Existing directory does not contain expected folder $WORKDIR"
        if [ "${BASH_SOURCE[0]}" != "${0}" ]; then return 1; else exit 1; fi
      fi
      cd $WORKDIR
    
      eval `scram runtime -sh`
      export BOOSTINCLUDES=`scram tool tag boost INCLUDE`
    
      #if lhapdf6 external is available then above points to lhapdf5 and needs to be overridden
      LHAPDF6TOOLFILE=$CMSSW_BASE/config/toolbox/$SCRAM_ARCH/tools/available/lhapdf6.xml
      if [ -e $LHAPDF6TOOLFILE ]; then
        LHAPDFCONFIG=`cat $LHAPDF6TOOLFILE | grep "<environment name=\"LHAPDF6_BASE\"" | cut -d \" -f 4`/bin/lhapdf-config
      else
        LHAPDFCONFIG=`echo "$LHAPDF_DATA_PATH/../../bin/lhapdf-config"`
      fi
    
      #make sure env variable for pdfsets points to the right place
      export LHAPDF_DATA_PATH=`$LHAPDFCONFIG --datadir`  
      
    
      if [ "$name" == "interactive" ]; then
        set +e
        set +u  
        if [ "${BASH_SOURCE[0]}" != "${0}" ]; then return 0; else exit 0; fi
      else
        if [ $iscmsconnect -gt 0 ]; then
          echo "Reusing existing process directory - be careful!"
        else
          echo "Reusing an existing process directory ${name} is not actually supported in production at the moment.  Please clean or move the directory and start from scratch."
          if [ "${BASH_SOURCE[0]}" != "${0}" ]; then return 1; else exit 1; fi
        fi
      fi
      
      if [ -z ${carddir} ]; then
        echo "Card directory not provided"
        if [ "${BASH_SOURCE[0]}" != "${0}" ]; then return 1; else exit 1; fi
      fi
    
      if [ ! -d $CARDSDIR ]; then
        echo $CARDSDIR " does not exist!"
        if [ "${BASH_SOURCE[0]}" != "${0}" ]; then return 1; else exit 1; fi
      fi
      
      if [ ! -e $CARDSDIR/${name}_run_card.dat ]; then
        echo $CARDSDIR/${name}_run_card.dat " does not exist!"
        if [ "${BASH_SOURCE[0]}" != "${0}" ]; then return 1; else exit 1; fi
      fi  
    
    fi  
    
    if [ -d gridpack ]; then
      rm -rf gridpack
    fi
    
    if [ -d processtmp ]; then
      rm -rf processtmp
    fi
    
    if [ -d process ]; then
      rm -rf process
    fi
    
    if [ ! -d ${name} ]; then
      echo "Process output directory ${name} not found.  Either process generation failed, or the name of the output did not match the process name ${name} provided to the script."
      if [ "${BASH_SOURCE[0]}" != "${0}" ]; then return 1; else exit 1; fi
    fi
    
    #make copy of process directory for reuse only if not running on temp scratch space
    if [ "$isscratchspace" -gt "0" ]; then
      echo "moving generated process to working directory"
      mv $name processtmp
    else
      echo "copying generated process to working directory"
      cp -a $name/ processtmp
    fi
    
    cd processtmp

    for proc in $(ls -d SubProcesses/P*); do
        echo "Moving $proc..."
        mv $proc ../../../
    done

    exit 1
    
    #RWSEED=657343
    #RWNEVT=1000
    #./run.sh $RWNEVT $RWSEED
    #mv $WORKDIR/process/madevent/Events/GridRun_${RWSEED}/"events.lhe.gz" $WORKDIR/"unweighted_events.lhe.gz"
    #ls -ltr $WORKDIR
}

#exit on first error
set -e

#First you need to set couple of settings:

name=${1}

# name of the run
carddir=${2}

# which queue
queue=${3}

# processing options
jobstep=${4}

if [ -n "$5" ]
  then
    scram_arch=${5}
  else
    scram_arch=slc6_amd64_gcc630 #slc6_amd64_gcc481
fi

if [ -n "$6" ]
  then
    cmssw_version=${6}
  else
    cmssw_version=CMSSW_9_3_8 #CMSSW_7_1_30
fi
 
# jobstep can be 'ALL','CODEGEN', 'INTEGRATE', 'MADSPIN'

if [ -z "$PRODHOME" ]; then
  PRODHOME=`pwd`
fi 

# Folder structure is different on CMSConnect
helpers_dir=${PRODHOME}/Utilities
if [ ! -d "$helpers_dir" ]; then
    helpers_dir=$(git rev-parse --show-toplevel)/bin/MadGraph5_aMCatNLO/Utilities
fi
source ${helpers_dir}/gridpack_helpers.sh 


if [ ! -z ${CMSSW_BASE} ]; then
  echo "Error: This script must be run in a clean environment as it sets up CMSSW itself.  You already have a CMSSW environment set up for ${CMSSW_VERSION}."
  echo "Please try again from a clean shell."
  if [ "${BASH_SOURCE[0]}" != "${0}" ]; then return 1; else exit 1; fi
fi

#catch unset variables
set -u

if [ -z ${name} ]; then
  echo "Process/card name not provided"
  if [ "${BASH_SOURCE[0]}" != "${0}" ]; then return 1; else exit 1; fi
fi

if [ -z ${queue} ]; then
  queue=local
fi

if [ -z ${jobstep} ]; then
  jobstep=ALL
fi

#Check values of jobstep:
if [ "${jobstep}" == "ALL" ] || [ "${jobstep}" == "CODEGEN" ] || [ "${jobstep}" == "INTEGRATE" ] || [ "${jobstep}" == "MADSPIN" ]; then
    echo "Running gridpack generation step ${jobstep}"
else
    echo "No Valid Job Step specified, exiting "
    if [ "${BASH_SOURCE[0]}" != "${0}" ]; then return 1; else exit 1; fi
fi 

# @TODO: MADSPIN hasn't been split from INTEGRATE step yet. Just exit for now.
if  [ "${jobstep}" == "MADSPIN" ]; then
    echo "MADSPIN hasn't been split from INTEGRATE step yet. Doing nothing. "
    if [ "${BASH_SOURCE[0]}" != "${0}" ]; then return 1; else exit 1; fi
fi 

#For correct running you should place at least the run and proc card in a folder under the name "cards" in the same folder where you are going to run the script
RUNHOME=`pwd`
LOGFILE=${RUNHOME}/${name}.log
LOGFILE_NAME=${LOGFILE/.log/}

# where to search for datacards, that have to follow a naming code: 
#   ${name}_proc_card_mg5.dat
#   ${name}_run_card.dat
CARDSDIR=${PRODHOME}/${carddir}
# the folder where the script works, I guess
GEN_FOLDER=${RUNHOME}/${name}

WORKDIR=$GEN_FOLDER/${name}_gridpack/work/

is5FlavorScheme=-1
if [ -z ${iscmsconnect:+x} ]; then iscmsconnect=0; fi

# Workaround to numpy bug in CMSSW_9_3_0 under slc6_amd64_gcc630
if [ $iscmsconnect -gt 0 ]; then
  if [ "$cmssw_version" == "CMSSW_9_3_0" ] && [ "$scram_arch" == "slc6_amd64_gcc630" ]; then
    export PYTHONPATH=/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/py2-numpy/1.14.1-omkpbe2/lib/python2.7/site-packages:$PYTHONPATH
  fi
fi

if [ "${name}" != "interactive" ]; then
    # Make PIPESTATUS inherit make_gridpack return/exit codes
    set -o pipefail
    # Do not exit main shell if make_gridpack fails. We want to return rather than exit if we are sourcing this script.
    set +e
    make_gridpack | tee $LOGFILE
    pipe_status=$PIPESTATUS
    # tee above will create a subshell, so exit calls inside function will just affect that subshell instance and return the exitcode in this shell.
    # This breaks cases when the calls inside make_gridpack try to exit the main shell with some error, hence not having the gridpack directory.
    # or not wanting to create a tarball.
    # Explicitely return or exit accordingly if make_gridpack returned an error.
    if [ $pipe_status -ne 0 ]; then
      if [ "${BASH_SOURCE[0]}" != "${0}" ]; then return $pipe_status; else exit $pipe_status; fi
    fi
    # Also, step CODEGEN will try to exit with 0, but that will only affect the subshell.
    # Explicitely exit the main shell (or return 0 if sourced) if jobstep == CODEGEN.
    if [ "$jobstep" == "CODEGEN" ]; then
      if [ "${BASH_SOURCE[0]}" != "${0}" ]; then return 0; else exit 0; fi
    fi
    # Re-enable set -e
    set -e

    echo "Saving log file(s)"
    cd $WORKDIR/gridpack
    for i in ${LOGFILE_NAME}*.log; do 
        cp $i ${i/$LOGFILE_NAME/gridpack_generation}
    done
else
    make_gridpack
fi
