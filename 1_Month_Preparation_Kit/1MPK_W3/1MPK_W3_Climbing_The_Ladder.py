#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    clrank = sorted(set(ranked), reverse=False)
    ##print(clrank) ## ascending
    
    rsiz = len(clrank)
    start = 0
    posList = []
    for pscore in player:
        ##print(f'doing {pscore}')
        if pscore > clrank[-1]:
            posList.append(1)
        else : 
            for j in range(start, rsiz):
                print(f' doing {pscore} against {clrank[j]}')
                if pscore < clrank[j]:
                    start = j
                    posList.append( (rsiz-j)+1)
                    break
                elif pscore == clrank[j] :
                    posList.append( (rsiz-j))
                    break

    return posList



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
