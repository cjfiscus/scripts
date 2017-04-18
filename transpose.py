## Tranpose Matrix
## Python 3 script that tranposes tab-delimited data contained in an input file and writes to an output file
##
## by JB Landis  
## fixed by CF 
# for some reason Python wouldn't strip the newline character, but I could get it to print. 

import itertools

with open("Sample.vcf") as f, open("Transposed.vcf", "w") as g: # f is input, g is output 
    try:
        for column_index in itertools.count():		
            f.seek(0)
            col = [line.split('\t')[column_index] for line in f]
            col =map(str.strip,col)			# brute force strip EVERYTHING not a string 			
            g.write("\t".join(col)+'\n')	# write to outfile 
    except IndexError:
        pass