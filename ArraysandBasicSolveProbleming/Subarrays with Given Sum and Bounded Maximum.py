#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'countSubarraysWithSumAndMaxAtMost' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. LONG_INTEGER k
#  3. LONG_INTEGER M
#

def countSubarraysWithSumAndMaxAtMost(nums, k, M):
    # Write your code here
    count = 0
    prefix = 0
    freq = {0:1}
    for num in nums:
        if num > M:
            prefix = 0
            freq = {0:1}
            continue
            
        prefix += num
        count += freq.get(prefix - k, 0)
        freq[prefix] = freq.get(prefix, 0) + 1
    return count

if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    k = int(input().strip())

    M = int(input().strip())

    result = countSubarraysWithSumAndMaxAtMost(nums, k, M)

    print(result)
