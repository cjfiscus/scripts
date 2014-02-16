#!/bin/bash

# set array to max K
#SBATCH --array=1-20

# allocate more memory (solving memory error)
#SBATCH --ntasks=2

#Set job options 
#SBATCH -D /home/cjfiscus/projects/structure/array_run
#SBATCH -o /home/cjfiscus/projects/structure/array_run/slurm-log/struct10k-stdout-%A_%a.txt
#SBATCH -e /home/cjfiscus/projects/structure/array_run/slurm-log/struct10k-stderr-%A_%a.txt
#SBATCH -J strut10
set -e
set -u

# load the module to use
module load structure-console

# run the module using K = array task id
structure -K $SLURM_ARRAY_TASK_ID 