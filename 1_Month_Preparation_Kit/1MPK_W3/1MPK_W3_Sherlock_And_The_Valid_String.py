#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    ## n == size
    siz = len(s)
    if siz <= 3:
        print("fast")
        return "YES"
    
    ## O(n) Theta(n)
    mset = set(s)
    cdict = {}
    ## O(n) Theta(k)
    for ch in mset:
        cdict[ch] = 0
    
    ## O(n) Theta(n)
    for c in s :
        cdict[c] += 1

    v0 = cdict[s[0]]
    print(f'v0:{v0}')
    excount = 0
    ## O(n) Theta(k)
    for key, val in cdict.items() : 
        print(f'key{key}, val{val}')
        if val == v0 : 
            pass
        if val - v0 != 0:
            excount += 1
            if excount > 1 :
                return "NO"
    return "YES"
    
    ## total : O(n)
    ## best :   T(n) = 2n + 2k
    ## worst :  T(n) = 2n + 2k




### this is a better way to populate the set if the string is very long and *has been randomized*
def needRND_isValid(s):
    # Write your code here
    ## n == size
    siz = len(s)
    if siz <= 3:
        print("fast")
        return "YES"
    
    ## O(n)
    pos = 0
    cdict = {}
    import string
    lenAlph = len(string.ascii_lowercase)
    
    mset = set()
    ref = 10000 // lenAlph
    if siz > ref : 
        while pos < siz :
            ## T(n) = 2*k -> 2*n
            mset.add(s[pos])
            if len(mset) == lenAlph:
                break
    else : 
        ## T(n) = n
        mset = set(s)
    
    ## size of set be k <= n
    ## T(n) = k
    for ch in mset:
        cdict[ch] = 0
        
    ## T(n) = n
    for c in s :
        cdict[c] += 1

    v0 = cdict[s[0]]
    print(f'v0:{v0}')
    excount = 0
    ## T(n) = k
    for key, val in cdict.items() : 
        print(f'key{key}, val{val}')
        if val == v0 : 
            pass
        if val - v0 != 0:
            excount += 1
            if excount > 1 :
                return "NO"
    return "YES"
    
    ## total O(n)
    ## best :   T(n) = n + 2k + 2*k*c0 + c1, c0 st k*c0 <= n
    ## worst :  T(n) = 3n + 2k + c1





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
