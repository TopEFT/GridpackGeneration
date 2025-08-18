import random
import json

# wc_names_list is in the order for the scanpoints file
WC_NAMES_LST = ["ctWRe" , "ctHRe" , "cHQ1" , "cte" , "ctl" , "cQe" , "ctBRe" , "cQl1" , "cQl3" , "ctGRe" , "cleQt3Re" , "cbWRe" , "cHQ3" , "cHtbRe" , "cHt" , "cleQt1Re" , "cQj31" , "cQj38" , "cQj11" , "ctj1" , "cQj18" , "ctj8"]
WC_NAMES_LST = ["ctHRe", "cHQ1", "ctWRe", "ctBRe", "ctGRe", "cbWRe", "cHQ3", "cHtbRe", "cHt", "cQl3", "cQl1", "cQe", "ctl", "cte", "cleQt1Re", "cleQt3Re", "cQj31", "cQj38", "cQj11", "ctj1", "cQj18", "ctj8", "ctt", "cQQ1", "cQt1", "cQt8", "cbGRe", "clj1", "cHbox", "ctu1", "ctb8", "clu", "cld", "cQb8", "ctd8", "cQd1", "cQd8", "ctd1", "cQu1", "cbBRe", "ctu8", "cQu8"]
WC_NAMES_LST = ["ctHRe", "cHQ1", "ctWRe", "ctBRe", "ctGRe", "cbWRe", "cHQ3", "cHtbRe", "cHt", "cQl3", "cQl1", "cQe", "ctl", "cte", "cleQt1Re11", "cleQt1Re22", "cleQt1Re33", "cleQt3Re11", "cleQt3Re22", "cleQt3Re33", "cQj31", "cQj38", "cQj11", "ctj1", "cQj18", "ctj8", "ctt", "cQQ1", "cQt1", "cQt8", "cbGRe", "clj1", "cHbox", "ctu1", "ctb8", "clu", "cld", "cQb8", "ctd8", "cQd1", "cQd8", "ctd1", "cQu1", "cbBRe", "ctu8", "cQu8"] # 46 WCs including 4-heavy (needed for tttt)
WC_NAMES_LST = ["ctHRe", "cHQ1", "ctWRe", "ctBRe", "ctGRe", "cbWRe", "cHQ3", "cHtbRe", "cHt", "cQl3", "cQl1", "cQe", "ctl", "cte", "cleQt1Re11", "cleQt1Re22", "cleQt1Re33", "cleQt3Re11", "cleQt3Re22", "cleQt3Re33", "cQj31", "cQj38", "cQj11", "ctj1", "cQj18", "ctj8", "cbGRe", "clj1", "cHbox", "ctu1", "ctb8", "clu", "cld", "cQb8", "ctd8", "cQd1", "cQd8", "ctd1", "cQu1", "cbBRe", "ctu8", "cQu8"] # 42 WCs excluding 4-heavy
WC_NAMES_LST = ["ctHRe", "cHQ1", "ctWRe", "ctBRe", "ctGRe", "cbWRe", "cHQ3", "cHtbRe", "cHt", "cQl31", "cQl32", "cQl33", "cQl11", "cQl12", "cQl12", "cQe1", "cQe2", "cQe3", "ctl1", "ctl2", "ctl2", "cte1", "cte2", "cte3", "cleQt3Re11", "cleQt3Re22", "cleQt3Re33", "cleQt1Re11", "cleQt1Re22", "cleQt1Re33", "cQj31", "cQj38", "cQj11", "ctj1", "cQj18", "ctj8", "clj1", "cHbox", "ctu1", "ctb8", "clu", "cld", "cQb8", "ctd8", "cQd1", "cQd8", "ctd1", "cQu1", "cbBRe", "ctu8", "cQu8"] # Full set with all lepton flavors expanded
WC_NAMES_LST = ["ctHRe", "cHQ1", "ctWRe", "ctBRe", "ctGRe", "cbWRe", "cHQ3", "cHtbRe", "cHt", "cQl31", "cQl32", "cQl33", "cQl11", "cQl12", "cQl12", "cQe1", "cQe2", "cQe3", "ctl1", "ctl2", "ctl2", "cte1", "cte2", "cte3", "cleQt3Re11", "cleQt3Re22", "cleQt3Re33", "cleQt1Re11", "cleQt1Re22", "cleQt1Re33", "cQj31", "cQj38", "cQj11", "ctj1", "cQj18", "ctj8", "clj1", "cHbox", "ctu1", "ctb8", "clu", "cld", "cQb8", "ctd8", "cQd1", "cQd8", "ctd1", "cQu1", "cbBRe", "ctu8", "cQu8"] # Full set with all lepton flavors expanded

TOP19001_LIMS = {
    "ctWRe"   : [-3.08, 2.87],
    "ctBRe"   : [-3.32, 3.15],
    "ctHRe"   : [-16.98, 44.26],
    "cHQ1"  : [-7.59, 21.65],
    "ctGRe"   : [-1.38, 1.18],
    "cbWRe"   : [-4.95, 4.95],
    "cHQ3"  : [-7.37, 3.48],
    "cHtbRe"  : [-12.72, 12.63],
    "cHt"   : [-18.62, 12.31],
    "cQl3" : [-9.67, 8.97],
    "cQl1" : [-4.02, 4.99],
    "cQe"  : [-4.38, 4.59],
    "ctl"  : [-4.29, 4.82],
    "cte"  : [-4.24, 4.86],
    "cleQt1Re" : [-6.52, 6.52],
    "cleQt3Re" : [-0.84, 0.84],
}

TOP19001_TTHJET_START = {
    "ctWRe"    :  -8.30,
    "ctHRe"    :  64.33,
    "cHQ1"   :  45.88,
    "cte"   :  24.32,
    "ctl"   :  24.43,
    "cQe"   :  23.75,
    "ctBRe"    :  -6.09,
    "cQl1"  :  23.95,
    "cQl3"  :  21.54,
    "ctGRe"    :  -3.60,
    "cleQt3Re"  :  21.80,
    "cbWRe"    :  49.59,
    "cHQ3"   :  -51.1,
    "cHtbRe"   :  136.1,
    "cHt"    :  -43.5,
    "cleQt1Re"  :  -20.0,
}

TOP19001_TTWJET_START = {
    "ctWRe"    : -3.82,
    "ctHRe"    : 51.50,
    "cHQ1"   : 23.00,
    "cte"   : 8.938,
    "ctl"   : -7.00,
    "cQe"   : 8.968,
    "ctBRe"    : 5.727,
    "cQl1"  : 6.952,
    "cQl3"  : 9.243,
    "ctGRe"    : 2.430,
    "cleQt3Re"  : 2.116,
    "cbWRe"    : -7.37,
    "cHQ3"   : -14.4,
    "cHtbRe"   : -21.8,
    "cHt"    : -20.3,
    "cleQt1Re"  : -9.99,
}

TOP19001_TTZJET_START = {
    "ctWRe"   : -5.02,  
    "ctHRe"   : 32.91,  
    "cHQ1"  : -8.06,  
    "cte"  : 6.003,  
    "ctl"  : 10.16,  
    "cQe"  : 4.804,  
    "ctBRe"   : -3.86,  
    "cQl1" : -7.15,  
    "cQl3" : -8.33,  
    "ctGRe"   : 1.606,  
    "cleQt3Re" : 2.824,  
    "cbWRe"   : -3.82,  
    "cHQ3"  : -13.2,  
    "cHtbRe"  : 14.49,  
    "cHt"   : -32.6,  
    "cleQt1Re" : -7.06,  
}

# I think from 1901 smefit paper
TEST1_2LEIGHT2HEAVY = {
    "cQj31" : 3.0,
    "cQj38" : -4.0,
    "cQj11" : 15.0,
    "ctj1"  : -12.0,
    "cQj18" : 15.0,
    "ctj8"  : -8.0,
}

# Just some numers
TEST2_2LEIGHT2HEAVY = {
    "cQj31" : 4.0,
    "cQj38" : 6.0,
    "cQj11" : 23.0,
    "ctj1"  : -19.0,
    "cQj18" : -13.0,
    "ctj8"  : 10.0,
}

# Just some numers
TEST3_2LEIGHT2HEAVY = {
    "cQj31" : -3.0,
    "cQj38" : 4.0,
    "cQj11" : -10.0,
    "ctj1"  : 10.0,
    "cQj18" : 17.0,
    "ctj8"  : -13.0,
}

OLD_AN_PT = {
    "ctWRe"   : -0.58,
    "ctBRe"   : -0.63,
    "ctHRe"   : 25.50,
    "cHQ1"  : -1.07,
    "ctGRe"   : -0.85,
    "cbWRe"   : 3.17 ,
    "cHQ3"  : -1.81,
    "cHtbRe"  : 0.13 ,
    "cHt"   : -3.25,
    "cQl3" : -4.20,
    "cQl1" : 0.74 ,
    "cQe"  : -0.27,
    "ctl"  : 0.33 ,
    "cte"  : 0.33 ,
    "cleQt1Re" : -0.07,
    "cleQt3Re" : -0.01
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
def make_scanpts_file(start_pt_type, wc_names_list, wc_lims_dict, scanfile_name, ref_pt_dict=None):

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
        "ctWRe"   : [-4,4], 
        "ctBRe"   : [-4,4],
        "ctHRe"   : [-11,41],
        "cHQ1"  : [-8,28],
        "ctGRe"   : [-2,2],
        "cbWRe"   : [-5,5],
        "cHQ3"  : [-10,4],
        "cHtbRe"  : [-18,18],
        "cHt"   : [-24,13],
        "cQl3" : [-8,7],
        "cQl1" : [-6,7],
        "cQe"  : [-6,6],
        "ctl"  : [-6,7],
        "cte"  : [-6,7],
        "cleQt1Re" : [-9,8],
        "cleQt3Re" : [-2,2],
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
    file_name_lst = ["startpts_scale_by_1p1_SMEFT"]
    for f_name in file_name_lst:
        d = open_json(f_name)
        for process_name,process_startpt in d.items():
            for wc_name in WC_NAMES_LST:
                if wc_name not in process_startpt:
                    process_startpt[wc_name] = 100.
            save_name = f_name+"_"+process_name+".txt"
            print(save_name)
            make_scanpts_file("ref",WC_NAMES_LST,make_lims_dict(process_startpt),save_name,ref_pt_dict=process_startpt)
    #'''


main()






