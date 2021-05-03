#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()
    minimum = abs(arr[0] - arr[1])
    for index in range(1, len(arr) - 1):
        if abs(arr[index] - arr[index+1]) < minimum:
            minimum = abs(arr[index] - arr[index+1])
    return minimum


if __name__ == '__main__':

    n = 10

    arr = list(map(int, "1 -3 71 68 17".split()))

    result = minimumAbsoluteDifference(arr)

    print(result)
