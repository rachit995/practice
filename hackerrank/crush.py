#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.


def arrayManipulation(n, queries):
    arr = [0] * n
    for query in queries:
        for index in range(query[0] - 1, query[1]):
            arr[index] += query[2]
    return max(arr)


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
