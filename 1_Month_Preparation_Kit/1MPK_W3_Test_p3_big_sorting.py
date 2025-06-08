#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

## Big Sorting : Big_Sorting

def bigSorting(unsorted):
    # Write your code here
    
    # longest numbers are bigger than shorter ones (they are all positive > 1)
    # after that, sort also does comparison on string lexicographically, so '1' < '2' ...
    
    unsorted.sort(key=lambda x: (len(x), x))
    return unsorted












if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
