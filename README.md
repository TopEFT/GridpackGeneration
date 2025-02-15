# GridpackGeneration

This repository contains the files that are necessary for setting up a `genproducitons` directory that can be used to produce EFT gridpacks

## Instructions: 
- First, `cd` into `mcgeneration`
- Next run `source setup_production.sh`
   - This script will checkout `cms-sw/genproductions`  
   - Two of the files in `cms-sw/genproductions` are overwritten with the modified versions located in `mcgeneration`  
   - Additional files from `mcgeneration` are copied to `genproductions` as well  
   - The script will move you to the `genproductions` directory it just created  
- To make gridpacks:
   - From `genproductions`, `cd` into `bin/MadGraph5_aMCatNLO`  
   - Open `configure_gridpack.py` and modify according to the type of gridpack or gridpacks you would like to produce  
   - Run `configure_gridpack.py`  

## Notes:
- If you are running the script from anywhere besides `cmsconnect`, the script will create the `genproductions` directory in the same directory that `GridpackGeneration` is located in
- If you are running the script from `cmsconnect`, it will create the directory in your `/local-scratch` area
- Files in `/local-scratch` are deleted 30 days after their last modification, so if you would like to keep your gridpacks, be sure to move them to a permanent location after they are completed

## Making Run 2 gridpacks on CMS Connect:
To correctly make gridpacks for Run 2 (based on slc7/cc7) you must enter singularity:
```
cmssw-cc7-condor-python27
```
This command should be executed from the base `genproductions` folder (*not* the MadGraph5 folder, otherwise the git repository won't be available).
