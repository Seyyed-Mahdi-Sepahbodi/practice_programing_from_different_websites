#!/bin/python3

import math
import os
import random
import re
import sys

def aVeryBigSum(ar):
    result = 0
    for i in ar:
        result += i
    return result

if __name__ == '__main__':
    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    print(result)

"""
In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.
"""