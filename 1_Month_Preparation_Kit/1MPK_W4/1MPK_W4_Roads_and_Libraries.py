#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

from collections import deque

def roadsAndLibraries(n, c_lib, c_road, cities):
    ## obv, if cost road > cost library, just build libraries
    if c_road >= c_lib:
        return n * c_lib
        
    ## otherwise, then we will build 1 library per connected block
    
    # Build adjacency matrix
    adj = [[] for _ in range(n+1)]
    for u, v in cities:
        adj[u].append(v)
        adj[v].append(u)
    visited = [False] * (n+1)
    total_cost = 0
    for city in range(1, n+1):
        ## BFS for connected community search:
        ## start with all cities not-visited, 
        ## -> keep expanding until all are visited 
        if not visited[city]:
            # BFS to find the size of the connected component
            queue = deque()
            queue.append(city)
            visited[city] = True
            component_size = 0
            while queue:
                current = queue.popleft()
                component_size += 1
                for neighbor in adj[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            # Calculate cost for this component
            total_cost += c_lib + (component_size - 1) * c_road
    return total_cost
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
