#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    # Write your code here
    mod = 10**9 + 7
    
    # Row Width 0:1 -> 1 way
    # Row Width 1:1 -> 1
    # Row Width 2:2 -> 2, 1+(1) 
    # Row Width 3:4 -> 3, 21, 1(2), 1(11) ->
    # Row Width 4:8 -> 4, 31, 211, 22, 1(3), 1(21), 1(12), 1(111)
    # Row Width 5:15 -> 41, 311, 2111, 212, 221, 23, 32,   
    #                 1(4) 1(31) 1(211) 1(22) 1(13) 1(121) 1(112) 1(1111)
    widthRowsCombs = [1,1,2,4]
    
    while len(widthRowsCombs) <= m:
        widthRowsCombs.append(sum(widthRowsCombs[-4:]) % mod)
        
    # get all possible combinations by height of our building
    totalCombs = [ pow(val, n, mod) for val in widthRowsCombs ]
    
    invalid = [0, 0] ## 
    for it in range(2, m+1):
        # iterate vertical lines
        tmp = []
        for linWidth in range(1, it):
            ## moving the col to the right gradually, 
            ## multiply possible stable walls on the left
            ## with unstable rows to the right
            ## so we get effectively invalid data
            left = totalCombs[linWidth] - invalid[linWidth]
            right = totalCombs[it -linWidth]
            tmp.append(left*right % mod)
        invalid.append(sum(tmp) % mod)
    
    return ( totalCombs[m] - invalid[m]) % mod
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
