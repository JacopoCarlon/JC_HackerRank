#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    
    late = ( "P" == s[-2])
    
    tim = s[:-2].split(":")
    if late:
        ## we are PM
        if tim[0]=="12":
            # 12PM stays 12
            pass
        else :
            tim[0] = int(tim[0])+int(12)
    else:
        ## we are AM
        if tim[0]=="12":
            # 12AM -> 00
            tim[0] = "00"
            
    
    res = f'{tim[0]}:{tim[1]}:{tim[2]}'
    
    # print(f' res:{res} ; input:{s}')
            
    return res
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
