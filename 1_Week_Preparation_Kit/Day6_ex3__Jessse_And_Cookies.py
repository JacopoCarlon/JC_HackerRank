#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def sort_cookies(k, A):
    # Write your code here
    size = len(A)
    srt = sorted(A)
    # print(f'SRT:{srt}')
    steps = 0
    
    if k > pow(2,size) :
        return -1
    
    while size > 2 and srt[0]<k:
        steps += 1
        least = srt[0]
        secl = srt[1]
        srt = srt[2:] ## this is too slow :(
        new = least + 2*secl
        size -= 1
        # print(f'{least}_{secl}->{new} .. ->  newSRT before insert:{srt}')
        if new <= srt[0]:
            ## then insert as first
            srt = [new] + srt
        elif new >= srt[-1]:
            ## then insert as last
            srt.append(new)
        else :
            ## insert new cookie in sorted position
            for i in range(0, size-1):
                if new < srt[i]:
                    before = srt[:i]
                    after = srt[i:]
                    srt = before[:i] + [new] + after
                    break
        # print(f'{least}_{secl}->{new} .. ->  newSRT:{srt}')
        if srt[0]>=k : 
            return steps   
    # print(f'outSRT:{srt}')
    if srt[0]>=k : 
        return steps    
    return -1
    


def cookies(k, A):
    #size = len(A)
    import heapq
    heapq.heapify(A)
    steps = 0
    
    while A[0] < k :
        if len(A) > 1:
            new = heapq.heappop(A) + 2*heapq.heappop(A)
            heapq.heappush(A, new)
            steps += 1
        else : 
            ## only one, low, cannot mix anymore
            return -1
    # lowest high enough
    return steps
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
