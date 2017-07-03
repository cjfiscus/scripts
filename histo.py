# Produce histogram from K-mer counts
# by Chris Fiscus
# 2017-04-12
# 
# Input file should be formatted like so:
# Kmer	Count
# AAAA	100

InFile = open("uniquekmers.txt","r") # file containing input of format above
OutFile = open("out.txt","w")	# outfile 

LineNo = 0 	# number of lines
count={}	# dict. of {abundance:Number of K-mers}

for Line in InFile:
	if LineNo > 1:	# skip header
		LineNo = LineNo + 1	# Line number
		 
		Line = Line.split('\t') # count in [1]
		
		num = Line[1].strip('\n')
		
		if num in count.keys():	# count has been seen before
			amend = count.get(num)	# get value for key 
			amend = int(amend) + 1	# new value 
			
			
		else:					# count is new
			amend = 1 
			
		count.update({num:amend}) # update dictionary 
		
	else:	
		LineNo = LineNo + 1
				
# write dictionary to file 
for key in count.keys():
	OutFile.write(str(key) + '\t' + str(count[key]) + '\n')
	
# done with these 	
InFile.close()
OutFile.close()
	