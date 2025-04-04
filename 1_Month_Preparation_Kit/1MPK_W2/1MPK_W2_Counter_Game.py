#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#

## 6    == 110      L-> 010 R-> 1:R        _ 1+1 = 2:R
## 132  == 10000100 L-> 100 R-> 10 L-> 1:L _ 1+2 = 3:L
## 4    == 100 L-> 10 R-> 1  _ 2+0=2:R  
## 7    == 111 L-> 11 R-> 1: _ 2+0=2:R

def counterGame(n):
    # Write your code here
    
    count = 0
    while n > 1:
        if n%2==0:
            count +=1
            n = n//2
        else : 
            break
    ## arrive here, 132 -> 66 -> 33 -> 100001 
    ## if i do 33%2->1 and 33//2-> even! so i count once as desired
    while n > 1:
        if n%2 == 1:
            count += 1
        n = n//2
    
    return "Richard" if count%2==0 else "Louise"
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
