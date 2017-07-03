# Kmergenie Output Parser
# by Chris Fiscus 
# 2017-04-05
#
# This script parses the best K from the Kmergenie html output file and stores it in a list and then writes list to output file.  This script also writes mean, median and mode K to stout. 
#
# NOTE: to work this script must be passed an argument upon execution using python script.py $VARIABLE (from bash) 

# import required modules and functions
import sys
import os 
import linecache	
import statistics 
#from statistics import mean
#from statistics import median
#from statistics import mode 

# get number of files from arg
high = int(sys.argv[1]) 

# List of Best Ks
List = []

# parse files 
for i in range(1 , high+1):

	# File to open, change this based on -o used by kmergenie 
	FileName="sub" + str(i) + "_report.html"
	
	# Take Line 20 which has the best K
	Read = linecache.getline(FileName, 20)
	
	# Get the best K value (parse the line)
	Read=Read.split(":")
	
	Add=Read[1].split("<")
	
	List.append(Add[0].strip(" "))
	
# Write to output 
OutFile=open("bestKs.txt","w")

# header line
OutFile.write("Best K" + '\n')

# write K values
for kmer in List:
	OutFile.write(kmer + '\n')

OutFile.close()

# change type from str to int
List = [int(i) for i in List]

# Calculate mean, median, and mode 
Mn = statistics.mean(List)

Med = statistics.median(List)

# Check is mode is unique using error handling 
try: 
	Md = statistics.mode(List)

except: # error given by statistics module, multiple modes  
	Md = "none"

# write to stdout 
print("Mean = " + str(Mn) + ", Median = " + str(Med) + ", Mode = " + str(Md)) 