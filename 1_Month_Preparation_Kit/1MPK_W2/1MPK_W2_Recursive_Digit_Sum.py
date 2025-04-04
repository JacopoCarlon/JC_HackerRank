#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    
    parsum = 0
    for i in n:
        parsum += int(i)
        
    if parsum == 0:
        return 0
        
    ## avoid multiplication overflow via : 
    ## mod(a*b) == mod( mod(a) * mod(b))
    res = ((parsum%9)*k)%9
    
    
    return 9 if res==0 else res
    
    
    
    
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
