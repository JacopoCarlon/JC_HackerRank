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
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
            if node.word:
                return False
        if node.children:
            return False
        node.word = True
        return True

def noPrefix(words):
    trie = Trie()
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
