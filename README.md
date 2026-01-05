# GridpackGeneration

This repository contains the files that are necessary for setting up a `genproducitons` directory that can be used to produce EFT gridpacks

## Instructions: 
- :memo: Make sure you're on the `SMEFTsim_run3` branch
  - ```
    git checkout SMEFTsim_run3
    ```
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
- Follow the [multilepton](multilepton.md) document for Run 3 multilepton samples.

## Notes:
- If you are running the script from anywhere besides `cmsconnect`, the script will create the `genproductions` directory in the same directory that `GridpackGeneration` is located in
- If you are running the script from `cmsconnect`, it will create the directory in your `/home` area

# Gridpack Options:
- The `replace_model` option expects a list of length 2. The first element is the name of the old Madgraph model as it exists in the process card and the second element is the name of the new model that should replace the old one.
```python
from helpers.Gridpack import Gridpack
gp = Gridpack(replace_model=['dim6top_LO_UFO','smloop'])
# Alternatively via setOptions
gp.setOptions(replace_model=['dim6top_LO_UFO','smloop'])
```
- The `restrict` option will tell the code to create a restrict card for the model you choose to use. The value you pass when setting the `restrict` option is a dictionary with the following structure. At the moment, the `restrict` option only has an effect when using `ScanType.SLINSPACE`.
```python
restrict = {
    "ref": "restrict_massless.dat",
    "blocks": ["SMEFT","SMEFTcpv"],
    "keep": True
}
gp.setOptions(restrict=restrict)
```
`ref`
: This should be the name of a restrict card that is already located in the directory of the model you intend to use. It will be used as a template reference to create the actual restrict card that Madgraph will be pointed to.

`blocks`
: This is a list of UFO block names that the code will consider when deciding to keep or exclude certain parameters. Any parameters specified under other blocks will be kept at the values they had in the reference restrict card. The block names _are_ case sensitive!

`keep`
: A booleon value that indicates how to treat matched parameters. If `True`, then only matched parameters are kept and all others in the block are set to 0. If `False`, then only the matched parameters are set to 0.


# Resubmitting failed gridpacks:
Sometimes a gridpack will get past the `codegen` stage but fail in the `integrate`, resulting in a `.tar.xz` file less than 10 MB. <br>
Use the `resubmit.py` script to resubmit these files (:memo: this script *must* be run with `python3`)
```python
python3 resubmit.py
```
