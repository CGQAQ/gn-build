#!/usr/bin/env python3

import sys;
import os;
import subprocess as sbp

def main():
    if sys.version_info[0] < 3 or sys.version_info[1] <= 6:
        raise Exception("Must be using Python 3.6 or higher")
    exe = sys.executable
    bin_suffix = ".exe" if sys.platform == "win32" else ""

    try:
        os.makedirs("./bin/ninja", exist_ok=True)
        os.makedirs("./bin/gn", exist_ok=True)
    except OSError as e:
        pass

    # build ninja
    print("Building ninja...")
    ret = sbp.run([exe, '../../tools/ninja/configure.py', '--bootstrap'], stderr=sys.stderr, stdout=sys.stdout, cwd="./bin/ninja").returncode
    if ret == 0:
        print("ninja build successful")
    else:
        print("ninja build failed")
        return 1
    
    print("---------------------------------------")

    # build gn
    print("Building gn...")
    ret = sbp.run([exe, './build/gen.py'],  stderr=sys.stderr, stdout=sys.stdout, cwd="./tools/gn").returncode
    if ret == 0:
        print("gen ninja.build successful")
    else:
        print("gen ninja.build failed")
        return 1

    print(f'./bin/ninja/ninja{bin_suffix} -C ../../tools/gn/out/ ')
    ret = sbp.run([f'./bin/ninja/ninja{bin_suffix}', '-C', "out"],  stderr=sys.stderr, stdout=sys.stdout, cwd="./tools/gn/").returncode
    if ret == 0:
        os.rename(f"./tools/gn/out/gn{bin_suffix}", f"./bin/gn/gn{bin_suffix}")
        print("gn build successful")
    else:
        print("gn build failed")

if __name__ == '__main__':
    main()