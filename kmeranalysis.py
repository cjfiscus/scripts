# K-mer Count Analysis
# by Chris Fiscus
# 2017-04-06
#
# This script compares the K-mer counts from two jellyfish dump files and computes statistics. 
#
# Produces tab-delimited outfile of format:
# K-mer	Count1	Count2
# GCGAGGTTACCATTTCT	1	1

# Files to compare, change this
InFile1=open("Morex_test.txt", "r")		# File 1
InFile2=open("Morex_test1.txt","r")		# File 2

# Outfiles 
OutFile1=open("out.txt","w")

def kmercompare():
	# Dictionary {Kmer:Count1\tCount2}
	kmers = {}

	# Processing File 1 
	for Line in InFile1:
		if Line.startswith(">"):
			# count 
			count = Line.strip('>')	# parsing
			count = count.strip('\n')
		
			# kmer
			kmer = next(InFile1)	# get next line (Kmer)
			kmer = kmer.strip('\n')	# parsing 
								
			kmers.update({kmer:count})	# add to dictionary
					
		else:
			pass
		
	for Line1 in InFile2:
		if Line1.startswith(">"):
		
			# count 
			count2 = Line1.strip('>')	# parsing
			count2 = count.strip('\n')
		
			# kmer
			kmer2 = next(InFile2)	# get next line (Kmer)
			kmer2 = kmer2.strip('\n')	# parsing 
		
			if kmer2 in kmers.keys():	# kmer exists in first file
				# amend existing key in dictionary 
				amend = kmers.get(kmer2)
				amend = str(amend + '\t' + count2)
				kmers.update({kmer2:amend})
			
			else: 						# kmer exists in second file but not first file 
				# create new dictionary key 
				new = str('0\t'+ count2) # not found in File 1
				kmers.update({kmer2:new})

	# write to OutFile	
	OutFile1.write("K-mer\tCount1\tCount2\n")

	for key in kmers.keys():
		# kmers that exist in first file but not second file 
		if kmers[key].count('\t') == 0:		# tabs haven't been added yet. 
			amend = kmers.get(key)			# lookup in dictionary
			amend = str(amend + '\t0')		# add 0
			kmers.update({key:amend})		# amend value in dict. 
	
		# Write dictionary to outfile with proper formatting		
		OutFile1.write(str(key) + '\t' + kmers[key] + '\n')
	


	InFile1.close()
	InFile2.close()
	OutFile1.close()
	
kmercompare()

def compute_stats():
	pass
	# parse output file line by line, splitting at tabs. 
	# check if [0] or [1] is 0. 
	# if zero add to unique list for that file (write to unique file)
	# count total number of K-mers, % of kmers represented 