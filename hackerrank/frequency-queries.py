#!/bin/python3

import math
import os
import random
import re
import sys
from typing import Hashable

# Complete the freqQuery function below.


def freqQuery(queries):
    hash_map = {}
    result = []
    freq_count = {}
    for q in queries:
        op = q[0]
        val = q[1]
        if op == 3:
            if val in freq_count and freq_count[val] > 0:
                result.append(1)
            else:
                result.append(0)
        else:
            next_val = -1
            prev_val = -1
            if op == 1:
                if val not in hash_map:
                    hash_map[val] = 0
                prev_val = hash_map[val]
                hash_map[val] += 1
                next_val = hash_map[val]
            elif op == 2 and val in hash_map:
                prev_val = hash_map[val]
                hash_map[val] -= 1
                next_val = hash_map[val]
                if hash_map[val] < 1:
                    del hash_map[val]
            if next_val not in freq_count:
                freq_count[next_val] = 0
            if prev_val not in freq_count:
                freq_count[prev_val] = 0
            freq_count[prev_val] -= 1
            freq_count[next_val] += 1
    return result


if __name__ == '__main__':
    q = int("10".strip())
    queries = []
    queries.append(list(map(int, "1 3".rstrip().split())))
    queries.append(list(map(int, "2 3".rstrip().split())))
    queries.append(list(map(int, "3 2".rstrip().split())))
    queries.append(list(map(int, "1 4".rstrip().split())))
    queries.append(list(map(int, "1 5".rstrip().split())))
    queries.append(list(map(int, "1 5".rstrip().split())))
    queries.append(list(map(int, "1 4".rstrip().split())))
    queries.append(list(map(int, "3 2".rstrip().split())))
    queries.append(list(map(int, "2 4".rstrip().split())))
    queries.append(list(map(int, "3 2".rstrip().split())))

    ans = freqQuery(queries)
    print(ans)
