#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    
    import string

    alphLen = len(string.ascii_lowercase)
    arcount = [0] * alphLen

    for char in s :
        if char in string.ascii_lowercase :
            arcount[string.ascii_lowercase.index(char)] = 1  
        elif char in string.ascii_uppercase :
            arcount[string.ascii_uppercase.index(char)] = 1
            
        arsum = sum(arcount)
        if arsum == alphLen:
            return "pangram"
    
    return "not pangram"
            
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
