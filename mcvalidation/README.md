# Girdpack validation scripts
## Basic procedure
To validate a gridpack, we need samples to process. Since our Coffea framework uses nanoAOD files, the quickest way to validate a gridpack is to make nanoGEN samples. These contain _only_ GEN level information, and are stored using the nano format (flat columnar tables)
The `scan.py` script can run over multiple gridpacks and submit jobs to CRAB.

:warning: Since this uses CRAB, make sure you have a proper `voms-proxy` configured!
This script can be run from anywhere that has access to the CMS Grid: lxplus, glados, Nebraska, etc.

:warning: We have not run this script from CMS Connect. It might be possible, but you'd need to find the XRootD redirector. It's easier to store you're gridpacks in a known, good area like EOS, CERNBox, or ceph on glados.

Once the nanoGEN samples are made, you can use our TopEFT [validation scripts](https://github.com/TopEFT/topeft/pull/491).

:warning: Update the link to the `mc_validation` folder in `master` once the PR is merged.

Steps for validation
1. Crate a gridpack
2. Make nanoGEN samples
3. Make jsons for TopEFT to process
4. Draw the quadratic parameterization curves and extract staring points, example
```
python quad_curves.py /scratch365/byates2/wc_validation/1D/2022_tWZll_4f_StPt6_1M_run0.pkl.gz --json ../../input_samples/sample_jsons/signal_samples/private_UL/2022_tWZll_4f_StPt6_1M_run0.json --dout 2022_tWZll_4f --scale 1.1
```
It's best to try multiple starting points, e.g. `--scale 1.1`, `--scale 1.3`, `--scale 1.5` will return the WC value where SM value of that process is scaled by 10, 30, or 50%

5. Process the files, example on glados using `futures` (only use `futures` if the files are small since this runs locally and uses up resources)
```
python run_gen_analysis.py ../../input_samples/sample_jsons/signal_samples/private_UL/2022_tWZll_4f_StPt6_1M_run0.json -o 2022_tWZll_4f_StPt6_1M_run0 -p /scratch365/byates2/wc_validation/ -x futures -r file:///cms/cephfs/data/
```
6. The `comp_norm.py` script allows you to plot your samples vs another, example
```
python comp_norm.py /scratch365/byates2/wc_validation/2022_tWZll_4f_StPt6_1M_run0.pkl.gz histos/2022_TWZToLL_Wlep_central.pkl.gz ../../input_samples/sample_jsons/signal_samples/private_UL/2022_tWZ_noDecay_1j_Mll30_StPt4_1M_xQcut5_run0.json
```
