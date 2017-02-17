# This script searches for orthologs in the Phytozome and Outputs the results in an OutFile #
# By Chris Fiscus 
# 2017-02-16
#
InFile=open("all_edit.txt", 'r') # File containing gene list to search

OutFile=open("orthos.txt", 'w')

Search = []  # list of genes to search for 

# Create query list of genes

for Line in InFile:
	
	Line = Line.lower()       # remove case 
	Line = Line.split('\t')   # split by tab
	Search.append(Line[0])    # add gene name to list, name must be in position 0
	
InFile.close

# Search for queries in Phytozome # 

Phy=open("Phytozome.txt", 'r')

matches = 0 

ClusterID = []

for Line in Phy:
	w = Line
	
	Line = Line.lower()		# make lines readable
	Line = Line.split('\t')
	
	if Line[1] in Search: 		# If gene is in Phytozome
		ClusterID.append(Line[3])
		matches = matches + 1

Phy.close()		
print(matches, "matches in Phytozome.")


# Find orthologs in rice # 

Phy=open("Phytozome.txt", 'r')

matches = 0 

for Line in Phy:
	w = Line 
	
	Line = Line.lower()
	Line = Line.split('\t')
	
	if Line[3] in ClusterID:
		if Line[0] == 'osativa':
			OutFile.write(w)
			matches = matches + 1 
			
print(matches, "matches in Rice.") 
	

		
OutFile.close()
Phy.close()
