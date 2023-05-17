#!/usr/bin/env python3

import sys
import os
import subprocess

def main():
    if sys.version_info[0] < 3 or sys.version_info[1] <= 6:
        raise Exception("Must be using Python 3.6 or higher")
    bin_suffix = ".exe" if sys.platform == "win32" else ""

    if not os.path.exists(f"./bin/ninja/ninja{bin_suffix}"):
        # run build-tools.py
        print("ninja not found, building...")
        ret = subprocess.run([sys.executable, "./build-tools.py"], stderr=sys.stderr, stdout=sys.stdout).returncode

    # forward all arguments to ninja
    ret = subprocess.run([f"./bin/ninja/ninja{bin_suffix}"] + sys.argv[1:], stderr=sys.stderr, stdout=sys.stdout).returncode
    if ret == 0:
        print("gn runs successfully")
    else:
        print("gn failed to run")
        return 1

if __name__ == '__main__':
    main()