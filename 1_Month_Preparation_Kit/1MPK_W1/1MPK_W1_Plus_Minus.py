#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos, neg, zer = 0,0,0
    for i in arr:
        if i > 0:
            pos +=1
        elif i < 0:
            neg += 1
        else :
            zer +=1
        
    size = len(arr)
    print(f'{(pos/size):.6f}\n{(neg/size):.6f}\n{(zer/size):.6f}\n')
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
