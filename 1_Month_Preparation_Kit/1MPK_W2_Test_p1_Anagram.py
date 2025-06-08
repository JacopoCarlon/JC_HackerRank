#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

## Anagram

def anagram(s):
    if len(s) % 2 == 1:
        return -1

    s1 = s[:int(len(s) / 2)]
    s2 = s[int(len(s) / 2):]
    unique_chars = list(set(s2))
    count = 0
    for c in unique_chars:
        count += max(s2.count(c) - s1.count(c), 0)
    return count



def diff_anagram(s):
    # Write your code here
    slen = len(s)
    if slen %2 == 1:
        return -1
        
    sset = set(s)
    sdic = {k:0 for k in sset}
    for e in s :
        sdic[e] += 1
    odds = 0
    for k, v in sdic:
        if v%2 == 1:
            odds += 1
    return odds
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
