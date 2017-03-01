# Add Short Gene Name
# by Chris Fiscus 
# 2017-02-28
# 
# Python 3 script that takes a list of genes from a file, searches a list from another file that has short gene names,
# and writes an outfile that adds the short gene name to the GeneID if it exists. 

# File operations

InFile=open("exp.txt","r")			# expression data	
OutFile=open("out.txt","w")			# outfile 
db=open("annotation_new.txt","r")	# file containing long and short names 

search=[]

# Build a list of genes to search for in db 
for Line in InFile:  # do this for every line in InFile

	w = Line
	
	Line = Line.lower()
	Line = Line.split('\t')  # make objs indexable 
	
	search.append(Line[1])	# build a list of genes to search for 

	
InFile.close()				# Will deal with this again later 

d = {}

# Find genes in db and store short name in dictionary 
for Line in db:
	
	Line = Line.lower()						# Make parsing easier 
	Line = Line.split('\t')
	
	if Line[1] in search:					# gene is in search list 
		if str(Line[3]) == "na":			# If gene name exists 
			pass
		elif str(Line[3]) == "_":			
			pass
		else:								# Gene name exists
#			OutFile.write(Line[1] +'\t'+ Line[3]+'\n')
			d.update({Line[1]:Line[3]})		# write to dictionary
			
db.close()

InFile=open("exp.txt","r")

# Write Outfile with short gene names added (if they exist)

for Line in InFile:
	Line=Line.lower()
	Line=Line.split('\t')
	
	if Line[1] in d.keys():					# if gene is in dictionary (short gene name exits)
		
		gene = d.get(Line[1])				# assign value to var
		
		Line[1] = (Line[1]+' ('+gene+')')	# formatting
		Line[1] = Line[1].upper()			# formatting
		
		Line = "\t".join(Line)				# join line indices with tab
		
		OutFile.write(Line)					
		
	else:									# no short gene name for these 
		Line = "\t".join(Line)						# format and write to outfile
		Line= Line.upper()		
		OutFile.write(Line)	
		
InFile.close()
OutFile.close()
