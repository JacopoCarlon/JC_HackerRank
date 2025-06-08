#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#


## Components in a Graph : Components_in_a_Graph

def componentsInGraph(gb):
    # Write your code here
    parent = {}
    size = {}
    
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    
    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        if u_root == v_root:
            return
        if size[u_root] < size[v_root]:
            u_root, v_root = v_root, u_root
        ## now v_root is the one with smallest size, 
        ## and we append it to u_block , thus keeping the tree smaller
        parent[v_root] = u_root
        size[u_root] += size[v_root]
       
    for edge in gb:
        u, v = edge
        if u not in parent:
            parent[u] = u
            size[u] = 1
        if v not in parent:
            parent[v] = v
            size[v] = 1
        union(u, v)
    
    roots = set()
    for node in parent:
        roots.add(find(node))
    
    component_sizes = [size[root] for root in roots]
    smallest = min(component_sizes)
    largest = max(component_sizes)
    
    # According to the problem statement, the answer should exclude isolated nodes if any
    # ... but since all nodes are part of edges, all nodes are in some component
    return (smallest, largest)
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
