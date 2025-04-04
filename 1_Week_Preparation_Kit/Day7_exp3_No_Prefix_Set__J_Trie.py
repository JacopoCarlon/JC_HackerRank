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

class TrieNode:
    def __init__(self, value):
        self.value = value
        self.is_end = False
        # children are TrieNodes based on the chars that go from this node onwards
        self.children = {} 

class Trie:
    def __init__(self, value):
        self.root = TrieNode(value)

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
            if node.is_end:
                # a word that ends here already existed, 
                # "word" is a complete duplicate
                # insertion failed (meaning we didn't insert "word" because it was already there)
                return False
        if node.children:
            # we have arrived at the end of the "word"
            # but the word existed already, and continues somewhere
            # "word" is the prefix substring of something that was inserted before, 
            # insertion failed (meaning we didn't insert "word" because it was already there)
            return False
        # if we arrive here, 
        # then this is the first insertion of "word", that finishes here!
        node.is_end = True
        return True


def noPrefix(words):
    trie = Trie("")
    for s in words:
        if not trie.insert(s):
            print("BAD SET")
            print(s)
            return
    print("GOOD SET")
    return
    

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)
        
    noPrefix(words)
