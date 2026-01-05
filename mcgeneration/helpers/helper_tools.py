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
        if l == b'' and p.poll() is not None:
            break
        if l:
            stdout.append(l.strip())
            if verbose: print(indent_str+l.strip())
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
    for k,v in pt1.items():
        if k not in pt2:
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
        for c,dof in dofs.items():
            for k,v in dof.eval(dof.getStart()).items():
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
        c = list(dofs.keys())[0]
        for k,v in dofs[c].eval(0.0123).items():
            f.write("\nset %s %.6f" % (k,v))
        f.write("\n")

        for idx,pt in enumerate(pts):
            rwgt_str = "EFTrwgt%d" % (idx)
            for k,v in pt.items():
                rwgt_str += '_' + k + '_' + str(round(v,6))
            f.write("\nlaunch --rwgt_name=%s" % (rwgt_str))
            for k1,v1 in pt.items():
                for k2,v2 in dofs[k1].eval(v1).items():
                    f.write("\nset %s %.6f" % (k2,v2))
            f.write("\n")

def make_restrict_card(ref_fpath,out_fpath,keep=True,**blocks):
    '''
        ref_fpath: Full path to the reference restrict card to read, which will serve as the basis
                   for the new restrict card
        out_fpath: Full path to write the modified restrict card to.
        keep: If true, then for a given block, the listed parameters will be NOT zero'd out.
              If false, then for a given block, the listed parameters will be zero'd out.
        blocks: {
            "block_A" : ["param1", "param2", ...],
            "block_B" : [ ... ],
        }

        NOTE: If a lhablock is not included as part of the 'blocks' dictionary, then all parameters
              in that block will be untouched. If you want to zero out all parameters for a particular
              block, then simply include that block and give it an empty list (with keep=True).

        NOTE: The keys of the 'blocks' dictionary are case sensitive and need to match exactly with
              how they are spelled in the reference restrict card. The same goes for the parameter
              names.

        NOTE: The newly made restrict card needs to be placed in the directory of the model that the
              process card intends to use, e.g. "addons/models/NAME_OF_MODEL". The gridpack_generation.sh
              script has a line that will copy everything under "addons/models" into the MG base
              directory that gets created on the fly in gridpack_generation.sh. This is how MG is able
              to find custom models that aren't default included in MG.

        NOTE: The 'for' loop explicitly avoids using any 'continue' statements, since we want the
              new restrict card to be a 1-to-1 match of the original, with the only changes being
              the values of specific parameters in certain lhablocks.
    '''
    counter = 1
    indent = " "*2
    lines = []
    block = None
    with open(ref_fpath,'r') as f:
        for line_no,l in enumerate(f.readlines()):
            # Check if this ENTIRE line is a comment
            is_comment = l.startswith("#")
            # Check if this line specifies the start of a new LHA block section
            is_block_header = l.lower().startswith("block")
            # Check if this line is an empty line
            is_empty_line = len(l.strip()) == 0
            # Skip lines we know we won't need to edit
            skip = is_comment or is_block_header or is_empty_line
            if is_block_header:
                # Store the name of the current block
                block = l.split()[1]
            if l.lower().startswith("decay"):
                # Decay lines are their own thing separate from LHA block stuff, so don't mess with them
                skip = True
            elif block == "QNUMBERS":
                # QNUMBERS blocks have a bit different syntax then other blocks, so avoid them as well
                skip = True
            # Avoid dealing with lines that should never need to be edited
            if not skip:
                data, param_name = [x.strip() for x in l.split(" # ")]
                # data should always be 2 numbers separated by a single space
                idx, value = data.split()
                if block in blocks:
                    params = blocks[block]
                    if keep:
                        # Zero out any params that aren't specified
                        if param_name in params:
                            l = f"{indent}{idx:>3} 0.{counter:0<7}e+00 # {param_name} "
                            counter += 1
                        else:
                            l = f"{indent}{idx:>3} 0.0000000e+00 # {param_name} "
                    else:
                        # Zero out any params that are specified
                        if param_name in params:
                            l = f"{indent}{idx:>3} 0.0000000e+00 # {param_name} "
                        else:
                            l = f"{indent}{idx:>3} 0.{counter:0<7}e+00 # {param_name} "
                            counter += 1
            # The new restrict card should be (as far as lines go) a 1-to-1 mirror of the base card
            lines.append(l.rstrip("\n"))

    with open(out_fpath,'w') as f:
        f.write("\n".join(lines))
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
        for k,dof in dofs.items():
            header += dof.getName().ljust(col_spacing) + col_sep
        start_row = "\nMGStart".ljust(col_spacing) + col_sep
        for k,dof in dofs.items():
            start_row += str(dof.getStart()).ljust(col_spacing) + col_sep
        f.write(header)
        f.write(start_row)
        for idx,pt in enumerate(rwgt_pts):
            row_name = "rwgt%d" % (idx)
            row = "\n" + row_name.ljust(col_spacing) + col_sep
            for k,dof in dofs.items():
                if dof.getName() not in pt:
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
