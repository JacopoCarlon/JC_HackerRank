#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#   

## Palindrome Index : Palindrome_Index
    
def palindrome(s):
    if s==s[::-1]:
        return True
    else:
        return False
        
def palindromeIndex(s):
    if s==s[::-1]:
        return -1
    else:
        for i in range(len(s)//2):
            a=i
            b=len(s)-i-1
            if s[a]!=s[b]:
                ns=s[:a]+s[a+1:]
                ns2=s[:b]+s[b+1:]
                if palindrome(ns):
                    return a
                if palindrome(ns2):
                    return b
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
