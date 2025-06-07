#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#



def highestValuePalindrome(s, n, k):
    s = list(s)
    changes_needed = 0
    latest_change = -1
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            changes_needed += 1
            latest_change = i
    if changes_needed > k:
        return "-1"
    
    remaining_changes = k - changes_needed
    for i in range(n // 2):
        if i > latest_change and remaining_changes < 2:
            break  # No more changes needed or possible
        left = s[i]
        right = s[n - 1 - i]
        if i<= latest_change :
            if left != right:
                ## then we need to at the least change 1 of them 2 to make the palindrome
                if remaining_changes >=  1 and (left != '9' and right != '9'):
                    # maximize palindrome : change 1 more than needed for palindromicy
                    # Set both to 9
                    s[i] = '9'
                    s[n - 1 - i] = '9'
                    remaining_changes -= 1
                else:
                    # Set to the max of the two (just execute the needed)
                    max_char = max(left, right)
                    s[i] = max_char
                    s[n - 1 - i] = max_char
                    # remaining_changes -= 0
                changes_needed -= 1
            else:
                if left != '9' and remaining_changes >= 2:
                    # Set both to 9
                    s[i] = '9'
                    s[n - 1 - i] = '9'
                    remaining_changes -= 2
        else :
            # now the left and right values are equal (i> latest_change)
            # so we just maximize both, making the earliest (this i) to 9
            if left != '9' and remaining_changes >= 2:
                # Set both to 9
                s[i] = '9'
                s[n - 1 - i] = '9'
                remaining_changes -= 2
    # Handle the middle character
    if n % 2 == 1 and remaining_changes > 0:
        s[n // 2] = '9'
    
    return ''.join(s)





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
