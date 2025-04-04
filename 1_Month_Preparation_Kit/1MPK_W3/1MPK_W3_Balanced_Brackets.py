#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

## using replace (costly)
## each replace is O(n) on the whole (curr-existing) string
## worst case : Theta( 3n(n+2)/8) ~ or ... Theta(3n(n+4)/16) -> O(n^2)
def replace_isBalanced(s):
    # Write your code here
    siz = len(s)
    prevLen = siz
    
    for i in range(0, siz+3//2, 1):
        s = s.replace("()", "").replace("[]","").replace("{}","")
        if len(s) == prevLen and len(s) != 0:
            return "NO"
        
    if len(s) > 0:
        return "NO"
    else :
        return "YES"




## using memory ... max Theta(~n/2) 
## + very early stop is possible !!!
def isBalanced(s):
    stack = []
    ## idea : if a closed bracked appear (reading left to right), 
    ##          then it MUST be closing its opened bracket (that must be the last one readable !!!)
    
    open = [
    '{' ,
    '[' ,
    '(' 
    ]
    
    # prep 1:1 map of <open:closed> brackets !
    close = {
        '}':'{' ,
        ']':'[' ,
        ')':'('
    }
    
    for c in s:
        if c in open:
            ## if opening, just record stack of opened brackets
            stack.append(c)
        else:
            ## closing bracket
            if len(stack) > 0 and stack[-1] == close[c]:
                ## then the current is closing , and the last opened is matching , we can continue
                stack.pop()
            else:
                # got a close but no match, (or open stack empty -> no match ever possible)
                return 'NO'

    if len(stack) > 0:
        # some brackets opened but were not closed :
        return 'NO'
    else :
        # all was closed nicely
        return 'YES'



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()


