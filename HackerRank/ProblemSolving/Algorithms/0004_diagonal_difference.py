#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):

    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0

    for i in range(n):
        for j in range(n):
            if i == j:
                primary_diagonal_sum += arr[i][j]
            elif i + j == n - 1:
                secondary_diagonal_sum += arr[i][j]

    if n % 2 != 0:
        secondary_diagonal_sum += arr[int(n / 2)][int(n / 2)]

    return abs(primary_diagonal_sum - secondary_diagonal_sum)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)

"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals. 
"""

