import random
import json

# wc_names_list is in the order for the scanpoints file
WC_NAMES_LST = ["ctp", "cpQM", "ctW", "ctZ", "ctG", "cbW", "cpQ3", "cptb", "cpt", "cQl3i", "cQlMi", "cQei", "ctli", "ctei", "ctlSi", "ctlTi", "cQq13", "cQq83", "cQq11", "ctq1", "cQq81", "ctq8", "ctt1", "cQQ1", "cQt1", "cQt8", "clq1", "cHbox", "ctu1", "ctb8", "clu", "cld", "cQb8", "ctd8", "cQd1", "cQd8", "ctd1", "cQu1", "cbB", "ctu8", "cQu8"] # Include 4hq needed for tttt
WC_NAMES_LST = ["ctp", "cpQM", "ctW", "ctZ", "ctG", "cbW", "cpQ3", "cptb", "cpt", "cQl3i", "cQlMi", "cQei", "ctli", "ctei", "ctlSi", "ctlTi", "cQq13", "cQq83", "cQq11", "ctq1", "cQq81", "ctq8", "clq1", "cHbox", "ctu1", "ctb8", "clu", "cld", "cQb8", "ctd8", "cQd1", "cQd8", "ctd1", "cQu1", "cbB", "ctu8", "cQu8"]
new_list = ["clq1", "cHbox", "ctu1", "ctb8", "clu", "cld", "cQb8", "ctd8", "cQd1", "cQd8", "ctd1", "cQu1", "cbB", "ctu8", "cQu8"]

TOP19001_LIMS = {
    "ctW"   : [-3.08, 2.87],
    "ctB"   : [-3.32, 3.15],
    "ctp"   : [-16.98, 44.26],
    "cpQM"  : [-7.59, 21.65],
    "ctG"   : [-1.38, 1.18],
    "cbW"   : [-4.95, 4.95],
    "cpQ3"  : [-7.37, 3.48],
    "cptb"  : [-12.72, 12.63],
    "cpt"   : [-18.62, 12.31],
    "cQl3" : [-9.67, 8.97],
    "cQl1" : [-4.02, 4.99],
    "cQe"  : [-4.38, 4.59],
    "ctl"  : [-4.29, 4.82],
    "cte"  : [-4.24, 4.86],
    "ctlSi" : [-6.52, 6.52],
    "ctlTi" : [-0.84, 0.84],
}

TOP19001_TTHJET_START = {
    "ctW"    :  -8.30,
    "ctp"    :  64.33,
    "cpQM"   :  45.88,
    "cte"   :  24.32,
    "ctl"   :  24.43,
    "cQe"   :  23.75,
    "ctB"    :  -6.09,
    "cQl1"  :  23.95,
    "cQl3"  :  21.54,
    "ctG"    :  -3.60,
    "ctlTi"  :  21.80,
    "cbW"    :  49.59,
    "cpQ3"   :  -51.1,
    "cptb"   :  136.1,
    "cpt"    :  -43.5,
    "ctlSi"  :  -20.0,
}

TOP19001_TTWJET_START = {
    "ctW"    : -3.82,
    "ctp"    : 51.50,
    "cpQM"   : 23.00,
    "cte"   : 8.938,
    "ctl"   : -7.00,
    "cQe"   : 8.968,
    "ctB"    : 5.727,
    "cQl1"  : 6.952,
    "cQl3"  : 9.243,
    "ctG"    : 2.430,
    "ctlTi"  : 2.116,
    "cbW"    : -7.37,
    "cpQ3"   : -14.4,
    "cptb"   : -21.8,
    "cpt"    : -20.3,
    "ctlSi"  : -9.99,
}

TOP19001_TTZJET_START = {
    "ctW"   : -5.02,  
    "ctp"   : 32.91,  
    "cpQM"  : -8.06,  
    "cte"  : 6.003,  
    "ctl"  : 10.16,  
    "cQe"  : 4.804,  
    "ctB"   : -3.86,  
    "cQl1" : -7.15,  
    "cQl3" : -8.33,  
    "ctG"   : 1.606,  
    "ctlTi" : 2.824,  
    "cbW"   : -3.82,  
    "cpQ3"  : -13.2,  
    "cptb"  : 14.49,  
    "cpt"   : -32.6,  
    "ctlSi" : -7.06,  
}

# I think from 1901 smefit paper
TEST1_2LEIGHT2HEAVY = {
    "cQq13" : 3.0,
    "cQq83" : -4.0,
    "cQq11" : 15.0,
    "ctq1"  : -12.0,
    "cQq81" : 15.0,
    "ctq8"  : -8.0,
}

# Just some numers
TEST2_2LEIGHT2HEAVY = {
    "cQq13" : 4.0,
    "cQq83" : 6.0,
    "cQq11" : 23.0,
    "ctq1"  : -19.0,
    "cQq81" : -13.0,
    "ctq8"  : 10.0,
}

# Just some numers
TEST3_2LEIGHT2HEAVY = {
    "cQq13" : -3.0,
    "cQq83" : 4.0,
    "cQq11" : -10.0,
    "ctq1"  : 10.0,
    "cQq81" : 17.0,
    "ctq8"  : -13.0,
}

OLD_AN_PT = {
    "ctW"   : -0.58,
    "ctB"   : -0.63,
    "ctp"   : 25.50,
    "cpQM"  : -1.07,
    "ctG"   : -0.85,
    "cbW"   : 3.17 ,
    "cpQ3"  : -1.81,
    "cptb"  : 0.13 ,
    "cpt"   : -3.25,
    "cQl3" : -4.20,
    "cQl1" : 0.74 ,
    "cQe"  : -0.27,
    "ctl"  : 0.33 ,
    "cte"  : 0.33 ,
    "ctlSi" : -0.07,
    "ctlTi" : -0.01
}

# Open a json file, assumes file is in same directory this file is being run from
def open_json(file_name):
    with open (file_name+".json","r") as f:
        d = json.load(f)
    return d

def find_rwgt_pt(wc_lims_dict,factor):
    rwgt_pt_dict = {}
    for wc_name, lims in wc_lims_dict.items():
        low = lims[0]*factor
        high = lims[1]*factor
        r_pt = random.uniform(low,high)
        rwgt_pt_dict[wc_name] = r_pt
    return rwgt_pt_dict;
        
def find_start_pt(wc_lims_dict,factor):
    start_pt_dict = {}
    max_tries = 100
    for wc_name, lims in wc_lims_dict.items():
        counter = 0
        low = lims[0]*factor
        high = lims[1]*factor
        while True:
            r_pt = random.uniform(low,high)
            if r_pt < 0:
                #print(low, r_pt)
                if abs(r_pt) > 0.5*abs(low):
                    #print("pt chosen:" , r_pt)
                    break
            else:
                #print(high, r_pt)
                if abs(r_pt) > 0.5*abs(high):
                    #print("pt chosen:" , r_pt)
                    break
            counter = counter +1
            if counter == max_tries:
                print("Could not find a valid start pt for",wc_name,"in",max_tries,"tries!")
                break
        start_pt_dict[wc_name] = r_pt
    return start_pt_dict


#def make_scanpts_file(start_pt_type, wc_names_list, wc_lims_dict, scanfile_name, start_pt_lst=None):
def make_scanpts_file(start_pt_type, wc_names_list, wc_lims_dict, scanfile_name, ref_pt_dict=None, new_list=None):

    buffer_window = 25
    sfile = open(scanfile_name,"w")

    # Find the start point dictionary
    if start_pt_type == "calculate":
        start_pt_dict = find_start_pt(wc_lims_dict,1.5) 
    elif start_pt_type == "ref":
        '''
        #ref_pt_vals = ["-8.303849","64.337172","45.883907","24.328689","24.43011","23.757944","-6.093077","23.951426","21.540499","-3.609446","21.809598","49.595354","-51.106621","136.133729","-43.552406","-20.005026"] #from ttll_16DOldLimitsAxisScan_run1_scanpoints.txt
        ref_pt_vals = start_pt_lst
        ref_pt_dict = {}
        for i,wc_name in enumerate(wc_names_list):
            ref_pt_dict[wc_name] = ref_pt_vals[i]
        '''
        start_pt_dict = ref_pt_dict

    # Write the WC names line
    sfile.write(" "*buffer_window)
    for wc_name in wc_names_list:
        sfile.write(wc_name + " "*(buffer_window-len(wc_name)))

    # Write the start point line
    sfile.write("\nMGStart" + " "*(buffer_window-len("MGStart")))
    if new_list is not None:
        for wc in new_list:
            start_pt_dict[wc] = 0
    for wc_name in wc_names_list: 
        #print(start_pt_dict[wc_name])
        buffer_str = " "*(buffer_window - len(str(start_pt_dict[wc_name])))
        sfile.write(str(start_pt_dict[wc_name])+buffer_str)

    # Write each rwgt pt line
    n_wc = len(wc_names_list)
    n_rwgt_pts = int(1.2*(1 + 2*n_wc + n_wc*(n_wc-1)/2))
    print(n_rwgt_pts)
    for i in range((n_rwgt_pts)+1):
        sfile.write("\nrwgt" + str(i) + " "*(buffer_window-len("rwgt"+str(i))))
        rwgt_pt_dict = find_rwgt_pt(wc_lims_dict,1.5)
        for wc_name in wc_names_list:
            if i == n_rwgt_pts:
                sfile.write(str("0.0") + " "*(buffer_window-len(str("0.0")))) 
            else:
                buffer_str = " "*(buffer_window - len(str(rwgt_pt_dict[wc_name])))
                sfile.write(str(rwgt_pt_dict[wc_name])+buffer_str)
            
    sfile.close()


def combine_dicts(d1,d2):
    ret_dict = {}
    for k in d1.keys():
        if k in d2:
            print("\nCannot combine these dictionaries, there is an overlap! Exiting...\n")
            raise Exception
    for k,v in d1.items():
        ret_dict[k] = v
    for k,v in d2.items():
        ret_dict[k] = v
    return ret_dict

def make_lims_dict(start_pt_dict):
    lims_dict = {}
    for wc,val in start_pt_dict.items():
        lims_dict[wc] = (-abs(1.2*val),abs(1.2*val))
    return lims_dict

def main():

    # Limits from AN (approx)
    wc_lims_dict = {
        "ctW"   : [-4,4], 
        "ctB"   : [-4,4],
        "ctp"   : [-11,41],
        "cpQM"  : [-8,28],
        "ctG"   : [-2,2],
        "cbW"   : [-5,5],
        "cpQ3"  : [-10,4],
        "cptb"  : [-18,18],
        "cpt"   : [-24,13],
        "cQl3" : [-8,7],
        "cQl1" : [-6,7],
        "cQe"  : [-6,6],
        "ctl"  : [-6,7],
        "cte"  : [-6,7],
        "ctlSi" : [-9,8],
        "ctlTi" : [-2,2],
    }

    # Some starting points
    ref_pt_vals = ["-8.303849","64.337172","45.883907","24.328689","24.43011","23.757944","-6.093077","23.951426","21.540499","-3.609446","21.809598","49.595354","-51.106621","136.133729","-43.552406","-20.005026"] #from ttll_16DOldLimitsAxisScan_run1_scanpoints.txt

    '''
    #top19001hi = []
    #oldANpt = []
    #for wc in WC_NAMES_LST:
    #    top19001hi.append(str(TOP19001_LIMS[wc][1]))
    #    oldANpt.append(str(OLD_AN_PT[wc]))
    #print(top19001hi)
    #print(oldANpt)

    #make_scanpts_file("ref",wc_names_list, wc_lims_dict, "plusJetCheck_refPt.txt")
    #make_scanpts_file("calculate",wc_names_list, wc_lims_dict, "plusJetCheck_startPt3.txt")

    # Tests
    #make_scanpts_file("calculate",WC_NAMES_LST, wc_lims_dict, "test.txt")
    #make_scanpts_file("ref",WC_NAMES_LST, wc_lims_dict, "test.txt",start_pt_lst=oldANpt)
    '''

    '''
    # Make ttHJet file
    ttHJet_start = combine_dicts(TOP19001_TTHJET_START,TEST1_2LEIGHT2HEAVY)
    ttHJet_lims = make_lims_dict(ttHJet_start)
    make_scanpts_file("ref",WC_NAMES_LST,ttHJet_lims,"ttHJet_22WCs_v0.txt",ref_pt_dict=ttHJet_start)

    # Make ttlnuJet file
    ttlnuJet_start = combine_dicts(TOP19001_TTWJET_START,TEST1_2LEIGHT2HEAVY)
    ttlnuJet_lims = make_lims_dict(ttlnuJet_start)
    make_scanpts_file("ref",WC_NAMES_LST,ttlnuJet_lims,"ttlnuJet_22WCs_v0.txt",ref_pt_dict=ttlnuJet_start)

    # Make ttllJet file
    ttllJet_start = combine_dicts(TOP19001_TTZJET_START,TEST1_2LEIGHT2HEAVY)
    ttllJet_lims = make_lims_dict(ttllJet_start)
    make_scanpts_file("ref",WC_NAMES_LST,ttllJet_lims,"ttllJet_22WCs_v0.txt",ref_pt_dict=ttllJet_start)
    '''

    '''
    # Make scanpoints file from TOP-19-001 lims
    top19001_lo_startpt = {}
    top19001_hi_startpt = {}
    for wc,lims in TOP19001_LIMS.items():
        top19001_lo_startpt[wc] = lims[0]
        top19001_hi_startpt[wc] = lims[1]
    top19001_lo_startpt_22d = combine_dicts(top19001_lo_startpt,TEST2_2LEIGHT2HEAVY)
    top19001_hi_startpt_22d = combine_dicts(top19001_hi_startpt,TEST3_2LEIGHT2HEAVY)
    make_scanpts_file("ref",WC_NAMES_LST,make_lims_dict(top19001_lo_startpt_22d),"top19001_lo_startpt_22d.txt",ref_pt_dict=top19001_lo_startpt_22d)
    make_scanpts_file("ref",WC_NAMES_LST,make_lims_dict(top19001_hi_startpt_22d),"top19001_hi_startpt_22d.txt",ref_pt_dict=top19001_hi_startpt_22d)
    '''


    #'''
    # Read start points from json files
    #file_name_lst = ["startpts_scale_by_1p1"]
    #file_name_lst = ["startpts_ctu"]
    file_name_lst = ["startpts_scale_by_5p0","startpts_scale_by_2p0","startpts_scale_by_1p5","startpts_scale_by_1p3","startpts_scale_by_1p1","startpts_ttgamma_SMEFTsim"]
    file_name_lst = ["startpts_scale_by_1p1"]
    file_name_lst = ["startpts_ttgamma_SMEFTsim"]
    file_name_lst = ["startpts_scale_by_1p1_Run3_dim6top"]
    for f_name in file_name_lst:
        d = open_json(f_name)
        for process_name,process_startpt in d.items():
            for wc_name in WC_NAMES_LST:
                if wc_name not in process_startpt:
                    process_startpt[wc_name] = 100.
            save_name = f_name+"_"+process_name+".txt"
            print(save_name)
            make_scanpts_file("ref",WC_NAMES_LST,make_lims_dict(process_startpt),save_name,ref_pt_dict=process_startpt,new_list=new_list)
    #'''


main()






