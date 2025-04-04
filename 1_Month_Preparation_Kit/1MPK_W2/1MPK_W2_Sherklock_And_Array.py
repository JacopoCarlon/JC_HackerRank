#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def optimized_balancedSums(arr):
    total_sum = sum(arr)
    left_sum = 0
    for num in arr:
        if left_sum == (total_sum - left_sum - num):
            return "YES"
        left_sum += num
    return "NO"


def balancedSums(arr):
    # Write your code here
    size = len(arr)
    left = -1
    right = size
    
    sl = 0
    sr = 0
    
    if size == 0 or size == 1 :
        return "YES"
    if size == 2 :
        return "YES" if arr[0]==0 or arr[1]==0 else "NO"
    
    while left + 2 <= right :
        if sl == sr :
            if left + 2 == right:
                return "YES"
            else :
                ## i move adding the least possible 
                ## if <eq.0.0.0.0.7.eq> i should move to get ...eq.7.eq
                if arr[left+1] > arr[right-1] :
                    right -= 1
                    sr += arr[right]
                elif arr[left+1] < arr[right-1]:
                    left += 1
                    sl += arr[left]
                else : 
                    ## i move both (they had distance 2, distance is checked in all whiles)
                    right -= 1
                    sr += arr[right]
                    left += 1
                    sl += arr[left]
        while left < right and sl < sr :
            left += 1
            sl += arr[left]
        while left < right and sr < sl :
            right -= 1
            sr += arr[right]
    
    return "NO"
    
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
