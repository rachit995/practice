#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.


def countSwaps(a):
    n = len(a)
    num_swaps = 0
    for _ in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                num_swaps += 1
                a[j], a[j+1] = a[j+1], a[j]
    print("Array is sorted in "+str(num_swaps)+" swaps.")
    print("First Element: "+str(a[0]))
    print("Last Element: "+str(a[n-1]))


if __name__ == '__main__':
    a = [3, 2, 1]
    countSwaps(a)
