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

# Gridpack Options:
- The `replace_model` option expects a list of length 2. The first element is the name of the old Madgraph model as it exists in the process card and the second element is the name of the new model that should replace the old one.
```python
from helpers.Gridpack import Gridpack
gp = Gridpack(replace_model=['dim6top_LO_UFO','smloop'])
# Alternatively via setOptions
gp.setOptions(replace_model=['dim6top_LO_UFO','smloop'])
```
