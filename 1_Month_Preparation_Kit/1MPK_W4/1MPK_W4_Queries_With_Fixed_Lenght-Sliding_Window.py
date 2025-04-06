#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#

# 2,10,3,11,4,12 -> 10,10,11,11,12
# 2,3,4,10,11,12 -> 3,4,10,11,12


## solution if the input is alwasy SORTED :
def ifSorted_solve(arr, queries):
    # Write your code here
    print(f'input : arr{arr}, queries{queries}')
    results = []
    for this_d in queries:
        skip = this_d-1
        results.append(queries[skip])
    
    return results
    

## single Query costs :
## Time  : O(n*1)               (deque operations are O(1))
## Space : O(d) -> wrst: O(n)   (deque max size is n)
def solve(arr, queries):   
    from collections import deque
    results = []
    arrSiz = len(arr)
    
    for this_d in queries:
        current_window = deque()
        d_min_of_max = None
        
        this_d_last_range = this_d-1
        for i in range(arrSiz):
            i_dist_req_d = i-this_d_last_range
            if current_window and current_window[0] < i_dist_req_d:
                current_window.popleft()

            while current_window and arr[current_window[-1]] < arr[i]:
                current_window.pop()

            current_window.append(i)

            if i_dist_req_d >= 0:
                if not d_min_of_max :
                    d_min_of_max = (arr[current_window[0]])
                elif d_min_of_max > arr[current_window[0]] :
                    d_min_of_max = arr[current_window[0]]
                else :
                    continue
        results.append(d_min_of_max)
    
    return results
    

    
## single Query costs :
## Time  : O(n*d) -> wrst. O(q*n^2)   (deque max size is n)
## Space : O(1)
def S1_Tn2_solve(arr, queries):
    results = []
    
    for this_d in queries:
        d_min_of_max = None
        
        for i in range(len(arr) - this_d + 1):
            current_max = max(arr[i:i+this_d])
            if not d_min_of_max :
                d_min_of_max = current_max
            elif d_min_of_max > current_max :
                d_min_of_max = current_max
            else :
                continue
            
        results.append(d_min_of_max)
    
    return results

    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
