#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def dict_icecreamParlor(m, arr):
    # Write your code here
    mydict = {}
    siz = len(arr)
    for i in range(0, siz) : 
        trg = arr[i]
        if trg not in mydict :
            mydict[trg] = [i]
        else :
            mydict[trg].append(i)
    
    for i in range(len(arr)):
        price1 = arr[i]
        price2 = m - price1
        if price1 == price2:
            # If we need two ice creams of the same price
            if len(mydict[price1]) > 1:
                # Take the first two indices and sort them
                indices = sorted(mydict[price1][:2])
                return [indices[0] + 1, indices[1] + 1]
        elif price2 in mydict:
            # Return the indices in ascending order
            indices = sorted([i, mydict[price2][0]])
            return [indices[0] + 1, indices[1] + 1]
    
    return None
    




## O(n^2)
def bruteForce_icecreamParlor(m, arr):
    siz = len(arr)
    
    ## just iterate over what arrives in that order, and find a match
    for iter1 in range(0, siz):
        for iter2 in range(iter1 + 1, siz):
            if arr[iter1] + arr[iter2] == m :
                return ([ iter1 + 1, iter2 + 1])    


## O(n^2), but better
def cheap_icecreamParlor(m, arr):
    ## remove too pricy elements, but keep memory of their original position !
    siz = len(arr)
    gArr = [(arr[i],i) for i in range(siz) if arr[i] <=m ]
    
    ## just iterate over what arrives in that order, and find a match
    gSize = len(gArr)
    for iter1 in range(0, gSize):
        for iter2 in range(iter1 + 1, gSize):
            if gArr[iter1][0] + gArr[iter2][0] == m :
                return ([ gArr[iter1][1] + 1, gArr[iter2][1] + 1])    



### !!! O(n) + high_price_skip 
def icecreamParlor(m, arr):
    price_map = {}
    
    # Iterate through the array
    for i in range(len(arr)):
        current_price = arr[i]
        
        ## work under the hypothesis that prices cannot be negative !
        if current_price > m : 
            continue
            
        missing = m - current_price
        
        # Do we have already registered any price==missing -> that would be solution !
        if missing in price_map:
            return [price_map[missing] + 1, i + 1]
        
        ## note that if curPrice == m/2 we record it once, and if it appeares again, 
        ## we catch it in the if_missing above !!!
        
        # Store the current price and its index
        price_map[current_price] = i
          
    return None











if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
