#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def basic_matchingStrings(strings, queries):
    # Write your code here
    
    mydict = {}
    for i in strings:
        if i in mydict.keys() :
            mydict[i] += 1
        else :
            # add to dict
            mydict[i] = 1
    
    mykeys = mydict.keys()
    res = []
    for j in queries:
        if j in mykeys:
            res.append(mydict[j])
        else :
            res.append(0)
    return res
    
    
def matchingStrings(strings, queries):
    counts = {}
    for s in strings:
        counts[s] = counts.get(s, 0) + 1
    return [counts.get(q, 0) for q in queries]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
