#!/usr/bin/env python3
#version 2.1
import sys
import subprocess
import os
import glob
class bcolors:
    PINK = '\033[35m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'
dirs = glob.glob('*' + os.path.sep)
gits = glob.glob('./*/.git')
numgits = len(gits)
for i in range(0, numgits):
    print("\n" + bcolors.PINK + gits[i] + bcolors.ENDC)
    stats = subprocess.Popen("cd " + dirs[i] +"; git status --porcelain; cd ..", shell=True, stdout=subprocess.PIPE)
    status = stats.communicate()[0]
    stat = str(status)
    if "M" in stat or "??" in stat:
        if "M" in stat:
            print(bcolors.RED + "Modified Files" + bcolors.ENDC)
        if "??" in stat:
            print(bcolors.RED + "Untracked Files" + bcolors.ENDC)
    else:
        print(bcolors.GREEN + "Clean" + bcolors.ENDC)
