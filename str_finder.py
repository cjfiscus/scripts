# String Finder
# by Chris Fiscus
# 2017-02-17
#
# This script finds a string in a line in a file and if the line contains the string writes the line to an out file. 

File=open("aralip_data.txt", 'r')
OutFile=open("out.txt", 'w') 

string1= "Suberin Synthesis & Transport 1"
string2= "Suberin Synthesis & Transport 2"
string3= "Suberin Synthesis & Transport 3"

for Line in File:
	if string1 in Line:
		OutFile.write(Line)
	if string2 in Line:
		OutFile.write(Line)
	if string3 in Line:
		OutFile.write(Line)
		
File.close()
OutFile.close()