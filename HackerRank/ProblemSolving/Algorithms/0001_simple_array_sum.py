#!/bin/python3

import math
import random
import re
import sys

def simpleArraySum(ar):
    result = 0
    for i in ar:
        result += i
    return result

if __name__ == '__main__':

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    print(result)

"""
Given an array of integers, find the sum of its elements.
For example, if the array ar = [1, 2, 3], 1 + 2 + 3 = 6, so return6.
"""