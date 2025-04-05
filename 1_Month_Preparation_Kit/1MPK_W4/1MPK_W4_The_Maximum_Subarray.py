#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

### O(n) space ; O(n) time
def maxUsing_maxSubarray(arr):
    if arr == []:
        return '0 0'
    
    ## subsequences can jump negative values, subarr does not
        
    subarr = [arr[0]]
    subseq = [arr[0]]
    
    for i in range(1, len(arr)) : 
        subarr.append(max(subarr[i-1] + arr[i], arr[i]))
        subseq.append(max(subseq[i-1], subseq[i-1] + arr[i], arr[i]))
    
    max_subarr = max(subarr)
    max_subseq = subseq[-1]
    # return f'{max_subarr} {max_subseq}'
    return [max_subarr, max_subseq]
    
    
## use cmp instead of max ... ?
### O(n) space ; O(n) time
def cmp_maxSubarray(arr):
    if arr == []:
        return [0,0]
    
    ## subsequences can jump negative values, subarr does not
        
    subarr = [arr[0]]
    max_subseq = arr[0]
    
    for i in range(1, len(arr)) : 
        curr_val = arr[i]       
        ## SUBARR
        subarr.append(max(subarr[i-1] + arr[i], arr[i]))
        
        ## SUBSEQ : avoid max_of_3
        ## ## ## subseq.append(max(subseq[i-1], subseq[i-1] + arr[i], arr[i]))
        if curr_val > 0 :
            if max_subseq > 0 :
                max_subseq += curr_val
            else :
                max_subseq = curr_val
        else : 
            if curr_val > max_subseq:
                max_subseq = curr_val
            else : 
                pass
    
    max_subarr = max(subarr)
    # return f'{max_subarr} {max_subseq}'
    return [max_subarr, max_subseq]
    
    
    
## KADANE 'S ALGORITHM
## O(1) space, O(n) time !!! 
def maxSubarray(arr):
    # Write your code here
    if not arr:
        return [0,0]    
    
    ## max subarray : Kadane's Algorithm
    curr_max = arr[0]        
    max_subarr = arr[0]     
    sizeArr = len(arr)
    for i in range(1, sizeArr):
        ## if parSum ever goes negative , 
        ## and then we get a positive number, just take the positive 
        ## (start a new seq to compare against highest seq)
        curr_max    = max( curr_max + arr[i], arr[i] )
        max_subarr  = max( max_subarr, curr_max )
    
    ## max subsequence 
    max_subseq = max(arr)
    if max_subseq > 0:
        max_subseq = sum(x for x in arr if x > 0)
    ## if max value in arr is negative, let's just keep the one closest to 0 :/

    return [max_subarr, max_subseq]




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
