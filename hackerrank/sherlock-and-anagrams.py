#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.


def sherlockAndAnagrams(s):
    hash_map = {}
    for st in s:
        if st not in hash_map:
            hash_map[st] = 0
        hash_map[st] += 1
    print(hash_map)
    return 0


if __name__ == '__main__':
    s = "abba"
    result = sherlockAndAnagrams(s)
    print(result)
