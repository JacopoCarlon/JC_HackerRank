#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

# Flipping the Matrix : Flipping_the_Matrix

def flippingMatrix(matrix):
    # Write your code here
    side = len(matrix)
    half = side // 2
    
    parSum = 0
    
    for i in range(0, half):
        for j in range(0, half):
            a0 = matrix[i][j]
            a1 = matrix[side-1 -i][j]
            a2 = matrix[i][side-1-j]
            a3 = matrix[side-1 -i][side-1-j]
            thisMax = max(a0, a1, a2, a3)
            parSum += thisMax
    
    return parSum
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
