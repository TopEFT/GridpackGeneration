import os
import subprocess
from helpers.helper_tools import regex_match,run_process

#NOTE: This is meant to transfer two files in the format: p_c_r_scanpoints.txt and p_c_r_*_tarball.tar.xz

# voms-proxy-init -voms cms -valid 192:00

MAX_TRANSFERS = 999  # Limit the number of transfers per code running
USERNAME = 'awightma'
SUB_DIR = '2019_04_19'

def main():
    dry_run = True

    good_fname = 'good_copies.log'
    bad_fname = 'failed_copies.log'

    protocol = 'gsiftp://'
    tar_host = 'deepthought.crc.nd.edu'
    tar_dir = '/store/user/{user}/gridpack_scans/{subdir}/'.format(user=USERNAME,subdir=SUB_DIR)
    scan_dir = '/scanpoints/'
    failed_copies = []
    good_copies = []

    indent_lvl = 1
    indent = "\t"*indent_lvl

    p_wl = []
    c_wl = []
    r_wl = []

    transfer_files = getFilesToTransfer('.',p_wl=p_wl,c_wl=c_wl,r_wl=r_wl)
    for idx,fn in enumerate(transfer_files):
        if idx > MAX_TRANSFERS:
            break
        bad_copy = False
        remote_fn = protocol+tar_host+tar_dir+fn
        if "_scanpoints.txt" in fn:
            remote_fn = protocol+tar_host+tar_dir+scan_dir+fn

        print "#"*100
        print "[%d/%d] Transfering File: %s" % (idx+1,len(transfer_files),fn)
        
        local_sz      = getFileSize(fn)
        local_chksum  = getCheckSum(fn)

        if not dry_run:
            remote_sz     = getFileSize(remote_fn)
            remote_chksum = getCheckSum(remote_fn) if remote_sz != -1 else -1
        else:
            remote_sz = -1
            remote_chksum = -1

        if remote_chksum == local_chksum:
            # The file is already present and has correct checksum
            print "%sRemote file already exists, skipping..." % (indent)
            print ""
            continue

        print "%sTarget: %s" % (indent,remote_fn)
        print "%sSize: %.2f MB" % (indent,float(local_sz)/(1024*1024))

        if not dry_run:
            try:
                stdout_arr = run_process(['gfal-copy','-fp',fn,remote_fn],indent=1)
                copied_chksum = getCheckSum(remote_fn)
            except KeyboardInterrupt:
                print "Ending early!"
                failed_copies.append(fn)
                break
        else:
            copied_chksum = -1

        if copied_chksum != local_chksum:
            print "%sResult: FAILED" % (indent)
            failed_copies.append(fn)
        else:
            print "%sResult: SUCCESS" % (indent)
            good_copies.append(fn)
        print "%sDone!" % (indent)

    with open(bad_fname,'w') as f:
        f.write('failed copies:\n')
        for fname in failed_copies:
            f.write(fname)
            f.write('\n')

    with open(good_fname,'w') as f:
        f.write('good copies:\n')
        for fname in good_copies:
            f.write(fname)
            f.write('\n')
    return

# Get a list of all (local) files to transfer
def getFilesToTransfer(fdir='.',p_wl=[],c_wl=[],r_wl=[]):
    search_strs = ['.*_tarball\.tar\.xz','.*_scanpoints\.txt']
    files = []
    arr = getLocalFiles(fdir)
    for idx,f in enumerate(arr):
        if len(regex_match([f],search_strs)) == 0:
            # The file does not contain any of the search strings
            continue
        arr = f.split('_')
        if len(arr) < 3:
            continue
        p,c,r = arr[:3]

        if len(regex_match([p],p_wl)) == 0:
            continue
        elif len(regex_match([c],c_wl)) == 0:
            continue
        elif len(regex_match([r],r_wl)) == 0:
            continue

        cross_checks = [
            "%s_%s_%s_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz" % (p,c,r),
            "%s_%s_%s_scanpoints.txt" % (p,c,r)
        ]
        if not os.path.exists(cross_checks[0]) or not os.path.exists(cross_checks[1]):
            # The file is missing a complement
            continue
        files.append(f)
    return files

# Get a list of local files in a directory
def getLocalFiles(fdir='.'):
    files = []
    for idx,f in enumerate(os.listdir(fdir)):
        if os.path.isdir(f):
            continue
        files.append(f)
    return files

# Get a list of files from a remote directory
def getRemoteFiles(fdir):
    # NOTE: Not currently finished!
    files = []
    arr = run_process(['gfal-ls',fdir],verbose=True)
    print arr

    return files

# Returns the target file size using gfal-stat
def getFileSize(f):
    arr = run_process(['gfal-stat',f],verbose=False)
    if len(arr) < 2:
        return -1

    if not 'Size: ' in arr[1]:
        return -1

    return int(arr[1].split('\t')[0][6:])

# Returns the MD5 checksum of target file using gfal-sum
def getCheckSum(f):
    arr = run_process(['gfal-sum',f,'MD5'],verbose=False)
    if len(arr) != 1:
        return -1
    return arr[0].split()[1]

#def run_process(inputs,verbose=True,indent=0):
#    indent_str = "\t"*indent
#    if verbose:
#        print indent_str+"Command: "+" ".join(inputs)
#    p = subprocess.Popen(inputs,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
#    stdout = []
#    while True:
#        l = p.stdout.readline()
#        if l == '' and p.poll() is not None:
#            break
#        if l:
#            stdout.append(l.strip())
#            if verbose: print indent_str+l.strip()
#    return stdout


if __name__ == "__main__":
    main()
