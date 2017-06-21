## File Splitter
## by Chris Fiscus
## 2017-06-20
##
## This script splits large text files into files containing 1,000,000 lines each.
## 
## Run this script as follows:
## $ python3 file_splitter.py FILE.txt

import sys # required to use sys.args
import os

## Input file
FiletoOpen=sys.argv[1] # filename provided in sys arg

File=open(FiletoOpen, "r") # open file to read

LineNo=1 # Number of Lines

## Count number of lines in File
for Line in File:
    LineNo = LineNo + 1

File.close() # not doing this messes up for loop later

NumFiles= int(LineNo/1000000) + (LineNo % 1000000 > 0)

coords = [] # empty list for coordinates for file splitting

## Determine how many files to create
for i in range(0,NumFiles):
    coords.append(1000000*i)

## Initialize variables
LinesWritten=1
i = 0   # index of coords[]
nex = int(i + 1)

OutFileName= FiletoOpen + str(i)
Out=open(OutFileName, "w") # open first outfile

File=open(FiletoOpen, "r") # Re-open file to read from

## iterate
for Line in File:
    ## Write to file
    Out.write(Line)
    LinesWritten = LinesWritten + 1

    try: # error handling
        if LinesWritten <= coords[nex]:
            pass

        else:
            Out.close() # close last file
            i = i + 1 # adjust variables for NEXT file
            nex = int(i + 1)
            OutFileName= FiletoOpen + str(i) # open next outfile
            Out=open(OutFileName, "w")

    except: # out of range
        pass

# dump from memory
File.close()
Out.close()
