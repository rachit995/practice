#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.


def twoStrings(s1, s2):
    for s in s2:
        if s in s1:
            return "YES"
    return "NO"


if __name__ == '__main__':
    s1 = "hello"
    s2 = "wrrdd"
    result = twoStrings(s1, s2)
    print(result)
