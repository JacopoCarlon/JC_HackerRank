#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    ## n = number of pages, ordered 0.1 2.3 4.5 6.x
    ## p = target page to see
    
    outPages = (n+1) if n%2==1 else n+2
    leftPos = p//2
    righPos = (outPages - p -1) // 2
    
    return leftPos if leftPos < righPos else righPos
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
