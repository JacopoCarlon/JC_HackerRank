#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#


## Cut the Tree : Cut_the_Tree

# Depth First Search DFS
def cutTheTree(data, edges):
    # Write your code here
    n = len(data)
    adjacency = [[] for _ in range(n+1)]  # 1-based indexing
    
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    
    total_sum = sum(data)
    min_diff = float('inf')
    
    # Determine if perfect split is possible : for evens is 0, for odds is 1
    ## ## target_diff = 0 if total_sum % 2 == 0 else 1
    target_diff = total_sum % 2 
        
    parent = [0] * (n + 1)
    subtree_sums = [0] * (n + 1)
    
    stack = [(1, False)]  # (node, processed)
    
    ## DFS starting from node 1 
    ## (from note : the given tree is always rooted at vertex 1)
    while stack:
        node, processed = stack.pop()
        if not processed:
            stack.append((node, True))
            # Push children in reverse order
            for neighbor in reversed(adjacency[node]):
                if neighbor != parent[node]:
                    parent[neighbor] = node
                    stack.append((neighbor, False))
        else:
            subtree_sum = data[node-1]  # node is 1-based, data is 0-based
            for child in adjacency[node]:
                if child != parent[node]:
                    subtree_sum += subtree_sums[child]
            subtree_sums[node] = subtree_sum
            
            if node != 1:  # No edge to cut above root
                current_diff = abs(total_sum - 2 * subtree_sum)
                if current_diff == target_diff:
                    return current_diff  # Early exit if target found
                if current_diff < min_diff:
                    min_diff = current_diff
    
    return min_diff











if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()
