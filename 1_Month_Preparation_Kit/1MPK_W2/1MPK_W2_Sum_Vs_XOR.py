#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

## given long int n

## find 1<=x<n s.t. n+x == n^x
## (n+x)^x == n or (n+x)^n == x 
## 3:11 -> 3+0==3==3^0 ; 3+1==4!=3^1 ; 3+2==5!=3^2; -> 3 only "0" works -> 1sol
## 4:100 -> "0","1","2","3" == 2**2 -> 4 sol 
## 5:101 -> 0ok, 2ok
## 6:110 -> 0ok, 1ok,  
## 7:111 -> 0ok, 
## 10:1010 -> 0000, 100, 1, 101

## !!! need to count the zeroes

## this solution is too slow only on test case 1
def tooSlow_sumXor(n):
    zero_bits = 0
    while (n != 1):
        if (n & 1 == 0):
            zero_bits += 1           
        n >>= 1
    return 1 << zero_bits  
   
## using bin(n) and count('0') is faster because it's written in C
def sumXor(n):
    if n <2 :
        return 1
    else:
        # Ignore the '0b' prefix
        zero_bits = bin(n)[2:].count('0')  
        return 1 << zero_bits  
    
        
def fact(n):
    return bifact(n, 1)

def bifact(n, x):
    if n==1:
        return x
    return (n-1, x*n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
