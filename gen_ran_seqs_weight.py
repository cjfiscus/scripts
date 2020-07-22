#!/usr/bin/env python3
# generate random nt seqs
# usage
# python gen_ran_seqs.py LENGTH HOWMANY

import sys
import random
length=int(sys.argv[1])

def get_random_string(length):
    print("".join(random.choices(population=["A","T","C","G"], weights=[0.64, 0.64, 0.36, 0.36], k=length)))

for i in range(int(sys.argv[2])):
    print(">RANDOM_WEIGHTED" + str(i))
    get_random_string(length)
