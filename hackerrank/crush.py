#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.


def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    for query in queries:
        arr[query[0] - 1] += query[2]
        arr[query[1]] -= query[2]
    s_m = 0
    m = 0
    for e in arr:
        s_m += e
        m = max(m, s_m)
    return m


if __name__ == '__main__':
    nm = "5 3".split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    queries.append(list(map(int, "1 2 100".rstrip().split())))
    queries.append(list(map(int, "2 5 100".rstrip().split())))
    queries.append(list(map(int, "3 4 100".rstrip().split())))
    result = arrayManipulation(n, queries)
    print(result)
