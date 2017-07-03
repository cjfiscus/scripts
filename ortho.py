# Ortholog Pipeline to Identify Arabidopsis Orthologs in Rice 
#
# by Chris Fiscus
# 2017-02-16
# 
# Python 3.x script that, given a list of Arabidopsis genes, finds identified orthologs in rice from the Phytozome dataset
# and then exports expression data for the selected genes. 
#
#
# Files required in working directory:
#
# arabidopsis_genes.txt of format (tab-delimited):
# GENE_ID	etc. 
# ----------
# Phytozome.txt of format (tab-delimited):
# Organism.name	Gene.Name	Description	Cluster.ID
# ----------
# RAP-MSU_2016-08-05.txt of format (tab-delimited): 
# Os01g0100100	LOC_Os01g01010
# ----------
# RpkmExonsBygenes_Big_exp_R1_test_ID_clust.txt of format (tab-delimited):
# 	X	ABCDEFG	ABCDEFG	ABCDEFG	ABCDEFG etc. 
#	1	GENE_ID	0.000000000	0.000000000	0.000000000 etc. 
# ----------
# 
# Output files:
#
# selected_genes. txt
# Expression data of rice orthologs. 
# ----------
# temp.txt 
# Initial input gene list with duplicates removed. 
# ----------
# orthos.txt
# Phytosome search results for rice by ClusterID gathered from Arabidopsis genes. 
# ----------
# orthos2.txt
# orthos.txt with both RAP and MSU GeneIDs.  

# Duplicate Remover #

def dup_chk():
	InFile=open("arabidopsis_genes.txt", 'r') 	# Initial input file 

	OutFile=open("temp.txt", 'w')

	Compare = [] 								# gene list 

	duplicates = 0 								# count for number of duplicates

	for Line in InFile:
		w = Line								# Capture line to write in new file if not duplicate
		Line = Line.lower()       				# remove case 
		Line = Line.split('\t')   				# split by tab
	
		if Line[0] in Compare:					# check for duplicates
			duplicates = duplicates + 1		
		
		else:									# Not a duplicate
			Compare.append(Line[0])				# Add to list to check against	
			OutFile.write(w)					# Write line to new file 

		
	print(duplicates, "duplicate genes removed.")
	
	InFile.close
	OutFile.close
	

# Find orthologs in Rice using Phytozome #

def orthoid():
	InFile=open("temp.txt", 'r') 				# File containing gene list to search

	OutFile=open("orthos.txt", 'w')

	Search = []  								# list of genes to search for 

	# Create query list of genes

	for Line in InFile:
		Line = Line.lower()       				# remove case 
		Line = Line.split('\t')   				# split by tab
		Search.append(Line[0].strip('\n'))    				# add gene name to list, name must be in position [0]
	
	InFile.close

	# Search for queries in Phytozome # 

	Phy=open("Phytozome.txt", 'r')				# Phytozome file 

	matches = 0 								# count of matches in Phy	

	ClusterID = []								# ClusterIDs to retrieve

	for Line in Phy:
		w = Line
		Line = Line.lower()						# std format of line
		Line = Line.split('\t')
	
		if Line[1] in Search: 					# If gene is in Phytozome
			ClusterID.append(Line[3])			# ClusterID added to list
			matches = matches + 1				

	Phy.close()									
	print(matches, "ClusterID matches in Phytozome.")


	# Find orthologs in rice # 

	Phy=open("Phytozome.txt", 'r')

	matches = 0 

	for Line in Phy:
		w = Line 								
		Line = Line.lower()						# std format of line
		Line = Line.split('\t')
	
		if Line[3] in ClusterID:				# ClusterID match
			if Line[0] == 'osativa':			# Species name match (edit for dif. species)
				OutFile.write(w)				
				matches = matches + 1 
	Phy.close()
	OutFile.close()
	print(matches, "orthologs in Rice.") 		# Edit to reflect species name 
	
# RAP to MSU IDs #

def rap2msu():
	InFile=open("orthos.txt", 'r') 					# File containing gene list

	Db=open("RAP-MSU_2016-08-05.txt", 'r')  		# Database file with conversions

	OutFile=open("orthos2.txt", 'w')				

	d = {} 											# dict.

	# Make a database of the names
	for Line in Db:
		Line = Line.lower()    						# std format of line
		Line = Line.strip('\n')  
		Line = Line.split('\t')
		d.update({Line[1]:Line[0]}) 				# add to dict. 

	# Check and replace names 
	for Line in InFile:
		Line = Line.lower()      					# std format of line
		Line = Line.split('\t')  
	
		if Line[1] in d.keys():						# chk if in dict. 
			new = d.get(Line[1])					# retrieve value from dict. 
			Line[1] = str('\t'+Line[1]+'\t'+new+'\t')	# write as tab-delimited format 
			q = "".join(Line)
			OutFile.write(q)
	
	
	InFile.close()
	OutFile.close()

# Export Expression Data #
def export():
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
	OutFile.close()

# Call functions # 
dup_chk() 	
orthoid()
rap2msu()
export()
