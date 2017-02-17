# This script exports expression data for selected genes in rice #
# By Chris Fiscus 
# 2017-02-16
#
InFile=open("RpkmExonsBygenes_Big_exp_R1_test_ID_clust.txt", 'r') # File containing gene list to search

Db=open("orthos2.txt", 'r')  # Database file with conversions

OutFile=open("selected_genes.txt", 'w')

GeneID = []

# Make a list of genes to search for 
for Line in Db:
	Line = Line.lower()      
	Line = Line.split('\t') 
	
	if Line[2] != 'none':	#ignore the missing data
		GeneID.append(Line[2]) #add good data to list 
		
	else:		# do nothing
		pass
		
count = 0
for Line in InFile:
	if count > 0:	# not first line 
		w = Line
		Line = Line.lower()
		Line = Line.split('\t')
		
		if Line[1] in GeneID:
			OutFile.write(w)
	
	else:			# write first line
		OutFile.write(Line)
		count = count + 1
	
	
	
InFile.close()

Db.close()
		
OutFile.close()

