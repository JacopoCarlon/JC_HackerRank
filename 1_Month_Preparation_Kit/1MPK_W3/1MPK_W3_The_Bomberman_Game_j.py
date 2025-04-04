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

def update(grid, nrows, ncols):
    for i in range(nrows):
        for j in range(ncols):
            thisVal = grid[i][j]
            if thisVal == ".":
                grid[i][j] = ".1"
            if thisVal == "O":
                grid[i][j] = "1"
            elif thisVal == "1":
                grid[i][j] = "2"
            elif thisVal == ".1":
                grid[i][j] = "O"           
            elif thisVal == ".3":
                grid[i][j] = ".1"           
            elif thisVal == "2":
                grid[i][j] = ".1"
                if i>0:
                    ## explode above ?
                    grid[i-1][j] = ".1"
                if i < nrows-1 :
                    ## exblode below ?
                    if grid[i+1][j] != "2":
                        grid[i+1][j] = ".3"
                if j>0:
                    ## explode on left
                    grid[i][j-1] = ".1"
                if j<ncols-1:
                    ## explode on right ?
                    if grid[i][j+1] != "2":
                        grid[i][j+1] = ".3"
                    
                

def bomberMan(n, basegrid):
    # Write your code here
    # it is a deterministic pattern evolution
    ## -0- > -1- > 020 > --- > 000 > 111 > 222 > --- > 000 > 111 > 222 > --- > 000
    ##  0     1     2     3     4     5     6     7
    ## 8 ? -> 8-3-> 5 ... 5%4 = 1
    
    ## 0 > 1 > 2 > - > 0 > 1 > 2 > - > 0
    ## 0   1   2   3   4
    ## 8 ? 8-0-> 8 ... 8%4 = 0
    grid = [list(s) for s in basegrid]
    
    if grid == [[]]:
        return grid
    
    nrows = len(grid)
    ncols = len(grid[0])
    
    mydict = {}
    
    counter = 0
    loopLen = 0
    loopStart = 0
        
    while counter < n :
        stringed = repr(grid)
        ## print(f'grid at counter=={counter} , : {stringed} ')
        if stringed in mydict.keys() :
            ## found a loop
            loopStart = mydict[stringed]
            loopLen = counter - loopStart
            break
        
        mydict[stringed] = counter
        
        ## increments : 
        update(grid, nrows, ncols)
        counter += 1
    
    if counter == n:
        # we found no cycle, but we calculated everything
        
        res = compressForRet(grid)
        ##print(f'result : \n{res}')
        return res
        
    resPos = n - loopStart
    resPos = resPos%loopLen
    resGrids = [key for key, val in mydict.items() if val == resPos]
    resTrg = eval(resGrids[0])
    
    res = compressForRet(resTrg)
    
    ##print(f'result : \n {res} ')
    
    return 
    
    

def compressForRet(grid):
    res = []
    for i in range(len(grid)):
        parsol = ""
        for j in range(len(grid[i])):
            val = "." if grid[i][j] == "." or grid[i][j] == ".1" or grid[i][j] == ".3" else "O"
            parsol += val
        res.append(parsol)
    return res
    

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
