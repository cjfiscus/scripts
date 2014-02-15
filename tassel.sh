#!/bin/bash

cd /Users/cjfiscus/tassel4-standalone 

./run_pipeline.pl -fork1 -importGuess ./Tut_Data/d8_sequence.phy -fork2 -importGuess ./Tut_Data/mdp_population_structure.txt -fork3 -importGuess ./Tut_Data/mdp_traits.txt -combine4 -input1 -input2 -input3 -intersect -glm -glmMaxP 1e-3 -glmOutputFile ./test -runfork1 -runfork2 -runfork3

