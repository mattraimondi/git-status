#!/usr/bin/env python3

# Version 2.3

# 2019 Matthew Raimondi
# www.mattraimondi.com
# www.github.com/mattraimondi

#MIT License
#
#Copyright (c) 2019 Matthew Raimondi
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
    
    red = "\u001b[38;5;$1m"
    orange = "\u001b[38;5;$208m"
    yellow = "\u001b[38;5;$11m"
    green = "\u001b[38;5;$2m"
    blue = "\u001b[38;5;$4m"
    indigo = "\u001b[38;5;$63m"
    violet = "\u001b[38;5;$129m"
    pink = "\u001b[38;5;$13m"
    brown = "\u001b[38;5;$130m"
    white = "\u001b[38;5;$231m"
    black = "\u001b[38;5;$0m"
    
    redback = "\u001b[48;5;$1m"
    orangeback = "\u001b[48;5;$208m"
    yellowback = "\u001b[48;5;$11m"
    greenback = "\u001b[48;5;$2m"
    blueback = "\u001b[48;5;$4m"
    indigoback = "\u001b[48;5;$63m"
    violetback = "\u001b[48;5;$129m"
    pinkback = "\u001b[48;5;$13m"
    brownback = "\u001b[48;5;$130m"
    whiteback = "\u001b[48;5;$231m"
    blackback = "\u001b[48;5;$0m"
    
    reset = "\033[0m"
    clear = "\033[0m"
    
    custpink = "\u001b[38;5;$205m"
    custorange = "\u001b[38;5;$208m"
    skyblue = "\u001b[38;5;$39m"
    
    gpink = "\033[35m"
    ggreen = "\033[92m"
    gred = "\033[91m"
    
    colorversion = "10.0"
    
    def printcolor(number):
        if number >= 0 and number <= 256:
            sys.stdout.write(f"\u001b[38;5;${number}m")
        else:
            raise Exception("Number must be 0-256")

    def printbackcolor(number):
        if number >= 0 and number <= 256:
            sys.stdout.write(f"\u001b[48;5;${number}m")
        else:
            raise Exception("Number must be 0-256")


dirs = glob.glob(f"*{os.path.sep}")
gits = glob.glob("./*/.git")
numgits = len(gits)

for i in range(0, numgits):
    print(f"\n{mcolors.gpink}{gits[i]}{mcolors.clear}")
    stats = subprocess.Popen(f"cd {dirs[i]}; git status --porcelain; cd ..", shell=True, stdout=subprocess.PIPE)
    status = stats.communicate()[0]
    stat = str(status)
    if "M" in stat or "??" in stat:
        if "M" in stat:
            print(f"{mcolors.gred}Modified Files{mcolors.clear}")
        if "??" in stat:
            print(f"{mcolors.gred}Untracked Files{mcolors.clear}")
    else:
        print(f"{mcolors.ggreen}Clean{mcolors.clear}")
