#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    arr.sort()
    
    size = len(arr)
    if size == k:
        return arr[-1] - arr[0]

    step = k-1
    ## l = 3 -> step = 2 ;
    ## 0 1 2 3 4 5 6 ; size = 7 -> range [0, 5)
    
    mindif = arr[step] - arr[0]
    for i in range(1, size-step):
        thisDif = arr[i+step] - arr[i]
        if thisDif < mindif :
            mindif = thisDif
    
    return mindif if mindif > 0 else 0
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
