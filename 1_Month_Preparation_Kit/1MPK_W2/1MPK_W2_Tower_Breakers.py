#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

## all towers height 1 -> 2 wins

## 1 tower h>1 -> 1 wins

## odd num of towers : 
## 222 -> 122 -> 112 -> 111 -> 1w
## 444 -> 144 -> 124 -> 122 -> 112 -> 111 -> 1w
##            -> 114 -> 111 -> 1w
## 888 -> 188 -> 148 -> 144 -> 124 -> 122 -> 112 -> 111 -> 1w
##            -> 128 -> 122 -> 112 -> 111 -> 1w
##            -> 118 -> 111 -> 1w

## even num of towers : 
## 22 -> 12 -> 11 -> 2w
## 44 -> 14 -> 11 -> 2w
##    -> 24 -> 22 -> 12 -> 11 -> 2w
## 88 -> 18 -> 11 -> w2
##    -> 28 -> 22 -> 12 -> 11 -> 2w
##    -> 48 -> 44 -> 14 -> 11 -> 2w
##                -> 24 -> 22 -> 12 -> 11 -> 2w


def towerBreakers(n, m):
    # Write your code here
    if m==1 :
        return 2
    if n == 1 : 
        return 1
    if n%2 == 1 :
        return 1
    else :
        return 2
    
    
# this is suboptimal :
def recursiveTowerBearkers(n,m) : 
    # only moves are cut in 2^m or pass !!!
    if n%2 == 0 and m%2 == 0:
        towerBreakers(n//2, m//2)
    if n%2 == 0 or m==1  :
        return 2
    return 1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
