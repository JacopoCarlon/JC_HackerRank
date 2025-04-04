#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    # Write your code here
    goodst = "GOOD SET"
    badst = "BAD SET"
    
    from collections import deque
    que = deque(sorted(words))
    
    # print(f'input:{words}, sorted:{sorted(words)}')
    
    hits = []
    
    short = que.popleft()
    for i in range(1, len(words)):
        trg = que.popleft()
        if len(short) <= len(trg) :
            if short == trg[:len(short)]:
                #print(f'{badst}\n{trg}')
                #return
                hits.append(trg)
        ## else, iterate
        short=trg
        if que == None :
            break
    
    if hits == [] :
        print(f'{goodst}')
    
    print(f'{badst}')
    for i in words:
        if i in hits : 
            print(i)
            return
    
    return
    

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)
        
    noPrefix(words)
