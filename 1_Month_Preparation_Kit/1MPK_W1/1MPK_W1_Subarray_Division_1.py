#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    # lenght m
    # sum d
    
    hits = 0
    size = len(s)
    if size < m :
        return 0
    if size == m :
        return 1 if sum(s)==d else 0
    
    parsum = sum(s[0:m]) 
    if parsum == d :
        hits += 1
        
    for runner in range( size - m ) :
        parsum = parsum - s[runner] + s[runner + m]
        if parsum == d:
            hits += 1
    
    return hits
    
   
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
