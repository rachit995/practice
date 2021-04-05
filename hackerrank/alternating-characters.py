#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.


def alternatingCharacters(s):
    n = len(s)
    index = 0
    count = 0
    while index < n - 1:
        if s[index] == s[index + 1]:
            count += 1
        index += 1
    return count


if __name__ == '__main__':
    q = [
        "AAAA",
        "BBBBB",
        "ABABABAB",
        "BABABA",
        "AAABBB"
    ]
    for q_itr in q:
        result = alternatingCharacters(q_itr)
        print(result)
