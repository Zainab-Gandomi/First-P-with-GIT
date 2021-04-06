

import sys

infilename = sys.argv[1]
outfilename = sys.argv[2]
   
infile = open(infilename)
outfile = open(outfilename,'w')

for line in infile:
    line = line.strip("\n")
outfile.write(str(len(line))) + "\n"
    
infile.close()
outfile.close()

