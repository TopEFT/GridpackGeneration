# Producing Run 3 gridpacks for the multilepton analysis
Once this repo has been setup and `cms-sw/genproductions` has been checked out (see README.md) you are ready to make gridpacks.
Go to base `genproductions` 
```
cd /ospool/cms-user/$USER/genproductions_run3/genproductions/
```
and enter the CC7 singularity with condor
```
cmssw-cc7-condor
```.
The first thing you'll need to do is unset the PERL5 libaries as this causses issues with CMSSW
```
unset PERL5LIB
```.
Next, change directories into the MG5 base
```
bin/MadGraph5_aMCatNLO/
```
and you can then start making your gridpacks.
For Run 3 gridpacks we are using `CMSSW_12_4_8` with `slc7_amd64_gcc10`.


# Producing Run 2 gridpacks for the multilepton analysis
The procedure for Run 2 gridpacks is almost identical to Run 3 except we use `cmssw-cc7-condor-python27`.
*Note*: make sure you are using the `master` branch which checks out the `mg265UL` branch of the genproductions tools.
