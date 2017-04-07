scripts/
—————
convertRAP.py
python3 script to add MSU IDs (coryza) to a list of RAP IDs given the “Table of RAP and MSU's LOC_Os IDs in tab-delimited format” from rap-db, rapdb.dna.affrc.go.jp.  
—
export_exp.py
python3 script that exports lines of data containing IDs from another list. 
—
find_orthos.py
python3 script that takes a list of genes, finds the ClusterID in Phytozome db, then writes a file containing the genes that match the ClusterIDs for a second species. 
—
gene_names.py
python3 script that adds the short name to a list of genes using a second file that contains both the long and short names. 
-
kmeranalysis.py
Python 3 script that compares the K-mer counts from two jellyfish dump files and computes statistics on these counts. 
-
ortho.py
Python 3 pipeline to take a list of A. thaliana genes, removes duplicates, finds orthologs in Oryza from Phytozome db, adds MSU IDs (given RAP ID), and then exports the final list of genes from another data file (expression data, etc.). Conglomeration of convertRAP.py, export_exp.py, find_orthos.py, and process.py. 
-
Phytozome_ortho_export.py
Python 3 script that accepts a list of genes, finds the clusterIDs associated with those genes in Phytozome, and then exports a list of orthologs (identified by ClusterID) from a particular species.   
—
process.py
python3 junk script to pull data from one data table to another. 
—
README.txt
This README file.  
—
str_finder.py 
python3 script to extract lines from a file that contain one of three strings and write them to another file. 
—
