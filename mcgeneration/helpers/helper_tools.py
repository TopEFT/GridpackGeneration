import itertools
import random
import subprocess
import shutil
import re

# Pipes subprocess messages to STDOUT
def run_process(inputs,verbose=True,indent=0):
    # Note: This will hold the main thread and wait for the subprocess to complete
    indent_str = "\t"*indent
    p = subprocess.Popen(inputs,stdout=subprocess.PIPE)
    stdout = []
    while True:
        l = p.stdout.readline()
        if l == '' and p.poll() is not None:
            break
        if l:
            stdout.append(l.strip())
            if verbose: print indent_str+l.strip()
    return stdout

def find_process(p_name,p_lst):
    for p in p_lst:
        if p.getName() == p_name:
            return p
    return None

# Returns a list of linear spaced numbers (implementation of numpy.linspace)
def linspace(start,stop,num,endpoint=True,acc=7):
    if num < 0:
        raise ValueError("Number of samples, %s, must be non-negative." % num)
    acc = max(0,acc)
    acc = min(15,acc)
    div = (num - 1) if endpoint else num
    delta = stop - start
    if num > 1:
        step = float(delta) / div
        y = [round((start + step*idx),acc) for idx in range(num)]
    elif num == 1:
        y = [start]
    else:
        y = []
    if endpoint and num > 1:
        y[-1] = stop
    return y

# Checks if two W.C. phase space points are identical
def check_point(pt1,pt2):
    for k,v in pt1.iteritems():
        if not pt2.has_key(k):
            pt2[k] = 0.0    # pt2 is missing the coeff, add it and set it to SM value
        if v != pt2[k]:
            return False
    return True

# Sets the initial W.C. phase space point for MadGraph to start from (appends to customize card)
def set_initial_point(file_name,dofs,flavor_scheme=5):
    with open(file_name,'a') as f:
        if flavor_scheme == 5:
            f.write('set param_card MB 0.0 \n')
            f.write('set param_card ymb 0.0 \n')
        for c,dof in dofs.iteritems():
            for k,v in dof.eval(dof.getStart()).iteritems():
                f.write("set param_card %s %.6f \n" % (k,v))
        f.write('\n')
    return file_name

# Create the MadGraph reweight card with scans over the specified W.C. phase space points
def make_reweight_card(file_name,dofs,pts):
    # pts = [{c1: 1.0, c2: 1.0, ...}]
    header  = ""
    header += "#******************************************************************\n"
    header += "#                       Reweight Module                           *\n"
    header += "#******************************************************************\n"
    header += "\nchange rwgt_dir rwgt\n"

    if len(pts) == 0:
        return file_name

    with open(file_name,'w') as f:
        f.write(header)
        # This is a workaround for the MG bug causing first point to not be renamed
        f.write("\nlaunch --rwgt_name=dummy_point")
        c = dofs.keys()[0]
        for k,v in dofs[c].eval(0.0123).iteritems():
            f.write("\nset %s %.6f" % (k,v))
        f.write("\n")

        for idx,pt in enumerate(pts):
            rwgt_str = "EFTrwgt%d" % (idx)
            for k,v in pt.iteritems():
                rwgt_str += '_' + k + '_' + str(round(v,6))
            f.write("\nlaunch --rwgt_name=%s" % (rwgt_str))
            for k1,v1 in pt.iteritems():
                for k2,v2 in dofs[k1].eval(v1).iteritems():
                    f.write("\nset %s %.6f" % (k2,v2))
            f.write("\n")

# Reads a limit file and returns a dictionary mapping the WCs to their respective high,low limits to use
def parse_limit_file(fpath):
    wc_limits = {}
    with open(fpath,'r') as f:
        for l in f:
            arr = l.split()
            if len(arr) != 3:
                continue
            wc_limits[arr[0]] = [float(arr[1]),float(arr[2])]
    return wc_limits

# Note: The returned list will contain the MG starting point as the first element!
def parse_scan_file(fpath):
    pts = []
    with open(fpath,'r') as f:
        coeffs = []
        for idx,l in enumerate(f):
            if idx == 0:
                # The 0th line contains the WC names
                coeffs = l.split()
                continue
            else:
                vals = l.split()[1:]
            pt = {}
            for k,v in zip(coeffs,vals):
                pt[k] = float(v)
            pts.append(pt)
    return pts

# Calculates a random point between two specified values
def calculate_start_point(low,high,rfact=1.25):
    #NOTE1: rfact determines how close to 0 the randomly sample WC stregnth can be
    #NOTE2: rfact range can be [1,inf] and smaller numbers force the point to be further away from 0
    max_attempts = 999
    counter = 0
    #rand_factor = 1.25
    start_pt = round(random.uniform(low,high),6)
    while True:
        if counter > max_attempts:
            raise ValueError("Unable find valid starting point!")
        if start_pt < 0:
            if abs(start_pt)*rfact > abs(low):
                break
        else:
            if abs(start_pt)*rfact > abs(high):
                break
        start_pt = round(random.uniform(low,high),6)
        counter += 1
    return start_pt

# Saves the scan points to a text file formatted into a nice table
def save_scan_points(fpath,dofs,rwgt_pts):
    col_spacing = 15
    col_sep = " "
    with open(fpath,'w') as f:
        header = "".ljust(col_spacing)
        for k,dof in dofs.iteritems():
            header += dof.getName().ljust(col_spacing) + col_sep
        start_row = "\nMGStart".ljust(col_spacing) + col_sep
        for k,dof in dofs.iteritems():
            start_row += str(dof.getStart()).ljust(col_spacing) + col_sep
        f.write(header)
        f.write(start_row)
        for idx,pt in enumerate(rwgt_pts):
            row_name = "rwgt%d" % (idx)
            row = "\n" + row_name.ljust(col_spacing) + col_sep
            for k,dof in dofs.iteritems():
                if not pt.has_key(dof.getName()):
                    row += "0.0".ljust(col_spacing) + col_sep
                else:
                    row += str(pt[dof.getName()]).ljust(col_spacing) + col_sep
            f.write(row)

# Match strings using one or more regular expressions
def regex_match(lst,regex_lst):
    # NOTE: We don't escape any of the regex special characters!
    # TODO: Add whitelist/blacklist option switch
    matches = []
    if len(regex_lst) == 0:
        return lst[:]
    for s in lst:
        for pat in regex_lst:
            m = re.search(r"%s" % (pat),s)
            if m is not None:
                matches.append(s)
                break
    return matches

if __name__ == "__main__":
    pass