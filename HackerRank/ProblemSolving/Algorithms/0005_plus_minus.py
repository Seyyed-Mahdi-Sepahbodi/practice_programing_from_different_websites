#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):

    number_of_elements = len(arr)
    number_of_positive_elements = 0
    number_of_negetive_elements = 0
    number_of_zeros = 0

    for i in arr:
        if i == 0:
            number_of_zeros += 1
        elif i < 0:
            number_of_negetive_elements += 1
        else:
            number_of_positive_elements += 1

    print("{:.6f}\n{:.6f}\n{:.6f}".format((number_of_positive_elements / number_of_elements), (number_of_negetive_elements / number_of_elements), (number_of_zeros / number_of_elements)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.
"""