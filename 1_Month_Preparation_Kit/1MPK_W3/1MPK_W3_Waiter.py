#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#

def get_primes(q):
    ##topv = math.ceil(math.sqrt(q)+1)
    num_to_find = q
    primesFound = [2]
    itp = 3
    num_found = 1
    ##while itp < topv:
    while num_found < num_to_find :
        isPrime = True
        for j in primesFound:
            if itp % j == 0:
                isPrime = False
        if isPrime :
            num_found += 1
            primesFound.append(itp)
        itp += 2
    return primesFound


def waiter(number, q):
    # Write your code here
    
    answers = [] 
    usefulPrimes = get_primes(q)
    print(f'primes up to {q} : {usefulPrimes}')

    tmp = [] 
    for i in range(q):
        ## curr numbers is A0
        print(f'number:{number}')
        
        tmp = []
        for j in number:
            if j % usefulPrimes[i] == 0:
                ## append B1 to answers
                answers.append(j)
            else :
                ## populate A1
                tmp.append(j)
        print(f'tmp:{tmp}')
        number = tmp[::-1]
        
    answers.extend(number[::-1])
    print(f'res : {answers}')
    return answers
    
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
