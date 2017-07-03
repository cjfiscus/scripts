# K-mer Count Reformatter 
# by Chris Fiscus
# 2017-05-06
#
# This script reformats K-mer counts from Jellyfish dump files. 
#
# Produces tab-delimited outfiles of format:
# K-mer	Count1
# GCGAGGTTACCATTTCT	1	


import sys
import os 


# get filename from arg
name = sys.argv[1]

filename=str(name+".fa")

InFile1=open(filename, "r")

# Outfiles 

OutFileName=str(name+"_counts.txt")

def mktable():
	# Dictionary {Kmer:Count1\n}
	kmers = {}
	
	OutFile1=open(OutFileName,"w")

	# Processing File 
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


	# write to OutFile	
	OutFile1.write("K-mer\tCount1\n")

	for key in kmers.keys():
		amend = kmers.get(key)			# lookup in dictionary
		amend = str(amend + '\n')		# add newline character
		kmers.update({key:amend})		# amend value in dict. 
	
		# Write dictionary to outfile with proper formatting		
		OutFile1.write(str(key) + '\t' + kmers[key])
		
#	print(str(kmers.get('AAAAAAAAAA')))			# debug
	


	InFile1.close()
	OutFile1.close()

mktable()