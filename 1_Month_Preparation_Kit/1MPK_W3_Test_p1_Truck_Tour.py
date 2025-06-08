#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#



## Truck Tour : Truck_Tour

# O(n) time, O(1) space
# under the assumption that it will always find at the least 1 existing solution
# then we find the fastest one
def truckTour(petrolpumps):
    plen = len(petrolpumps)
    start = 0
    total_sum = 0
    current_sum = 0
    
    for i in range(plen):
        petrol, distance = petrolpumps[i]
        diff = petrol - distance
        current_sum += diff
        total_sum += diff
        if current_sum < 0:
            start = i + 1
            current_sum = 0
    
    return start

# O(n^2)
def n2_truckTour(petrolpumps):
    # Write your code here
    plen = len(petrolpumps)
    
    leftovers = [x - y for x, y in petrolpumps]
    
    for i in range(plen):
        sm = 0
        for j in range(plen):
            sm += leftovers[(i + j) % plen]
            if sm < 0:
                break
        else:
            return i
    return -1
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + '\n')

    fptr.close()
