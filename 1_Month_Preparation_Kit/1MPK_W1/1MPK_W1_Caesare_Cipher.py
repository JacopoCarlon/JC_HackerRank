#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

## good
def good_caesarCipher(s, k):
    # Write your code here
    alph = "abcdefghijklmnopqrstuvwxyz"
    salf = len(alph)
    myShift = { alph[i] : alph[(i+k)%salf] for i in range(salf)  }
    
    # this is for better execution in for loop (alphabeth has limited lenght anyways)
    upalph = alph.upper()
    myUpperShift ={ upalph[i] : upalph[(i+k)%salf] for i in range(salf)  }
    
    print(f'key{k} , myShift : {myShift} .')
    res = ""
    for char in s : 
        if char in alph :
            ## lowercase
            res += myShift[char]
        elif char in upalph:
            ## uppercase
            res += myUpperShift[char]
        else :
            res += char
    
    return res

## very_good
def very_good_caesarCipher(s, k):
    # Write your code here
    alph = "abcdefghijklmnopqrstuvwxyz"
    salf = len(alph)
    myShift = { alph[i] : alph[(i+k)%salf] for i in range(salf)  }
    
    # this is for better execution in for loop (alphabeth has limited lenght anyways)
    upalph = alph.upper()
    myUpperShift ={ upalph[i] : upalph[(i+k)%salf] for i in range(salf)  }
    
    print(f'key{k} , myShift : {myShift} .')
    res = ""
    for char in s : 
        res += myShift.get(char, myUpperShift.get(char, char))
    return res
    

# perfect
def caesarCipher(s, k):
    alph = "abcdefghijklmnopqrstuvwxyz"
    salf = len(alph)
    k = k % salf  # Ensure shift is within the alphabet length
    myShift = {alph[i]: alph[(i + k) % salf] for i in range(salf)}
    upalph = alph.upper()
    myUpperShift = {upalph[i]: upalph[(i + k) % salf] for i in range(salf)}
    return ''.join(map(lambda res: myShift.get(res, myUpperShift.get(res, res)), s))
    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
