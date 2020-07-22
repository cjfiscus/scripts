#!/usr/bin/env python3
# generate random nt seqs
# usage
# python gen_ran_seqs.py LENGTH HOWMANY

import sys
import random

def get_random_string(length):
    # put your letters in the following string
    sample_letters = 'ATCG'
    result_str = ''.join((random.choice(sample_letters) for i in range(length)))
    print(result_str)

for i in range(int(sys.argv[2])):
    print(">RANDOM_" + str(i))
    get_random_string(int(sys.argv[1]))
