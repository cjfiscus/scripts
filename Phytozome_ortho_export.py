# Identify Orthologous Genes in Phytozome 
#
# by Chris Fiscus
# 2017-02-23
# 
# Python 3.x script that, given a list of genes, exports identified orthologs in another species from the Phytozome dataset in a tab-delimited file. 
# 	
# NOTE
# Input file must be tab-delimited with one GeneID per line. 
# Phytozome database in file Phytozome.txt required. 

# Find orthologs in Phytozome #

def orthoid():
	Gene_List = input("Enter query list of genes (ex. genes.txt): ")	# Ask user for input filename
	 
	InFile=open(Gene_List, 'r') 										# File containing gene list to search

	Export_List = input("Enter name of outfile (ex. orthologs.txt): ") 	# Query user for output filename
	
	OutFile=open(Export_List, 'w')										# File where orthologs will be written 

	Search = []  														# list of genes to search for 

	species = input("Enter species to return orthologs from (ex. Osativa) or ALL to return orthologs from all species: ") # species to return from Phy by ClusterID
	
	species = species.lower()											# makes search easier later

	# Create query list of genes

	for Line in InFile: 
		Line = Line.lower()       				# remove case 
		Line = Line.split('\t')   				# split by tab
		Search.append(Line[0].strip('\n'))    	# add gene name to list, name must be in position [0]
	
	InFile.close()

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

	Phy.close()									# Necessary to undo splitting 
										
	print(matches, "ClusterID matches in Phytozome.")


	# Find orthologs in species of interest # 

	Phy=open("Phytozome.txt", 'r')

	matches = 0 								# track hits in database

	for Line in Phy:
		w = Line 								
		Line = Line.lower()						# std format of line
		Line = Line.split('\t')
	
		if Line[3] in ClusterID:				# ClusterID match
			if species == "all":				# write to outfile
				OutFile.write(w)
			
			elif Line[0] == species:			# Species name match
				OutFile.write(w)				# write to outfile 
			matches = matches + 1	
				
	Phy.close()									# Close files 
	OutFile.close()
	
	print(matches, "orthologs in " + species) 	# Edit to reflect species name 

orthoid()										# run this thang 