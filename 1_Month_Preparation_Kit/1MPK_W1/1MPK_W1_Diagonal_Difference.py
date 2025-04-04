#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    side = len(arr)
    
    countInc = 0
    countDec = 0
    parsum = 0
    middle = (side)//2 
    lastpos = side-1
    
    # 1. middle always simplifies (if odd obv), but calculating an if is costly if done each iteration
    # 2. it is better to do the difference at each step to avoid sum overflow ! ;-)
    
    for i in range(0, side):
        ###countInc = countInc + arr[i][i]     
        ###countDec = countDec + arr[i][lastpos -i]   
        countInc = arr[i][i]     
        countDec = arr[i][lastpos -i]    
        parsum = parsum + countInc - countDec
            
    ###return abs( countDec - countInc)
    return abs( parsum )
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
