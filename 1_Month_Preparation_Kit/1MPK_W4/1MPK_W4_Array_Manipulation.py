#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    # Write your code here
    # Will be using a difference-array, which will keep trace 
    # of starting and ending points of the bumps in the [0]*n array
    
    # Initialize the difference array with n+1 elements to avoid index issues
    diff = [0] * (n + 1)  # indices 0 to  
    # (remapping 1-indexed array to 0-indexed, and keeping +1 for easy last bound check)
    for a, b, k in queries:
        a -= 1  # convert to 0-based index
        b -= 1  # convert to 0-based index
        diff[a] += k
        if b + 1 < n:
            diff[b + 1] -= k
    
    # array is initialized at 0, so makes sense since k >= 0 per contraints
    max_value = 0 
    current = 0
    for i in range(n):
        current += diff[i]
        if current > max_value:
            max_value = current
    return max_value
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
