#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the isValid function below.


def isValid(s):
    count_hash = defaultdict(lambda: 0)
    freq_hash = defaultdict(lambda: 0)
    for char in s:
        count_hash[char] += 1
    count_values = list(count_hash.values())
    set_count_values = set(count_values)
    if len(set_count_values) == 1:
        return "YES"
    if count_values.count(1) > 1:
        return "NO"
    if len(set_count_values) == 2 and (list(set_count_values).count(1) == 1 or abs(set_count_values.pop() - set_count_values.pop()) == 1):
        for freq in count_hash.values():
            freq_hash[freq] += 1
        freq_values = list(freq_hash.values())
        if freq_values.count(1) == 1 and len(freq_values) == 2:
            return "YES"
    return "NO"


if __name__ == '__main__':
    s = "abccc"
    result = isValid(s)
    print(result)
