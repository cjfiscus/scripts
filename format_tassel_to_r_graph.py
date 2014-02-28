# Format TASSEL output for R Manhattan Plot Program
# Chris Fiscus
# 2/28/13
#
# Formats TASSEL output for input into gwas_plots.r
# Follow this script with a sed command to replace "NaN" with "NA" (for R)

def main():

    file = open("glm_3.txt", "r") # read this file (no edit to source file)

    file_w = open("glm_graph_3.txt", "w") # write to this file

    y = [] # empty list

    z = 0 # denotes first line

    for line in file: # do this for every line in the file
        if z > 0: # if not first line
            x = line.split() # split the line at the spaces
            y.append(x[1]) # add value of x[1] to list y 
            x[2] = x[2].replace('chr','') # same as above but strip chr
            y.append(x[2]) # etc
            y.append(x[3])
            y.append(x[6])

            file_w.write(' '.join(y)) # write contents of y to line 
            file_w.write('\n') # add newline
            del y[:] # empty y for next iteration

        else:
            file_w.write('SNP CHR BP P \n') # header line
            z = z + 1 # first line is done

    file.close # close input
    file_w.close # close output 

main()
        
        
