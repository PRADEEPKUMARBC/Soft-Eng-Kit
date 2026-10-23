#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'mergeHighDefinitionIntervals' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY intervals as parameter.
#

def mergeHighDefinitionIntervals(intervals):
    # Write your code here
    n = len(intervals)
    if not intervals or n == 0:
        return [[]]
    
    intervals.sort(key=lambda x: x[0])
    write = 0
    
    for i in range(1, n):
        if intervals[i][0] > intervals[write][1]:
            write += 1
            intervals[write] = intervals[i]
        else:
            intervals[write][1] = max(intervals[write][1],intervals[i][1])
            
    return intervals[:write+1]

if __name__ == '__main__':
    intervals_rows = int(input().strip())
    intervals_columns = int(input().strip())

    intervals = []

    for _ in range(intervals_rows):
        intervals.append(list(map(int, input().rstrip().split())))

    result = mergeHighDefinitionIntervals(intervals)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
