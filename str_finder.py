# String Finder
# by Chris Fiscus
# 2017-02-17
#
# This script finds a list of strings in a line in a file and if the line contains one of the strings writes the line to an out file. 

File=open("aralip_data.txt", 'r')				# file to search
OutFile=open("out.txt", 'w') 					# send results here
	
string1= "Suberin Synthesis & Transport 1"		# strings to search for, no reg exp
string2= "Suberin Synthesis & Transport 2"
string3= "Suberin Synthesis & Transport 3"

for Line in File:								# search for strings
	if string1 in Line:							
		OutFile.write(Line)
	if string2 in Line:
		OutFile.write(Line)
	if string3 in Line:
		OutFile.write(Line)						# will yield duplicates if more than one string found in a line of the file. 
		
File.close()
OutFile.close()