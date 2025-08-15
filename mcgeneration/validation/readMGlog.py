'''
This script processes the logs made by `gridpack_scan.sh`.
Example:
python3 readMGlog.py log_ttlnu_cHQ3
'''
import os
import argparse
import json

def skim_MGlog(inFile, outFile):
    p_dict = {}
    with open(outFile, "w") as output: 
        #output.write(f"\"{inFile.split('_')[-1]}\": {{")
        proc = inFile.split('_')[-1]
        p_dict[proc] = {}
        with open(inFile, "r") as input: 
            curr = ''
            skip=False
            for line in input:
                
                if "Summary" in line.strip("\n"):
                    if 'run_' in line: skip=True
                    if 'run_' in line: continue
                    skip=False
                    ### strip and lstrip also remove "S" from the SM point name so I switched to the .find method
                    ### line=line.strip("tag: tag_1 ===") works interactively but not when run in the script 
                    ### I have no clue why so instead just use line.find
                    # line=line.lstrip("=== Results Summary for run:")
                    # line=line.rstrip("tag: tag_1 ===")

                    index=line.find("run:")+5   #find index for first character after "Results Summary for run: "
                    line=line[index:]           #shorten line to remove those characters
                    line=line[:line.find("tag")]+'\n'   #remove "tag: tag_1 ===" from the end
                    #output.write(line)
                    if 'SM' in line:
                        curr = '0'
                    else:
                        curr = line.strip().split('=')[1]
                    p_dict[proc][curr] = 0

                if "Computing" in line.strip("\n") and not skip:
                    ### strip and lstrip also remove "S" from the SM point name so I switched to the .find method
                    ### line=line.strip("tag: tag_1 ===") works interactively but not when run in the script 
                    ### I have no clue why so instead just use line.find
                    # line=line.lstrip("=== Results Summary for run:")
                    # line=line.rstrip("tag: tag_1 ===")

                    index=line.find("Computing")+10
                    line=line[index:]           #shorten line to remove those characters
                    line=line[:line.find("tag")]+'\n'   #remove "tag: tag_1 ===" from the end
                    #output.write(f'"{line.strip()}": ')
                    if 'SM' in line:
                        curr = '0'
                    else:
                        curr = line.strip()
                    p_dict[proc][curr] = 0
                    skip = False


                if "Cross-section :" in line.strip("\n") and not skip:
                    line=line.strip("     Cross-section :   ")
                    #output.write(f'{line.split(" ")[0]}, ')
                    p_dict[proc][curr] = float(line.split(" ")[0])
        #output.write('}')
        json.dump(p_dict, output)

    print(f"saving to {outFile}")
    print(json.dumps(p_dict))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Command Line options parser")
    parser.add_argument("logFile", help="MG log file to be read")
    parser.add_argument("--outname", '-o', default="MG_xsec", help="output file name")
    args = parser.parse_args()

    logFile = args.logFile
    outname = args.outname

    outFile = f"{outname}.txt"

    skim_MGlog(logFile, outFile)
