import os
import subprocess
import shutil
import random

from BatchType import BatchType
from ScanType import ScanType
from DegreeOfFreedom import DegreeOfFreedom
from helper_tools import *

from CardEditor import MGRunCard, MGCustomizeCard

# Class for configuring and setting up the submission for a single gridpack, can also run a produced gridpack tarball
class Gridpack(object):
    #def __init__(self,process,limits_name,proc_card,template_dir,stype=ScanType.NONE,btype=BatchType.NONE):
    def __init__(self,**kwargs):
        self.HOME_DIR      = os.getcwd()
        self.CARD_DIR      = os.path.join("addons","cards")
        self.LIMITS_DIR    = os.path.join("addons","limits")
        self.PROC_CARD_DIR = os.path.join("addons","cards","process_cards")
        self.GRIDRUN_DIR   = 'gridruns'

        # MadGraph specific card naming
        self.MG_PROC_CARD     = 'proc_card.dat'
        self.MG_CUSTOM_CARD   = 'customizecards.dat'
        self.MG_REWEIGHT_CARD = 'reweight_card.dat'
        self.MG_RUN_CARD      = 'run_card.dat'

        # The custom limits file for determining range of WC values
        self.LIMITS_FILE = "dim6top_LO_UFO_limits.txt"

        # These file name conventions are determined by genproductions scripts
        self.TARBALL_POSTFIX  = 'tarball'
        self.TARBALL_TYPE     = 'tar.xz'

        # These file name conventions have been freely chosen by us
        #   Note: Even though they were chosen arbitrarily, they are still used by code after
        #         the gridpack generation stage
        self.SCANFILE_POSTFIX = 'scanpoints'
        self.SCANFILE_TYPE    = 'txt'

        # Used when naming the final gridpack tarball
        self.CURR_ARCH        = 'slc6_amd64_gcc630'
        self.CURR_RELEASE     = 'CMSSW_9_3_0'

        # The script that is used to actually run the gridpack production
        self.GENPROD_SCRIPT   = 'gridpack_generation.sh'

        self.ops = {
            'btype': BatchType.NONE,
            'stype': ScanType.NONE,
            'process': None,
            'tag': 'Test',
            'run': 0,
            'coeffs': [],
            'start_pt': {},
            'num_rwgt_pts': 0,
            'runcard_ops': {},              # Options that should be used to overwrite in the run_card.dat file
            'limits_name': None,            # The process name as it appears in the limits file
            'process_card': None,           # The name of the process card to be used (e.g. ttHDecay.dat)
            'template_dir': None,           # The path (relative to the CARD_DIR) to the dir with the template run and customize cards
            'save_diagrams': False,         # Runs a modified version of the generation script that exits early to keep feynman diagrams
            'use_coupling_model': False,    # Use the 'coupling_orders' version of the dim6 model
            'coupling_string': None,        # If not None replaces "DIM6=1" with the specified string in the process card
            'replace_model': None,          # If not None overwrites the import model line of the process card
            'flavor_scheme': 5,
            'default_limits': [-10,10],
        }

        self.setOptions(**kwargs)

        self.mg_runcard = None
        self.mg_customizecard = None

        self.scan_pts = []
        self.is_configured = False
        return

    def hasOption(self,op_name):
        return self.ops.has_key(op_name)

    # Note: Some options are complex objects (e.g. lists/dicts) and so the returned dict will contain
    #       only refs to those objects
    def getOptions(self,*args):
        r = {}
        for op in args:
            if not self.hasOption(op): continue
            r[op] = self.ops[op]
        return r

    # Return the value of a single option or None if invalid option name
    def getOption(self,op):
        r = self.ops[op] if self.hasOption(op) else None
        return r

    def setOptions(self,**kwargs):
        for op,v in kwargs.iteritems():
            if not self.hasOption(op):
                print "[ERROR] Unable to set option. Unknown Option: {op}".format(op=op)
                raise RuntimeError
            self.ops[op] = v

    # Change the process associated with this Gridpack object
    def setProcess(self,p):
        self.setOptions(
            process=p.getName(),
            limits_name=p.getProcess(),
            process_card=p.getProcessCard(),
            template_dir=p.getTemplateDir(),
            flavor_scheme=p.getFlavorScheme(self.CARD_DIR)
        )

    def loadRunCard(self):
        """
            Parses a MadGraph run card, which can then be modified independent
            of the original template card
        """
        cdir = os.path.join(self.HOME_DIR,self.CARD_DIR,self.ops['template_dir'])
        self.mg_runcard = MGRunCard(card_name=self.MG_RUN_CARD,card_dir=cdir)

    def modifyRunCard(self,**ops):
        for op,val in ops.iteritems():
            if not self.mg_runcard.hasOption(op):
                print "[ERROR] Unknown run card option: {op}".format(op=op)
                raise RuntimeError
            self.mg_runcard.setOption(op,val)

    def saveRunCard(self):
        """
            Save the run card to the specified location, overwriting any pre-existing
            card in that location
        """
        setup = self.getSetupString()
        target_dir = self.getTargetDirectory(create=False)
        fpath = os.path.join(target_dir,"{setup}_{base}".format(setup=setup,base=self.MG_RUN_CARD))
        self.mg_runcard.save(fpath,force=True)
        return fpath

    def loadCustomizeCard(self):
        """
            Parses a customize card, which can then be modified independent
            of the original template card
        """
        cdir = os.path.join(self.HOME_DIR,self.CARD_DIR,self.ops['template_dir'])
        self.mg_customizecard = MGCustomizeCard(card_name=self.MG_CUSTOM_CARD,card_dir=cdir)

    def modifyCustomizeCard(self,*ops):
        """
            Appends additional options to the customize card. The inputs should each be strings
            of fully formed valid customize card options
        """
        for op in ops:
            self.mg_customizecard.setOption(op)

    def saveCustomizeCard(self):
        """
            Save the customize card to the appropriate location, overwriting any pre-existing
            card in that location
        """
        setup = self.getSetupString()
        target_dir = self.getTargetDirectory(create=False)
        fpath = os.path.join(target_dir,"{setup}_{base}".format(setup=setup,base=self.MG_CUSTOM_CARD))
        self.mg_customizecard.save(fpath,force=True,indent=1)
        return fpath

    def saveProcessCard(self,indent=0):
        """
            Save the process card to the appropriate location, overwriting any pre-existing
            card in that location

            NOTE: This function does a lot of stuff related to modifying the process card after
                it gets copied to the setup location
        """
        indent_str = " "*4*indent

        setup = self.getSetupString()
        target_dir = self.getTargetDirectory(create=False)
        proc_src = os.path.join(self.HOME_DIR,self.PROC_CARD_DIR,self.ops['process_card'])
        fpath = os.path.join(target_dir,"{setup}_{base}".format(setup=setup,base=self.MG_PROC_CARD))
        shutil.copy(proc_src,fpath)

        if self.ops['save_diagrams']:
            # Remove the nojpeg option from the output line of the process card
            print "{ind}Saving diagrams!".format(ind=indent_str)
            run_process(['sed','-i','-e',"s|SUBSETUP -nojpeg|SUBSETUP|g",fpath])

        if not self.ops['coupling_string'] is None:
            # Replace the amp order specification with a new custom one
            print "{ind}Custom Couplings: {couplings}".format(couplings=self.ops['coupling_string'],ind=indent_str)
            sed_str = "s|DIM6=1|{new}|g".format(new=self.ops['coupling_string'])
            run_process(['sed','-i','-e',sed_str,fpath])

        if self.ops['use_coupling_model']:
            # Replace the default dim6 model with the 'each_coupling_order' version
            # NOTE: This will overwrite the 'replace_model' option
            print "{ind}Using each_coupling_order model!".format(ind=indent_str)
            old = "dim6top_LO_UFO"
            new = "dim6top_LO_UFO_each_coupling_order"
            sed_str = "s|import model {old}|import model {new}|g".format(old=old,new=new)
            run_process(['sed','-i','-e',sed_str,fpath])

        if self.ops['replace_model']:
            rep_model = self.ops['replace_model']
            print "{ind}Using {model} model".format(model=rep_model,ind=indent_str)
            old = "dim6top_LO_UFO"
            sed_str = "s|import model {old}|import model {new}|g".format(old=old,new=rep_model)
            run_process(['sed','-i','-e',sed_str,fpath])

        # Replace SUBSETUP in the process card with the correct name
        sed_str = "s|SUBSETUP|{setup}|g".format(setup=setup)
        run_process(['sed','-i','-e',sed_str,fpath])
        return fpath

    def saveReweightCard(self):
        """
            Save the reweight card to the appropriate location, overwriting any pre-existing
            card in that location. This function currently does a lot of things, should probably
            break it up...
        """
        setup = self.getSetupString()
        target_dir = self.getTargetDirectory(create=False)

        scanfile = self.getScanfileString()
        rwgt_tar = os.path.join(target_dir,"{setup}_{base}".format(setup=setup,base=self.MG_REWEIGHT_CARD))
        
        if len(self.scan_pts) == 0:
            self.scan_pts = ScanType.getPoints(self.ops['coeffs'],self.ops['num_rwgt_pts'],self.ops['stype'])

        save_scan_points(scanfile,self.ops['coeffs'],self.scan_pts)
        make_reweight_card(rwgt_tar,self.ops['coeffs'],self.scan_pts)

        return rwgt_tar

    ################################################################################################
    def getSetupString(self):
        """ Construct the gridpack setup string (basically the name of the gridpack) """
        return "{proc}_{tag}_run{N:d}".format(proc=self.ops['process'],tag=self.ops['tag'],N=self.ops['run'])

    def getTarballString(self):
        """ Construct the tarball file string """
        setup = self.getSetupString()
        return "{setup}_{arch}_{release}_{tarpostfix}.{tartype}".format(
            setup=setup,
            arch=self.CURR_ARCH,
            release=self.CURR_RELEASE,
            tarpostfix=self.TARBALL_POSTFIX,
            tartype=self.TARBALL_TYPE
        )

    def getScanfileString(self):
        """ Construct the scanpoints file string """
        setup = self.getSetupString()
        return '%s_%s.%s' % (setup,self.SCANFILE_POSTFIX,self.SCANFILE_TYPE)

    def getGridrunOutputDirectory(self,create=False):
        """
            Returns the full path to the directory were unpacking and running of a generated gridpack
            will take place
        """
        if os.getcwd() != self.HOME_DIR:
            err_str = "Call to getGridrunOutputDirectory() when not in self.HOME_DIR!"
            err_str += "\n\tself.HOME_DIR: %s" % (self.HOME_DIR)
            err_str += "\n\tos.getcwd():   %s" % (os.getcwd())
            raise RuntimeError(err_str)
        if create and not os.path.exists(self.GRIDRUN_DIR):
            os.mkdir(self.GRIDRUN_DIR)
        process_subdir = os.path.join(self.GRIDRUN_DIR,self.ops['process'])
        if create and not os.path.exists(process_subdir):
            os.mkdir(process_subdir)
        setup = self.getSetupString()
        output_dir = os.path.join(process_subdir,"%s" % (setup))
        if create and not os.path.exists(output_dir):
            os.mkdir(output_dir)
        #return os.path.join(process_subdir,"%s" % (setup))
        return output_dir

    def getTargetDirectory(self,create=False):
        """
            Returns the full path to the directory were the genproductions framework will in order
            to read the MadGraph cards
        """
        if os.getcwd() != self.HOME_DIR:
            err_str = "Call to getTargetDirectory() when not in self.HOME_DIR!"
            err_str += "\n\tself.HOME_DIR: %s" % (self.HOME_DIR)
            err_str += "\n\tos.getcwd():   %s" % (os.getcwd())
            raise RuntimeError(err_str)
        process_subdir = os.path.join(self.CARD_DIR,"%s_cards" % (self.ops['process']))
        if create and not os.path.exists(process_subdir):
            os.mkdir(process_subdir)
        setup = self.getSetupString()
        target_dir = os.path.join(process_subdir,setup)
        if create and not os.path.exists(target_dir):
            os.mkdir(target_dir)
        return target_dir

    def limitSettings(self,header=True,depth=0):
        """ Print settings related to the limits used for setting values of the DoFs """
        indent = "\t"*depth
        info = ""
        if header: info += indent + "Limit Settings: %s\n" % (self.getSetupString())
        for c,dof in self.ops['coeffs'].iteritems():
            key = "%s_%s" % (self.ops['limits_name'],c)
            if header: info += "\t"
            info += indent + "%s: [" % (key.ljust(11))
            for idx,v in enumerate(dof.limits):
                fstr = "%.2f" % (v)
                if idx:
                    info += ","
                info += "%s" % (fstr.rjust(1+3+3)) # sign + 3 digits + 2 decimals + decimal symbol
            info += "]\n"
        return info

    def directorySettings(self,header=True,depth=0):
        """ Print the settings for various directories to be used by the genproductions framework """
        indent = "\t"*depth
        info = ""
        if header: 
            info += indent + "Directory Settings: %s\n" % (self.getSetupString())
            indent += "\t"
        info += indent + "Home Dir    : %s\n" % (self.HOME_DIR)
        info += indent + "Target Dir  : %s\n" % (os.path.join(".",self.getTargetDirectory()))
        info += indent + "Template Dir: %s\n" % (os.path.join(".",os.path.join(self.CARD_DIR,self.ops['template_dir'])))
        info += indent + "Gridrun Dir : %s\n" % (os.path.join(".",self.getGridrunOutputDirectory()))
        return info

    def baseSettings(self,header=True,depth=0):
        """ Print a pruned down list of settings for this gridpack instance """
        indent = "\t"*depth
        info = ""
        if header: 
            info += indent + "Base Settings: %s\n" % (self.getSetupString())
            depth += 1
            indent += "\t"
        else:
            info += indent + "Setup: %s\n" % (self.getSetupString())
        info += indent + "Process     : %s\n" % (self.ops['process'])
        info += indent + "Process Card: %s\n" % (self.ops['process_card'])
        info += indent + "FlavorScheme: %s\n" % (self.ops['flavor_scheme'])
        info += indent + "ScanType    : %s\n" % (self.ops['stype'])
        info += indent + "BatchType   : %s\n" % (self.ops['btype'])
        info += indent + "Rwgt Points : %d\n" % (self.ops['num_rwgt_pts'])
        info += indent + "Scan Points : %d\n" % (len(self.scan_pts))
        info += self.limitSettings(header=True,depth=depth)
        return info

    # WIP
    def configureSettings(self,header=True,depth=0):
        """ Print only the configure related settings for this gridpack instance """
        indent = "\t"*depth
        info = ""
        if header: 
            info += indent + "Configure gridpack: %s" % (self.getSetupString())
            indent += "\t"
        info += indent + ""

        info += "\n"
        return info

    def allSettings(self,header=True,depth=0):
        """ Print all settings for this gridpack instance """
        indent = "\t"*depth
        info = ""
        if header: 
            info += indent + "All Settings: %s\n" % (self.getSetupString())
            depth += 1
            indent += "\t"
        else:
            info += indent + "Setup: %s\n" % (self.getSetupString())
        info += indent + "Process     : %s\n" % (self.ops['process'])
        info += indent + "Limits Name : %s\n" % (self.ops['limits_name'])
        info += indent + "Process Card: %s\n" % (self.ops['process_card'])
        info += indent + "ScanType    : %s\n" % (self.ops['stype'])
        info += indent + "BatchType   : %s\n" % (self.ops['btype'])
        info += indent + "Tarball File: %s\n" % (self.getTarballString())
        info += indent + "Scan File   : %s\n" % (self.getScanfileString())
        info += indent + "Rwgt Points : %d\n" % (self.ops['num_rwgt_pts'])
        info += indent + "Scan Points : %d\n" % (len(self.scan_pts))
        info += self.directorySettings(header=False,depth=depth)
        info += self.limitSettings(header=True,depth=depth)
        return info

    ################################################################################################

    def exists(self):
        """ 
            Checks for the existence of certain files/directories in order to determine if this
            gridpack configuration has already been produced (or is in the process of being produced)
        """
        if os.getcwd() != self.HOME_DIR:
            err_str  = "Call to exists() when not in self.HOME_DIR!"
            err_str += "\n\tself.HOME_DIR: %s" % (self.HOME_DIR)
            err_str += "\n\tos.getcwd():   %s" % (os.getcwd())
            raise RuntimeError(err_str)
        has_setup_dir = os.path.exists(self.getSetupString())
        has_tarball   = os.path.exists(self.getTarballString())
        has_scanfile  = os.path.exists(self.getScanfileString())
        has_gridrun   = os.path.exists(self.getGridrunOutputDirectory())
        return (has_setup_dir or has_tarball or has_gridrun or has_scanfile)

    def configure(self,tag,run,dofs,num_pts,start_pt={},scan_file=None):
        """ Parses options to produce gridpack in a particular way. """
        if len(self.ops['default_limits']) != 2:
            print "Invalid input for default limits!"
            self.is_configured = False
            return

        self.ops['tag'] = tag
        self.ops['run'] = run
        self.ops['coeffs'] = {}
        for dof in dofs:    # Convert list of WCs to a dictionary
            self.ops['coeffs'][dof.getName()] = dof
        coeffs = self.getOption('coeffs')   # Should probably add check for None

        if scan_file:
            # Set starting point and rwgt points based on a scanpoints file
            self.scan_pts = []
            pts = parse_scan_file(scan_file)
            missing_wc = []
            extra_wc = []
            for idx,pt in enumerate(pts):
                new_pt = {}
                for k,v in pt.iteritems():
                    # Keep only the WCs which have been specified
                    if self.ops['coeffs'].has_key(k):
                        new_pt[k] = v
                    else:
                        extra_wc.append(k)
                if idx == 0:
                    # Set the starting point from the scanpoints file
                    for k in self.ops['coeffs'].keys():
                        if not new_pt.has_key(k):
                            # Any WCs which are missing from the scanpoints file are set to SM value
                            missing_wc.append(k)
                            self.ops['coeffs'][k].setLimits(0,0,0)
                        else:
                            self.ops['coeffs'][k].setLimits(new_pt[k],0,0)
                else:
                    self.scan_pts.append(new_pt)
            if len(missing_wc):
                print "[WARNING] Scanpoints file is missing WCs used in this gridpack configuration, %s" % (str(missing_wc))
            if len(extra_wc):
                print "[WARNING] Scanpoints file has WCs that were not specified in this gridpack configuration, their values will be set to SM."
                print "\t%s" % (str(extra_wc)) 
            self.ops['num_rwgt_pts'] = len(self.scan_pts)
        else:
            self.scan_pts = []  # Clear the scan_pts array incase it was used previously

        if len(self.scan_pts) == 0:
            # The scan points will need to be set automatically
            if num_pts > 0:
                # Make sure we have enough points to reconstruct the parametrization
                if self.ops['stype'] == ScanType.FRANDOM:
                    N = len(self.ops['coeffs'].keys())
                    num_pts = max(num_pts,1.2*(1+2*N+N*(N-1)/2))
                elif self.ops['stype'] == ScanType.SLINSPACE:
                    num_pts = max(num_pts,3)
                num_pts = int(num_pts)
            self.ops['num_rwgt_pts'] = num_pts

            wc_limits = parse_limit_file(os.path.join(self.LIMITS_DIR,self.LIMITS_FILE))
            for idx,c in enumerate(self.ops['coeffs'].keys()):
                # Set the limits based on limits file (if needed/possible)
                if self.ops['coeffs'][c].hasLimits():
                    # The dof already has limits set
                    continue
                key = "%s_%s" % (self.ops['limits_name'],c)
                if wc_limits.has_key(key):
                    # Use limits based on those found in the limits file
                    low  = round(wc_limits[key][0],6)
                    high = round(wc_limits[key][1],6)
                else:
                    # The WC doesn't exist in the limits file, so use defaults
                    low,high = self.ops['default_limits']
                if start_pt.has_key(c):
                    strength = start_pt[c]
                else:
                    strength = calculate_start_point(low,high,1.25)
                self.ops['coeffs'][c].setLimits(strength,low,high)
        self.is_configured = True
        return

    def setup(self,indent=0):
        """
            Sets up and/or creates the needed directories and files need for creating a gridpack
            using the genproductions framework
        """
        BatchType.isValid(self.ops['btype'])
        ScanType.isValid(self.ops['stype'])

        os.chdir(self.HOME_DIR)

        setup = self.getSetupString()
        if self.exists():
            print "{0:>{w}}Skipping gridpack setup: {setup}".format("",setup=setup,w=4*indent)
            return False

        if self.ops['save_diagrams'] and self.ops['btype'] != BatchType.LOCAL:
            print "[ERROR] Invalid BatchType for saving diagrams: {btype}".format(btype=self.ops['btype'])
            return False

        if self.ops['stype'] == ScanType.NONE:
            # Don't do any reweighting
            self.scan_pts = []

        print "{0:>{w}}Setup gridpack: {setup}...".format("",setup=setup,w=4*indent)

        # Set the random seed adding extra events to the pilotrun
        # NOTE: This physically modifies the gridpack generation script
        seed = int(random.uniform(1,1e6))
        print "{ind:>{w}}Seed: {seed:d}".format(seed=seed,ind="",w=4*(indent+1))
        sed_str = "s|RWSEED=[0-9]*|RWSEED={seed:d}|g".format(seed=seed)
        run_process(['sed','-i','-e',sed_str,self.GENPROD_SCRIPT])

        target_dir = self.getTargetDirectory(create=False)
        if os.path.exists(target_dir):
            print "{0:>{w}}NOTE: The cards directory already exists, will overwrite existing cards.".format("",w=4*(indent+1))
        else:
            # Create the needed directories
            self.getTargetDirectory(create=True)

        #customize_src = os.path.join(self.HOME_DIR,self.CARD_DIR,self.ops['template_dir'],self.MG_CUSTOM_CARD)
        #customize_tar = os.path.join(target_dir,"%s_%s" % (setup,self.MG_CUSTOM_CARD))
        #shutil.copy(customize_src,customize_tar)

        #run_src = os.path.join(self.HOME_DIR,self.CARD_DIR,self.ops['template_dir'],self.MG_RUN_CARD)
        #run_tar = os.path.join(target_dir,"%s_%s" % (setup,self.MG_RUN_CARD))
        #shutil.copy(run_src,run_tar)

        #proc_src = os.path.join(self.HOME_DIR,self.PROC_CARD_DIR,self.ops['process_card'])
        #proc_tar = os.path.join(target_dir,"{setup}_{base}".format(setup=setup,base=self.MG_PROC_CARD))
        #shutil.copy(proc_src,proc_tar)

        self.loadCustomizeCard()
        self.loadRunCard()

        extra_customize_ops = []
        if self.ops['flavor_scheme'] == 5:
            extra_customize_ops.append('set param_card MB 0.0')
            extra_customize_ops.append('set param_card ymb 0.0')
        for c,dof in self.ops['coeffs'].iteritems():
            for k,v in dof.eval(dof.getStart()).iteritems():
                extra_customize_ops.append('set param_card {wc} {val:.6f}'.format(wc=k,val=v))
        self.modifyCustomizeCard(*extra_customize_ops)
        self.modifyRunCard(**self.ops['runcard_ops'])

        customize_tar = self.saveCustomizeCard()
        run_tar       = self.saveRunCard()
        rwgt_tar      = self.saveReweightCard()                 # NOTE: Can potentially modify self.scan_pts
        proc_tar      = self.saveProcessCard(indent=indent+1)   # NOTE: This makes a lot of modifcations to the card after copying

        # Sets the initial WC phase space point for MadGraph to start from (appends to customize card)
        #set_initial_point(customize_tar,self.ops['coeffs'],flavor_scheme=self.ops['flavor_scheme'])

        #scanfile = self.getScanfileString()
        #rwgt_tar = os.path.join(target_dir,"%s_%s" % (setup,self.MG_REWEIGHT_CARD))
        #if len(self.scan_pts) == 0:
        #    self.scan_pts = ScanType.getPoints(self.ops['coeffs'],self.ops['num_rwgt_pts'],self.ops['stype'])
        #save_scan_points(scanfile,self.ops['coeffs'],self.scan_pts)
        #make_reweight_card(rwgt_tar,self.ops['coeffs'],self.scan_pts)

        #if self.ops['save_diagrams']:
        #    # Remove the nojpeg option from the output line of the process card
        #    print "\tSaving diagrams!"
        #    run_process(['sed','-i','-e',"s|SUBSETUP -nojpeg|SUBSETUP|g",proc_tar])
        #if not self.ops['coupling_string'] is None:
        #    print "\tCustom Couplings: %s" % (self.ops['coupling_string'])
        #    run_process(['sed','-i','-e',"s|DIM6=1|%s|g" % (self.ops['coupling_string']),proc_tar])
        #if self.ops['use_coupling_model']:
        #    print "\tUsing each_coupling_order model!"
        #    run_process(['sed','-i','-e',"s|import model dim6top_LO_UFO|import model dim6top_LO_UFO_each_coupling_order|g",proc_tar])
        #if self.ops['replace_model']:
        #    rep_model = self.ops['replace_model']
        #    print "\tUsing %s model" % (rep_model)
        #    run_process(['sed','-i','-e',"s|import model dim6top_LO_UFO|import model %s|g" % (rep_model),proc_tar])
        ## Replace SUBSETUP in the process card
        #run_process(['sed','-i','-e',"s|SUBSETUP|%s|g" % (setup),proc_tar])
        return True

    def clean(self):
        """ Remove all folders/files created by the setup()/submit() methods """
        if not self.is_configured:
            print "The gridpack has not been configured yet, so no cleaning can be done!"
            return

        os.chdir(self.HOME_DIR)

        print "Cleaning files related to current gridpack configuration: %s" % (self.getSetupString())
        target_dir = self.getTargetDirectory(create=False)
        if os.path.exists(target_dir) and os.path.isdir(target_dir):
            # This is where the modified madgraph cards are stored
            print "\tRemoving existing directory: %s " % (target_dir)
            shutil.rmtree(target_dir)

        setup_dir = self.getSetupString()
        if os.path.exists(setup_dir) and os.path.isdir(setup_dir):
            # This is the directory that gets created by the setup_production.sh script (in LOCAL or CMSCONNECT mode)
            print "\tRemoving existing directory: %s " % (setup_dir)
            shutil.rmtree(setup_dir)

        gridrun_dir = self.getGridrunOutputDirectory()
        if os.path.exists(gridrun_dir) and os.path.isdir(gridrun_dir):
            # This is the directory that is used to unpack and run a gridpack tarball
            print "\tRemoving existing directory: %s " % (gridrun_dir)
            shutil.rmtree(gridrun_dir)

        tarball_file = self.getTarballString()
        if os.path.exists(tarball_file) and not os.path.isdir(tarball_file):
            # This is the tarball created by the setup_production.sh script
            print "\tRemoving existing file: %s" % (tarball_file)
            os.remove(tarball_file)

        scanpoints_file = self.getScanfileString()
        if os.path.exists(scanpoints_file) and not os.path.isdir(scanpoints_file):
            # This is the txt file which contains the recorded starting point and list of madgraph rwgt points
            print "\tRemoving existing file: %s" % (scanpoints_file)
            os.remove(scanpoints_file)

        log_file = "%s.log" % (self.getSetupString())
        if os.path.exists(log_file) and not os.path.isdir(log_file):
            # This is the log file created by the setup_production.sh script
            print "\tRemoving existing file: %s" % (log_file)
            os.remove(log_file)

        debug_file = "%s.debug" % (self.getSetupString())
        if os.path.exists(debug_file) and not os.path.isdir(debug_file):
            # This is the debug file created by the setup_production.sh script (only in CMSCONNECT mode)
            print "\tRemoving existing file: %s" % (debug_file)
            os.remove(debug_file)

        codegen_file = "%s_codegen.log" % (self.getSetupString())
        if os.path.exists(codegen_file) and not os.path.isdir(codegen_file):
            # This is the codegen log file created by the setup_production.sh script (only in CMSCONNECT mode)
            print "\tRemoving existing file: %s" % (codegen_file)
            os.remove(codegen_file)

        self.is_configured = False

    def submit(self):
        """ Run one of genproductions gridpack generation scripts """
        setup = self.getSetupString()
        target_dir = self.getTargetDirectory()
        btype = self.ops['btype']
        if not os.path.exists(target_dir):
            print "[ERROR] Can't find target directory, %s" % (target_dir)
            return False
        print "Submit gridpack: %s..." % (setup)
        print "\tBatchType: %s" % (btype)
        if btype == BatchType.LOCAL:
            # For interactive/serial running
            if self.ops['save_diagrams']:
                run_process(['./diagram_generation.sh',setup,target_dir])
            else:
                run_process(['./gridpack_generation.sh',setup,target_dir,"local","ALL",self.CURR_ARCH,self.CURR_RELEASE])
            return True
        elif btype == BatchType.LSF:
            # For batch running
            run_process(['./submit_gridpack_generation.sh','15000','15000','1nd',setup,target_dir,'8nh'])
            return True
        elif btype == BatchType.CMSCONNECT:
            # For cmsconnect running
            debug_file = "%s.debug" % (setup)
            cmsconnect_cores = 1
            print '\tCurrent PATH: {0}'.format(os.getcwd())
            print '\tWill execute: ./submit_cmsconnect_gridpack_generation.sh {setup} {dir} {cores} "{mem}" {arch} {release}'.format(
                setup=setup,
                dir=target_dir,
                cores=str(cmsconnect_cores),
                mem="15 Gb",
                arch=self.CURR_ARCH,
                release=self.CURR_RELEASE
            )
            subprocess.Popen(
                ["./submit_cmsconnect_gridpack_generation.sh",setup,target_dir,str(cmsconnect_cores),"15 Gb",self.CURR_ARCH,self.CURR_RELEASE],
                stdout=open(debug_file,'w'),
                stderr=subprocess.STDOUT
            )
            return True
        elif btype == BatchType.CONDOR:
            # Not currently working
            print "\tCondor running is not currently working. Sorry!"
            #run_process(['./submit_condor_gridpack_generation.sh',setup,target_dir])
            return True
        elif btype == BatchType.NONE:
            print "\tSkipping gridpack generation, %s" % (setup)
            return True
        return False

    def run(self,events,seed,cores):
        """ Unapack and run an existing gridpack to produce events in an LHE file """
        os.chdir(self.HOME_DIR)

        setup = self.getSetupString()
        print "Running Gridpack: %s" % (setup)
        print "\tSetting up directories..."

        output_dir = self.getGridrunOutputDirectory(create=False)
        if os.path.exists(output_dir):
            print "Removing existing output directory: %s" % (output_dir)
            shutil.rmtree(output_dir)
        output_dir = self.getGridrunOutputDirectory(create=True)
        #if os.path.exists(output_dir):
        #    # We already ran the gridpack once!
        #    print "Output directory already exists, skipping gridpack run: %s" % (setup)
        #    return
        #else:
        #    os.mkdir(output_dir)

        tarball = self.getTarballString()
        if not os.path.exists(tarball):
            print "No tarball file found! Skipping..."
            return
        #print "\tMoving tarball..."
        #shutil.move(tarball,output_dir)

        print "\tExtracting tarball..."
        run_process(['tar','xaf',tarball,'-C',output_dir])

        os.chdir(output_dir)

        #print "\tExtracting tarball..."
        #run_process(['tar','xaf',tarball])

        print "\tRunning gridpack..."
        run_process(['./runcmsgrid.sh',str(events),str(seed),str(cores)])

        os.chdir(self.HOME_DIR)
        return

if __name__ == "__main__":
    gridpack = Gridpack(
        process='ttllDecay',
        limits_name='ttll',
        proc_card='ttllDecay.dat',
        template_dir='template_cards/defaultPDFs_template',
        stype=ScanType.NONE,
        btype=BatchType.NONE
    )

    ctG  = DegreeOfFreedom(name='ctG'  ,relations=[['ctG'] ,1.0])
    ctW  = DegreeOfFreedom(name='ctW'  ,relations=[['ctW'] ,1.0])
    ctei = DegreeOfFreedom(name='ctei' ,relations=[['cte1','cte2','cte3'],1.0])

    dof_list = [ctG,ctW,ctei]

    ################################################################################################
    # Example using Gridpack class
    pt = {}
    for dof in dof_list:
        dof.setLimits(4.0,-50.0,50.0)   # Will force the code to use these limits instead of from the limits file
        pt[dof.getName()] = 4.0
    gridpack.configure(
        tag='ExampleTagName',
        run=0,
        dofs=dof_list,
        num_pts=10,
        start_pt=pt     # Optional, if not set will select starting strength for each WC randomly
    )
    if not gridpack.exists():
        result = gridpack.setup()
        result = gridpack.submit()
    ################################################################################################
    # Example generating multiple gridpacks at different 1-D starting points
    for dof in dof_list:
        tag = dof.getName() + 'ExampleTagName'
        dof_subset = [dof]
        for idx,v in enumerate(linspace(-50.0,50.0,5)):
            gridpack.configure(
                tag=tag,
                run=idx,
                dofs=dof_subset,
                num_pts=10
            )
            if not gridpack.exists():
                result = gridpack.setup()
                result = gridpack.submit()
    ################################################################################################
    # Example generating multiple gridpacks at random n-D starting points
    tag = 'ExampleTagName'
    for idx in range(5):
        pt = {}
        for dof in dof_list:
            pt[dof.getName()] = calculate_start_point(-50.0,50.0)
        gridpack.configure(
            tag=tag,
            run=idx,
            dofs=dof_list,
            num_pts=10,
            start_pt=pt
        )
        if not gridpack.exists():
            result = gridpack.setup()
            result = gridpack.submit()

