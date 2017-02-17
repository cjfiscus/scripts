# This script converts RAP to MSU IDs #
# By Chris Fiscus 
# 2017-02-16
#
InFile=open("orthos.txt", 'r') # File containing gene list to search

Db=open("RAP-MSU_2016-08-05.txt", 'r')  # Database file with conversions

OutFile=open("orthos2.txt", 'w')

d = {} # dictionary

# Make a database of the names
for Line in Db:
	Line = Line.lower()    
	Line = Line.strip('\n')   	# remove endline char
	Line = Line.split('\t')		# split at tab
	d.update({Line[1]:Line[0]}) # add to dictionary 

# Check and replace names 
for Line in InFile:
	
	Line = Line.lower()      
	Line = Line.split('\t')  
	
	if Line[1] in d.keys():
		new = d.get(Line[1])
		Line[1] = str('\t'+Line[1]+'\t'+new+'\t')
		q = "".join(Line)
		OutFile.write(q)
	
	
InFile.close

		
OutFile.close()

