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

# using trie structure solution
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

def noPrefix(words):
    root = TrieNode()
    ## concept : if a word passes through a is_end (finished word) than we found a prefix
    for word in words:
        current = root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            if current.is_end:
                print("BAD SET")
                print(word)
                return
        ## if you finished and there are more children, you are prefix
        ## else if there is another word ending here , identical words are prefix of each other
        if current.children or current.is_end:
            print("BAD SET")
            print(word)
            return
        current.is_end = True
    print("GOOD SET")
    

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
