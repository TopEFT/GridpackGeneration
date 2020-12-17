import os
import shutil
import subprocess

# This script is used to move the feynman diagrams produced by running MadGraph to some desired location for easier browsing/viewing
# NOTE: The MadGraph runs need to follow the p_c_r_* style naming convention for proper identification!

# Example output dir:
#OUTPUT_DIRECTORY = "/afs/cern.ch/user/a/awightma/www/eft_analysis/diagrams"

# Search the specified locations for directories corresponding to MadGraph runs
def getProcessDirectories(path='.',p_wl=[],c_wl=[],r_wl=[]):
    dir_paths = []
    if not os.path.exists(path):
        print "[ERROR] Path does not exists: %s" % (path)
        return dir_paths
    for idx,f in enumerate(os.listdir(path)):
        tmp_path = os.path.join(path,f)
        if not os.path.isdir(tmp_path):
            continue
        arr = f.split('_')
        if len(arr) != 3:
            continue
        p,c,r = arr
        if not "run" in r:
            continue
        elif len(p_wl) > 0 and not p in p_wl:
            continue
        elif len(c_wl) > 0 and not c in c_wl:
            continue
        elif len(r_wl) > 0 and not r in r_wl:
            continue
        dir_paths.append(tmp_path)
    return dir_paths

# Determine all the SubProcess directories in the MadGraph work area
def getSubProcessDirectories(path):
    dir_paths = []
    if not os.path.exists(path):
        print "[ERROR] Path does not exist %s" % (path)
        return dir_paths
    for idx,f in enumerate(os.listdir(path)):
        tmp_path = os.path.join(path,f)
        if not os.path.isdir(tmp_path):
            continue
        elif len(f.split('_')) < 2:
            continue
        #elif f[:2] != "P0" and f[:2] != "P1":
        elif f[:1] != "P":
            print "\nSkipping dir:" , f , "did you mean to do this?\n"
            #TODO: Change this to be more robust (e.g. via regex or something)
            continue
        dir_paths.append(tmp_path)
    return dir_paths

# Get all files from a particular directory (optionally specify an extension to filter on)
def getFiles(path,ext=None):
    files = []
    for idx,f in enumerate(os.listdir(path)):
        tmp_path = os.path.join(path,f)
        if not os.path.isfile(tmp_path):
            continue
        elif ext and os.path.splitext(tmp_path)[1] != ext:
            continue
        files.append(tmp_path)
    return files

# create an output directory at the specified location, with the needed sub-directories
def makeOutputDirectory(path,out_path):
    target_dir = None
    h,t = os.path.split(path)
    if not os.path.exists(h):
        print "[ERROR] Requested parent directory does not exist: %s" % (h)
        return target_dir
    
    if not os.path.exists(path):
        print "[INFO] Creating process output directory: %s" % (path)
        os.mkdir(path)

    subprocess_name = os.path.split(out_path)[1]
    if subprocess_name == "":
        print "[ERROR] Unable to get subprocess directory for %s" % (out_path)
        return target_dir
    target_dir = os.path.join(path,subprocess_name)
    if not os.path.exists(target_dir):
        print "[INFO] Creating SubProcess output directory: %s" % (target_dir)
        os.mkdir(target_dir)
    return target_dir

# Move the .ps files from one directory to another (matching) directory
def transferFiles(source_dirs,target_dirs):
    copied_files = []
    for sd in source_dirs:
        if not os.path.exists(sd):
            print "[WARNING] Source directory missing: %s" % (sd)
            continue
        sh,st = os.path.split(sd)
        match = None
        for td in target_dirs:
            if not os.path.exists(td):
                print "[WARNING] Target directory missing: %s" % (td)
                continue
            th,tt = os.path.split(td)
            if st == tt:
                match = td
                break
        if match is None:
            print "[WARNING] Unable to find matching target directory for %s" % (st)
            continue
        files = getFiles(sd,'.ps')
        for fsource in files:
            fh,ft = os.path.split(fsource)
            ftarget = os.path.join(match,ft)
            print "[INFO] Copying '%s' to '%s'" % (ft,match)
            shutil.copyfile(fsource,ftarget)
            cleanDiagram(ftarget)
            copied_files.append([fsource,ftarget])
    return copied_files

# Clean the matrix.ps postscript file in order to make things more readable
def cleanDiagram(fpath):
    fname = os.path.basename(fpath)
    if not os.path.exists(fpath): return
    elif not os.path.isfile(fpath): return
    elif not fname.endswith('.ps') or not 'matrix' in fname: return
    print "[INFO] Cleaning: %s" % (fpath)
    # NOTE: The order of these calls matters (namely the first two calls need to be first)!
    subprocess.check_call(['sed','-i','-e','s| FCNC_[Aa-Zz0-9]*=0,||g',fpath])    # Remove any instance of the string ' FCNC_XYZ###=0,'
    subprocess.check_call(['sed','-i','-e','s| DIM6_[Aa-Zz0-9]*=0,||g',fpath])    # Remove any instance of the string ' DIM6_XYZ###=0,'
    subprocess.check_call(['sed','-i','-e','s| FCNC=0,||g',fpath])                # Remove any instance of the specific string ' FCNC=0,'
    subprocess.check_call(['sed','-i','-e','s|DIM6_||g'   ,fpath])                # Remove the 'DIM6_' prefix from the diagram
    #subprocess.check_call(['sed','-i','-e','s|DIM6=1, ||g',fpath])                # Remove uneeded 'DIM6=1' strings from the diagram
    return

# Transfers the Feynman diagrams from a particular MadGraph run to some output directory location
def transferDiagrams(path):
    source = os.path.split(path)[1]
    print "[INFO] Transfering Feynman diagrams: %s" % (source)
    p,c,r = source.split('_')
    source_path = os.path.join('./',source)
    target_path = os.path.join(OUTPUT_DIRECTORY,"%s_%s" % (p,c))
    source_dirs = getSubProcessDirectories(source_path)
    target_dirs = []
    for d in source_dirs:
        result = makeOutputDirectory(target_path,d)
        if result:
            target_dirs.append(result)
    copied_files = transferFiles(source_dirs,target_dirs)
    return copied_files

def main():
    p_wl = []
    c_wl = []
    r_wl = []
    sources = getProcessDirectories(path='.',p_wl=p_wl,c_wl=c_wl,r_wl=r_wl)
    for s in sources:
        transferDiagrams(s)

if __name__ == "__main__":
    main()
