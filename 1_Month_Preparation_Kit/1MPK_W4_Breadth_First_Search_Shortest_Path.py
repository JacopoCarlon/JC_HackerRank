#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#


## Breadth First Search Shortest Path : Breadth_First_Search_Shortest_Path

from collections import deque

def bfs(n, m, edges, s):
    # Write your code here
    # Build adjacency list -> use sets for O(1) lookups and duplicate prevention
    adj = [set() for _ in range(n+1)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    
    # Initialize distances array with -1 (unvisited)
    distances = [-1] * (n+1)
    distances[s] = 0
    
    # Use deque for efficient queue operations : popleft/append
    q = deque([s])
    
    # Track remaining unvisited nodes for early termination
    remaining = n - 1
    
    while q and remaining > 0:
        current = q.popleft()
        for neighbor in adj[current]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current] + 6
                q.append(neighbor)
                remaining -= 1
                if remaining == 0:
                    break
    
    # Generate result directly without temporary list
    return (distances[i] for i in range(1, n+1) if i != s)
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
