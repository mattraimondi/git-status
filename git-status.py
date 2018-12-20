#!/usr/bin/env python3

# Version 2.2

# 2018 Matthew Raimondi
# www.mattraimondi.com
# www.github.com/mattraimondi

#MIT License
#
#Copyright (c) 2018 Matthew Raimondi
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


import sys
import subprocess
import os
import glob

class mcolors:
    PINK = '\033[35m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'

dirs = glob.glob('*' + os.path.sep)
gits = glob.glob('./*/.git')
numgits = len(gits)

for i in range(0, numgits):
    print("\n" + mcolors.PINK + gits[i] + mcolors.ENDC)
    stats = subprocess.Popen("cd " + dirs[i] +"; git status --porcelain; cd ..", shell=True, stdout=subprocess.PIPE)
    status = stats.communicate()[0]
    stat = str(status)
    if "M" in stat or "??" in stat:
        if "M" in stat:
            print(mcolors.RED + "Modified Files" + mcolors.ENDC)
        if "??" in stat:
            print(mcolors.RED + "Untracked Files" + mcolors.ENDC)
    else:
        print(mcolors.GREEN + "Clean" + mcolors.ENDC)
