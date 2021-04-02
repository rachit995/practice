#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.


def maximumToys(prices, k):
    prices.sort()
    index = 0
    while k > 0:
        k -= prices[index]
        index += 1
    return index - 1


if __name__ == '__main__':
    nk = "7 50".split()
    n = int(nk[0])
    k = int(nk[1])
    prices = list(map(int, "1 12 5 111 200 1000 10".split()))
    result = maximumToys(prices, k)
    print(result)
