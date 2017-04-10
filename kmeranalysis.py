# K-mer Count Analysis
# by Chris Fiscus
# 2017-04-06
#
# This script compares the K-mer counts from two jellyfish dump files and computes statistics. 
#
# Produces tab-delimited outfiles of format:
# K-mer	Count1	Count2
# GCGAGGTTACCATTTCT	1	1

# Files to compare, change this
InFile1=open("Morex_test.txt", "r")		# File 1 (WGS data)
InFile2=open("Morex_test1.txt","r")		# File 2 (RAD-Seq data)

# Outfiles 
OutFile1=open("kmercompare.txt","w")		# same as InFile1 in uniqueKs(), need to assign this to a variable 

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
	

def uniqueKs():
	InFile1=open("kmercompare.txt","r")		# same as outfile1, change 
	OutFile2=open("uniquekmers.txt","w")	# all unique K-mers (count = 1)
	OutFile3=open("filtered.txt", "w")		# unique K-mers (count = 1 in File 1 only)
	
	LineNo = 0	# Number of kmers in file (header is [0])
	
	zeros=0	# count of unique kmers
	
	errors=0	# count of unique kmers from file 2 (RAD-Seq unique Kmers must be errors) 
	
	WGS_unique=0 # count of unique kmers from file 1 (WGS data)
	
	uniqueKmers=[]	# list of unique kmers 
	
	filtered=[]		# list of kmers that aren't errors (unique Kmers in RAD-seq data must be errors)
	
	for Line in InFile1:
		if LineNo > 0:
			LineNo = LineNo + 1 
			Check = Line.split('\t')	# make indexable 
		
			Check[2] = Check[2].strip('\n')	# remove newline character from second item
		
			if int(Check[1]) == 0:		# if count is 0 for this kmer in file 1 but exists in file 2
				zeros=zeros+1
				uniqueKmers.append(Line)
				
				errors = errors + 1
				
			elif int(Check[2]) == 0:	# if count is 0 for the kmer in file 2 but exists in file 1
				zeros=zeros+1
				uniqueKmers.append(Line)
				filtered.append(Line)
				WGS_unique = WGS_unique + 1
				
			else:	# no zero in line, add to filtered dataset 
				filtered.append(Line)
				
				
		else:
			LineNo = LineNo + 1
			
	# Write OutFiles containing unique K mers
	OutFile2.write("K-mer\tCount1\tCount2\n")	# unfiltered
	OutFile3.write("K-mer\tCount1\tCount2\n")	# filtered
	
	for uniqueKmer in uniqueKmers:
		OutFile2.write(uniqueKmer)
		
	for Kmer in filtered:
		OutFile3.write(Kmer)
	
	InFile1.close()
	OutFile2.close()
	OutFile3.close()
	
	print(str(LineNo) + " K-mers, " + str(zeros) + " unique, " + str(errors) + " errors")
	
	print()		# print empty line
		
	count_unique = (zeros/LineNo)*100		# calculate % of unique K-mers 
	
	print(str(count_unique)+ "% of K-mers are unique (total count = 1 between both files).")
	
	print()
	
	count_unique1= (WGS_unique/LineNo)*100 
	
	print(str(count_unique1)+ "% of K-mers are present in File 1 but not File 2.")
	
	

kmercompare()	
uniqueKs()