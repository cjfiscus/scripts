#!/usr/local/bin/python3
#
## File reformatter
## cjfiscus
## 
## Accepts as input a file formatted as follows (tsv):
##  col1    col2 
##  Gene1   Code1,Code2
##  Gene2   Code3
##
## And reformats as follows:
##  col1    col2
##  Gene1   Code1
##  Gene1   Code2
##  Gene2   Code3

File=input("File to reformat: ")
File2=input("Reformatted file: ")

## open files 
InFile=open(File, "r") 
OutFile=open(File2,"w")

for Line in InFile:
    Process=Line.split("\t") 
    
    try: # multiple entries in col1 
        Separate=Process[1].split(',')

        for i in range(len(Separate)):
            OutFile.write(Process[0]+"\t"+Separate[i].strip('\n')+"\n")

    except: # only one entry in col2
        OutFile.write(Process[0]+"\t"+Process[1])


