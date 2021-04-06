# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 11:11:43 2021

@author: zainab
"""

import sys

infile = sys.argv[1]
outfile = sys.argv[2]
infile = open(infile)
outfile = open(outfile,'w')
for line in infile:
    line = line.strip("\n")
outfile.write(str(len(line))) + "\n"
infile.close()
outfile.close()