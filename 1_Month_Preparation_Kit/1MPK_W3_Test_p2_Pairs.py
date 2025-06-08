#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


## Pairs

# O(n) time , O(n) space
def pairs(k, arr):
    if k == 0:
        return 0
    s = set(arr)
    return sum(1 for num in arr if num - k in s)


def good_pairs(k, arr):
    arr_set = set(arr)
    num_pairs = 0
    
    for num in arr_set:
        if num + k in arr_set:
            num_pairs += 1
    
    return num_pairs
    
    
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
