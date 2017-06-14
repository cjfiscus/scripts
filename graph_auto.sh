#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks=10
#SBATCH --mem-per-cpu=2G
#SBATCH --output=g%j.stdout
#SBATCH --error=g%j.stderr
#SBATCH --mail-user=cfisc004@ucr.edu
#SBATCH --mail-type=ALL
#SBATCH --time=1:00:00
#SBATCH --job-name="g"
#SBATCH -p short


for f in ./*.txt 
	do
		name=$(basename "$f" | cut -d. -f1) # var for filename, no ext
		
		echo "$f"
		echo "$name"
		Rscript auto.R $f $name
		
		echo "$f done"
	done
