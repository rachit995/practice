#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.


def minimumSwaps(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        while(arr[i] != i + 1):
            count += 1
            temp = arr[i]
            arr[i], arr[temp - 1] = arr[temp - 1], arr[i]
    return count


if __name__ == '__main__':
    n = 5
    arr = [2, 3, 4, 1, 5]
    res = minimumSwaps(arr)
    print(str(res) + '\n')
