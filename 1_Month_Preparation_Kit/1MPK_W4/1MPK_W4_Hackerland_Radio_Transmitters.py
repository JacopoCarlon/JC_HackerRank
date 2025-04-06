#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

## say range 2 :
## .#--#--#--# -> 4 needed
## .########## -> 2 needed
## .#-######-# -> 2 needed
## .#-#####-## -> 3 needed



def hackerlandRadioTransmitters(x, k):
    
    ## array needs to be sorted for the while to be linear
    ## O(nlogn)
    x.sort()
    siz = len(x)
    
    irun = 0
    transmitters = 0
    ## In this case we need just the count, so we can keep space O(1) instead of O(n) by not listing the lamps
    ###lampList = []
    
    ## the while and its nested whiles keep the same iterator, so it's a single while with ifs !
    ## O(n)
    while irun < siz:
        # Address of the current house
        thisAddr = x[irun]
        
        # Place a transmitter at the rightmost house within k units of the current house
        furthes_acceptable_lamp = thisAddr + k
        while irun < siz and x[irun] <= furthes_acceptable_lamp:
            irun += 1
        ## while exits when lamp is too far, just use the previous one ... !
        
        # Position of the transmitter
        transmitter_pos = x[irun-1]
        transmitters += 1
        ###lampList.append(transmitter_pos)
        
        # Skip all houses covered by the transmitter
        end_of_coverage = transmitter_pos + k
        while irun < siz and x[irun] <= end_of_coverage:
            irun += 1
    
    ###print(f'addresses:{x}, lampList:{lampList}')
    ###return len(lampList)
    
    
    ## solution _ time:O(nlogn), space:O(1)
    return transmitters
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
