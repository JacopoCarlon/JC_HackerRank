#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def count_swaps(arr, target):
    pos = {val: idx for idx, val in enumerate(arr)}
    swaps = 0
    for i in range(len(arr)):
        if arr[i] != target[i]:
            swaps += 1
            # Get the value that should be at this position in the target
            correct_val = target[i]
            # Find the current position of this correct value in the original array
            original_pos = pos[correct_val]
            # Swap the values in the original array
            arr[i], arr[original_pos] = arr[original_pos], arr[i]
            # Update their positions in the pos dictionary
            pos[arr[original_pos]] = original_pos
            pos[arr[i]] = i
    return swaps

def lilysHomework(arr):
    # Create a copy of the original array to avoid modifying it directly
    arr_copy = arr.copy()
    # Sorted array for ascending and descending order
    sorted_asc = sorted(arr)
    sorted_desc = sorted(arr, reverse=True)
    # Calculate swaps for both orders
    swaps_asc = count_swaps(arr_copy.copy(), sorted_asc)
    swaps_desc = count_swaps(arr_copy.copy(), sorted_desc)
    # Return the minimum of the two
    return min(swaps_asc, swaps_desc)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
