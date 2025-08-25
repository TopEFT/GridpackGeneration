import os
import re

def resubmit():
    # Find all .tar.xz files less than 10 MB in size and resubmit them
    files = [f for f in os.listdir('.') if f.endswith('.tar.xz') and os.path.getsize(f) < 10 * 1024 * 1024]

    # Get list of processes from addons/cards/
    processes = [f.replace('_cards', '') for f in os.listdir('addons/cards/') if os.path.isdir(os.path.join('addons/cards/', f))]

    # Dictionary of files per process
    files_per_process = {process: [f for f in files if f.startswith(process) if 'clj1Run3' not in f] for process in processes}

    # Resubmit each file for each process
    for process, process_files in files_per_process.items():
        for file in process_files:
            long_name = file.split('run0')[0] + 'run0'
            print(f'Resubmitting {file}')

            # Extract architecture and CMSSW version from the file name
            match = re.search(r'(slc\d+_amd64_gcc\d+)_CMSSW_(\d+_\d+_\d+)', file)
            if match:
                arch = match.group(1)
                cmssw = f'CMSSW_{match.group(2)}'
                cmd = (
                    f'iscmsconnect=1 sh gridpack_generation.sh {long_name} '
                    f'addons/cards/{process}_cards/{long_name} condor INTEGRATE '
                    f'{arch} {cmssw} 2>&1 > {long_name}.debug &'
                )
                os.system(cmd)
            else:
                print(f'WARNING: Could not extract arch and cmssw rel from {file}!')
                continue


if __name__ == '__main__':
    resubmit()
