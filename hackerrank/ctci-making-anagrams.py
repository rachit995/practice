#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the makeAnagram function below.


def makeAnagram(a, b):
    count = 0
    freq_a = defaultdict(lambda: 0)
    freq_b = defaultdict(lambda: 0)
    for s in a:
        freq_a[s] += 1
    for s in b:
        freq_b[s] += 1
    checked_s = []
    for s in freq_a:
        if s in freq_b:
            count += abs(freq_a[s] - freq_b[s])
        else:
            count += abs(freq_a[s])
        checked_s.append(s)
    for s in freq_b:
        if s in freq_a:
            if s not in checked_s:
                count += abs(freq_a[s] - freq_b[s])
        else:
            count += abs(freq_b[s])
    return count


if __name__ == '__main__':
    a = "bacdc"
    b = "dcbad"
    res = makeAnagram(a, b)
    print(res)
