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

# Create the MadGraph restrict card with scans over the specified W.C. phase space points
def make_restrict_card(file_name,dofs):
    wc_dict = OrderedDict()
    wc_dict["cG"] = ("  1", "0.200000e+00" )
    wc_dict["cW"] =  ("  2", "0.300000e+00" )
    wc_dict["cH"] =  ("  3", "0.400000e+00" )
    wc_dict["cHbox"] =  ("  4", "0.500000e+00" )
    wc_dict["cHDD"] =  ("  5", "0.600000e+00" )
    wc_dict["cHG"] =  ("  6", "0.700000e+00" )
    wc_dict["cHW"] =  ("  7", "0.800000e+00" )
    wc_dict["cHB"] =  ("  8", "0.900000e+00" )
    wc_dict["cHWB"] =  ("  9", "0.020000e+00" )
    wc_dict["cuHRe"] =  (" 10", "0.030000e+00" )
    wc_dict["ctHRe"] =  (" 11", "0.040000e+00" )
    wc_dict["cdHRe"] =  (" 12", "0.050000e+00" )
    wc_dict["cbHRe"] =  (" 13", "0.060000e+00" )
    wc_dict["cuGRe"] =  (" 14", "0.070000e+00" )
    wc_dict["ctGRe"] =  (" 15", "0.080000e+00" )
    wc_dict["cuWRe"] =  (" 16", "0.090000e+00" )
    wc_dict["ctWRe"] =  (" 17", "0.002000e+00" )
    wc_dict["cuBRe"] =  (" 18", "0.003000e+00" )
    wc_dict["ctBRe"] =  (" 19", "0.004000e+00" )
    wc_dict["cdGRe"] =  (" 20", "0.005000e+00" )
    wc_dict["cbGRe"] =  (" 21", "0.006000e+00" )
    wc_dict["cdWRe"] =  (" 22", "0.007000e+00" )
    wc_dict["cbWRe"] =  (" 23", "0.008000e+00" )
    wc_dict["cdBRe"] =  (" 24", "0.009000e+00" )
    wc_dict["cbBRe"] =  (" 25", "0.000200e+00" )
    wc_dict["cHj1"] =  (" 26", "0.000300e+00" )
    wc_dict["cHQ1"] =  (" 27", "0.000400e+00" )
    wc_dict["cHj3"] =  (" 28", "0.000500e+00" )
    wc_dict["cHQ3"] =  (" 29", "0.000600e+00" )
    wc_dict["cHu"] =  (" 30", "0.000700e+00" )
    wc_dict["cHt"] =  (" 31", "0.000800e+00" )
    wc_dict["cHd"] =  (" 32", "0.000900e+00" )
    wc_dict["cHbq"] =  (" 33", "0.000020e+00" )
    wc_dict["cHudRe"] =  (" 34", "0.000030e+00" )
    wc_dict["cHtbRe"] =  (" 35", "0.000040e+00" )
    wc_dict["cjj11"] =  (" 36", "0.000050e+00" )
    wc_dict["cjj18"] =  (" 37", "0.000060e+00" )
    wc_dict["cjj31"] =  (" 38", "0.000070e+00" )
    wc_dict["cjj38"] =  (" 39", "0.000080e+00" )
    wc_dict["cQj11"] =  (" 40", "0.000090e+00" )
    wc_dict["cQj18"] =  (" 41", "0.000002e+00" )
    wc_dict["cQj31"] =  (" 42", "0.000003e+00" )
    wc_dict["cQj38"] =  (" 43", "0.000004e+00" )
    wc_dict["cQQ1"] =  (" 44", "0.000005e+00" )
    wc_dict["cQQ8"] =  (" 45", "0.000006e+00" )
    wc_dict["cuu1"] =  (" 46", "0.000007e+00" )
    wc_dict["cuu8"] =  (" 47", "0.000008e+00" )
    wc_dict["ctt"] =  (" 48", "0.000009e+00" )
    wc_dict["ctu1"] =  (" 49", "0.1100000e+00")
    wc_dict["ctu8"] =  (" 50", "0.1200000e+00")
    wc_dict["cdd1"] =  (" 51", "0.1300000e+00")
    wc_dict["cdd8"] =  (" 52", "0.1400000e+00")
    wc_dict["cbb"] =  (" 53", "0.1500000e+00")
    wc_dict["cbd1"] =  (" 54", "0.1600000e+00")
    wc_dict["cbd8"] =  (" 55", "0.1700000e+00")
    wc_dict["cud1"] =  (" 56", "0.1800000e+00")
    wc_dict["ctb1"] =  (" 57", "0.1900000e+00")
    wc_dict["ctd1"] =  (" 58", "0.2100000e+00")
    wc_dict["cbu1"] =  (" 59", "0.2200000e+00")
    wc_dict["cud8"] =  (" 60", "0.2300000e+00")
    wc_dict["ctb8"] =  (" 61", "0.2400000e+00")
    wc_dict["ctd8"] =  (" 62", "0.2500000e+00")
    wc_dict["cbu8"] =  (" 63", "0.2600000e+00")
    wc_dict["cutbd1Re"] =  (" 64", "0.2700000e+00")
    wc_dict["cutbd8Re"] =  (" 65", "0.2800000e+00")
    wc_dict["cju1"] =  (" 66", "0.2900000e+00")
    wc_dict["cQu1"] =  (" 67", "0.3100000e+00")
    wc_dict["cju8"] =  (" 68", "0.3200000e+00")
    wc_dict["cQu8"] =  (" 69", "0.3300000e+00")
    wc_dict["ctj1"] =  (" 70", "0.3400000e+00")
    wc_dict["ctj8"] =  (" 71", "0.3500000e+00")
    wc_dict["cQt1"] =  (" 72", "0.3600000e+00")
    wc_dict["cQt8"] =  (" 73", "0.3700000e+00")
    wc_dict["cjd1"] =  (" 74", "0.3800000e+00")
    wc_dict["cjd8"] =  (" 75", "0.3900000e+00")
    wc_dict["cQd1"] =  (" 76", "0.4100000e+00")
    wc_dict["cQd8"] =  (" 77", "0.4200000e+00")
    wc_dict["cbj1"] =  (" 78", "0.4300000e+00")
    wc_dict["cbj8"] =  (" 79", "0.4400000e+00")
    wc_dict["cQb1"] =  (" 80", "0.4500000e+00")
    wc_dict["cQb8"] =  (" 81", "0.4600000e+00")
    wc_dict["cjQtu1Re"] =  (" 82", "0.4700000e+00")
    wc_dict["cjQtu8Re"] =  (" 83", "0.4800000e+00")
    wc_dict["cjQbd1Re"] =  (" 84", "0.4900000e+00")
    wc_dict["cjQbd8Re"] =  (" 85", "0.5100000e+00")
    wc_dict["cjujd1Re"] =  (" 86", "0.5200000e+00")
    wc_dict["cjujd8Re"] =  (" 87", "0.5300000e+00")
    wc_dict["cjujd11Re"] =  (" 88", "0.5400000e+00")
    wc_dict["cjujd81Re"] =  (" 89", "0.5500000e+00")
    wc_dict["cQtjd1Re"] =  (" 90", "0.5600000e+00")
    wc_dict["cQtjd8Re"] =  (" 91", "0.5700000e+00")
    wc_dict["cjuQb1Re"] =  (" 92", "0.5800000e+00")
    wc_dict["cjuQb8Re"] =  (" 93", "0.5900000e+00")
    wc_dict["cQujb1Re"] =  (" 94", "0.6100000e+00")
    wc_dict["cQujb8Re"] =  (" 95", "0.6200000e+00")
    wc_dict["cjtQd1Re"] =  (" 96", "0.6300000e+00")
    wc_dict["cjtQd8Re"] =  (" 97", "0.6400000e+00")
    wc_dict["cQtQb1Re"] =  (" 98", "0.6500000e+00")
    wc_dict["cQtQb8Re"] =  (" 99", "0.6600000e+00")
    wc_dict["ceHRe"] =  (100, "0.6700000e+00")
    wc_dict["ceWRe"] =  (101, "0.6800000e+00")
    wc_dict["ceBRe"] =  (102, "0.6900000e+00")
    wc_dict["cHl1"] =  (103, "0.7100000e+00")
    wc_dict["cHl3"] =  (104, "0.7200000e+00")
    wc_dict["cHe"] =  (105, "0.7300000e+00")
    wc_dict["cll"] =  (106, "0.7400000e+00")
    wc_dict["cll1"] =  (107, "0.7500000e+00")
    wc_dict["clj1"] =  (108, "0.7600000e+00")
    wc_dict["clj3"] =  (109, "0.7700000e+00")
    wc_dict["cQl1"] =  (110, "0.7800000e+00")
    wc_dict["cQl3"] =  (111, "0.7900000e+00")
    wc_dict["cee"] =  (112, "0.8100000e+00")
    wc_dict["ceu"] =  (113, "0.8200000e+00")
    wc_dict["cte"] =  (114, "0.8300000e+00")
    wc_dict["ced"] =  (115, "0.8400000e+00")
    wc_dict["cbe"] =  (116, "0.8500000e+00")
    wc_dict["cje"] =  (117, "0.8600000e+00")
    wc_dict["cQe"] =  (118, "0.8700000e+00")
    wc_dict["clu"] =  (119, "0.8800000e+00")
    wc_dict["ctl"] =  (120, "0.8900000e+00")
    wc_dict["cld"] =  (121, "0.9100000e+00")
    wc_dict["cbl"] =  (122, "0.9200000e+00")
    wc_dict["cle"] =  (123, "0.9300000e+00")
    wc_dict["cledjRe"] =  (124, "0.9400000e+00")
    wc_dict["clebQRe"] =  (125, "0.9500000e+00")
    wc_dict["cleju1Re"] =  (126, "0.9600000e+00")
    wc_dict["cleQt1Re"] =  (127, "0.9700000e+00")
    wc_dict["cleju3Re"] =  (128, "0.9800000e+00")
    wc_dict["cleQt3Re"] =  (129, "0.9900000e+00")

    header  = ""
    header += "######################################################################\n"
    header += "## PARAM_CARD AUTOMATICALY GENERATED BY THE UFO  #####################\n"
    header += "######################################################################\n"
    header += "\n"
    header += "###################################\n"
    header += "## INFORMATION FOR SMINPUTS\n"
    header += "###################################\n"
    header += "Block SMINPUTS \n"
    header += "    1 8.038700e+01 # MW \n"
    header += "    2 1.166379e-05 # Gf \n"
    header += "    3 1.179000e-01 # aS \n"
    header += "\n"
    header += "###################################\n"
    header += "## INFORMATION FOR MASS\n"
    header += "###################################\n"
    header += "Block MASS \n"
    header += "    1 0.000000e+00 # MD \n"
    header += "    2 0.000000e+00 # MU \n"
    header += "    3 0.000000e+00 # MS \n"
    header += "    4 0.000000e+00 # MC \n"
    header += "    5 0.000000e+00 # MB \n"
    header += "    6 1.727600e+02 # MT \n"
    header += "    11 1.727600e+02 # Me\n"
    header += "    13 1.740691e+02 # MMU\n"
    header += "    15 1.742157e+02 # MTA\n"
    #header += "   11 0.000000e+00 # Me \n"
    #header += "   13 0.000000e+00 # MMU \n"
    #header += "   15 0.000000e+00 # MTA \n"
    header += "   23 9.118760e+01 # MZ \n"
    header += "   25 1.250900e+02 # MH \n"
    header += "##  Not dependent paramater.\n"
    header += "## Those values should be edited following analytical the \n"
    header += "## analytical expression. Some generator could simply ignore \n"
    header += "## those values and use the analytical expression\n"
    header += "  22 0.000000 # a : 0.0 \n"
    header += "  21 0.000000 # g : 0.0 \n"
    header += "  9000005 91.187600 # Z1 : MZ \n"
    header += "  9000006 80.387000 # W1+ : MWsm \n"
    header += "  12 0.000000 # ve : 0.0 \n"
    header += "  14 0.000000 # vm : 0.0 \n"
    header += "  16 0.000000 # vt : 0.0 \n"
    header += "  9000007 172.760000 # t1 : MT \n"
    header += "  9000008 125.090000 # H1 : MH \n"
    header += "  24 80.387000 # W+ : MW \n"
    header += "\n"
    header += "###################################\n"
    header += "## INFORMATION FOR DECAY\n"
    header += "###################################\n"
    header += "DECAY   6 1.330000e+00 \n"
    header += "DECAY  23 2.495200e+00 \n"
    header += "DECAY  24 2.085000e+00 \n"
    header += "DECAY  25 4.070000e-03 \n"
    header += "##  Not dependent paramater.\n"
    header += "## Those values should be edited following analytical the \n"
    header += "## analytical expression. Some generator could simply ignore \n"
    header += "## those values and use the analytical expression\n"
    header += "DECAY  22 0.000000 # a : 0.0 \n"
    header += "DECAY  21 0.000000 # g : 0.0 \n"
    header += "DECAY  9000005 2.495200 # Z1 : WZ \n"
    header += "DECAY  9000006 2.085000 # W1+ : WW \n"
    header += "DECAY  12 0.000000 # ve : 0.0 \n"
    header += "DECAY  14 0.000000 # vm : 0.0 \n"
    header += "DECAY  16 0.000000 # vt : 0.0 \n"
    header += "DECAY  11 0.000000 # e- : 0.0 \n"
    header += "DECAY  13 0.000000 # mu- : 0.0 \n"
    header += "DECAY  15 0.000000 # ta- : 0.0 \n"
    header += "DECAY  2 0.000000 # u : 0.0 \n"
    header += "DECAY  4 0.000000 # c : 0.0 \n"
    header += "DECAY  1 0.000000 # d : 0.0 \n"
    header += "DECAY  3 0.000000 # s : 0.0 \n"
    header += "DECAY  5 0.000000 # b : 0.0 \n"
    header += "DECAY  9000007 1.330000 # t1 : WT \n"
    header += "DECAY  9000008 0.004070 # H1 : WH \n"
    header += "\n"
    header += "###################################\n"
    header += "## INFORMATION FOR SWITCHES\n"
    header += "###################################\n"
    header += "Block SWITCHES \n"
    header += "    1 0.000000e+00 # linearPropCorrections \n"
    header += "\n"
    header += "###################################\n"
    header += "## INFORMATION FOR SMEFTCUTOFF\n"
    header += "###################################\n"
    header += "Block SMEFTcutoff \n"
    header += "    1 1.000000e+03 # LambdaSMEFT \n"
    header += "\n"
    header += "###################################\n"
    header += "## INFORMATION FOR SMEFT\n"
    header += "###################################\n"
    header += "Block SMEFT \n"

    footer = ""
    footer += "\n"
    footer += "###################################\n"
    footer += "## INFORMATION FOR SMEFTCPV\n"
    footer += "###################################\n"
    footer += "Block SMEFTcpv \n"
    footer += "    1 0.000000e+00 # cGtil \n"
    footer += "    2 0.000000e+00 # cWtil \n"
    footer += "    3 0.000000e+00 # cHGtil \n"
    footer += "    4 0.000000e+00 # cHWtil \n"
    footer += "    5 0.000000e+00 # cHBtil \n"
    footer += "    6 0.000000e+00 # cHWBtil \n"
    footer += "    7 0.000000e+00 # cuGIm \n"
    footer += "    8 0.000000e+00 # ctGIm \n"
    footer += "    9 0.000000e+00 # cuWIm \n"
    footer += "   10 0.000000e+00 # ctWIm \n"
    footer += "   11 0.000000e+00 # cuBIm \n"
    footer += "   12 0.000000e+00 # ctBIm \n"
    footer += "   13 0.000000e+00 # cdGIm \n"
    footer += "   14 0.000000e+00 # cbGIm \n"
    footer += "   15 0.000000e+00 # cdWIm \n"
    footer += "   16 0.000000e+00 # cbWIm \n"
    footer += "   17 0.000000e+00 # cdBIm \n"
    footer += "   18 0.000000e+00 # cbBIm \n"
    footer += "   19 0.000000e+00 # cuHIm \n"
    footer += "   20 0.000000e+00 # ctHIm \n"
    footer += "   21 0.000000e+00 # cdHIm \n"
    footer += "   22 0.000000e+00 # cbHIm \n"
    footer += "   23 0.000000e+00 # cHudIm \n"
    footer += "   24 0.000000e+00 # cHtbIm \n"
    footer += "   25 0.000000e+00 # cutbd1Im \n"
    footer += "   26 0.000000e+00 # cutbd8Im \n"
    footer += "   27 0.000000e+00 # cjQtu1Im \n"
    footer += "   28 0.000000e+00 # cjQtu8Im \n"
    footer += "   29 0.000000e+00 # cjQbd1Im \n"
    footer += "   30 0.000000e+00 # cjQbd8Im \n"
    footer += "   31 0.000000e+00 # cjujd1Im \n"
    footer += "   32 0.000000e+00 # cjujd8Im \n"
    footer += "   33 0.000000e+00 # cjujd11Im \n"
    footer += "   34 0.000000e+00 # cjujd81Im \n"
    footer += "   35 0.000000e+00 # cQtjd1Im \n"
    footer += "   36 0.000000e+00 # cQtjd8Im \n"
    footer += "   37 0.000000e+00 # cjuQb1Im \n"
    footer += "   38 0.000000e+00 # cjuQb8Im \n"
    footer += "   39 0.000000e+00 # cQujb1Im \n"
    footer += "   40 0.000000e+00 # cQujb8Im \n"
    footer += "   41 0.000000e+00 # cjtQd1Im \n"
    footer += "   42 0.000000e+00 # cjtQd8Im \n"
    footer += "   43 0.000000e+00 # cQtQb1Im \n"
    footer += "   44 0.000000e+00 # cQtQb8Im \n"
    footer += "   45 0.000000e+00 # ceHIm \n"
    footer += "   46 0.000000e+00 # ceWIm \n"
    footer += "   47 0.000000e+00 # ceBIm \n"
    footer += "   48 0.000000e+00 # cledjIm \n"
    footer += "   49 0.000000e+00 # clebQIm \n"
    footer += "   50 0.000000e+00 # cleju1Im \n"
    footer += "   51 0.000000e+00 # cleju3Im \n"
    footer += "   52 0.000000e+00 # cleQt1Im \n"
    footer += "   53 0.000000e+00 # cleQt3Im \n"
    footer += "\n"
    footer += "###################################\n"
    footer += "## INFORMATION FOR YUKAWA\n"
    footer += "###################################\n"
    footer += "Block YUKAWA \n"
    footer += "    1 0.000000e+00 # ymdo \n"
    footer += "    2 0.000000e+00 # ymup \n"
    footer += "    3 0.000000e+00 # yms \n"
    footer += "    4 0.000000e+00 # ymc \n"
    footer += "    5 0.000000e+00 # ymb \n"
    footer += "    6 1.727600e+02 # ymt \n"
    # massless
    #footer += "   11 0.000000e+00 # yme \n"
    #footer += "   13 0.000000e+00 # ymm \n"
    #footer += "   15 0.000000e+00 # ymtau \n"
    # massless_q
    footer += "    11 1.727600e+02 # yme \n"
    footer += "    13 1.740691e+02 # ymm \n"
    footer += "    15 1.742157e+02 # ymtau \n"
    #footer += "   11 5.110000e-04 # yme  \n"
    #footer += "   13 1.056600e-01 # ymm  \n"
    #footer += "   15 1.777000e+00 # ymtau  \n"
    footer += "#===========================================================\n"
    footer += "# QUANTUM NUMBERS OF NEW STATE(S) (NON SM PDG CODE)\n"
    footer += "#===========================================================\n"
    footer += "\n"
    footer += "Block QNUMBERS 9000005  # Z1 \n"
    footer += "        1 0  # 3 times electric charge\n"
    footer += "        2 3  # number of spin states (2S+1)\n"
    footer += "        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)\n"
    footer += "        4 0  # Particle/Antiparticle distinction (0=own anti)\n"
    footer += "Block QNUMBERS 9000006  # W1+ \n"
    footer += "        1 3  # 3 times electric charge\n"
    footer += "        2 3  # number of spin states (2S+1)\n"
    footer += "        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)\n"
    footer += "        4 1  # Particle/Antiparticle distinction (0=own anti)\n"
    footer += "Block QNUMBERS 9000007  # t1 \n"
    footer += "        1 2  # 3 times electric charge\n"
    footer += "        2 2  # number of spin states (2S+1)\n"
    footer += "        3 3  # colour rep (1: singlet, 3: triplet, 8: octet)\n"
    footer += "        4 1  # Particle/Antiparticle distinction (0=own anti)\n"
    footer += "Block QNUMBERS 9000008  # H1 \n"
    footer += "        1 0  # 3 times electric charge\n"
    footer += "        2 1  # number of spin states (2S+1)\n"
    footer += "        3 1  # colour rep (1: singlet, 3: triplet, 8: octet)\n"
    footer += "        4 0  # Particle/Antiparticle distinction (0=own anti)\n"

    with open(file_name,'w') as f:
        f.write(header)
        for wc,(num,val) in wc_dict.items():
            if wc in dofs:
                f.write("    {num} {val}  # {wc}\n".format(num=num, val=val, wc=wc))
            else:
                f.write("    {num} 0.0000000e+00  # {wc}\n".format(num=num, wc=wc))
        f.write(footer)

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
