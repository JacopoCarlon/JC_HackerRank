#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#


### .2. ...
### .1. ...

### .2. ...
### 12. ...

### 2.1 ...
### 1.2 ...

## .1 means will be placed 0 next turn
## .3 means left just exploded, should remain .1
## .3 means above just exploded, should remain .1


                

# Write your code here
# it is a deterministic pattern evolution
## -0- > -1- > 020 > --- > 000 > 111 > 222 > --- > 000 > 111 > 222 > --- > 000
##  0     1     2     3     4     5     6     7
## 8 ? -> 8-3-> 5 ... 5%4 = 1

## 0 > 1 > 2 > - > 0 > 1 > 2 > - > 0
## 0   1   2   3   4
## 8 ? 8-0-> 8 ... 8%4 = 0

## !!!!!! bombs are placed by me with period 2 , i can do that on parity check
### appearance of the board changes only every
    

## this is an optimized solution, based on noticing that the cycles ALWAYS have period of 4 !!!
def bomberMan(n, grid):
    if n == 1:
        return grid
    
    # After n=1, if n is even, the grid is completely filled with bombs
    if n % 2 == 0:
        return ['O' * len(grid[0]) for _ in range(len(grid))]
    
    # We only need to calculate for n=3, n=5, n=7, ...
    # And there's a cycle: state after n=3 and state after n=7 are the same,
    # state after n=5 and state after n=9 are the same
    
    # Convert initial grid to a more efficient format (2D array)
    r, c = len(grid), len(grid[0])
    initial_grid = [['O' if cell == 'O' else '.' for cell in row] for row in grid]
    
    # Calculate the state after 3 seconds (place bombs everywhere, then detonate)
    state_3 = simulate_explosion(initial_grid, r, c)
    
    # If n=3, return this state
    if n % 4 == 3:
        return [''.join(row) for row in state_3]
    
    # Calculate the state after 5 seconds (place bombs everywhere, then detonate)
    state_5 = simulate_explosion(state_3, r, c)
    
    # Return the appropriate state (n=5, n=9, n=13, ...)
    ## notice how odd 
    
    return [''.join(row) for row in state_5]
    
def simulate_explosion(grid, r, c):
    # Create a new grid filled with bombs
    new_grid = [['O' for _ in range(c)] for _ in range(r)]
    
    # Process explosions
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'O':  # If there was a bomb, it explodes
                new_grid[i][j] = '.'
                if i > 0:
                    new_grid[i-1][j] = '.'
                if i < r-1:
                    new_grid[i+1][j] = '.'
                if j > 0:
                    new_grid[i][j-1] = '.'
                if j < c-1:
                    new_grid[i][j+1] = '.'
    
    return new_grid
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
