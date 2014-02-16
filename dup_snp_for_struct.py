# Duplicate SNP Data for STRUCTURE v.2
# Chris Fiscus
# 2/3/14

def main():
    f_r = open("reformatted.txt", "r")
    f_w = open("outfile.txt", "w")

    x = 0 

    for line in f_r:
        
        if x == 0:
            line = line.replace("rs", "") 
            f_w.write(line)

        else:
            f_w.write(line)
            f_w.write(line)

        x = x + 1



    f_r.close()
    f_w.close()

main()
