#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.


def minimumBribes(q):
    n = len(q)
    steps = 0
    for index in range(n):
        step = q[index] - (index + 1)
        if step > 2:
            print('Too chaotic')
            return
    for index in range(n):
        for j in range(max(q[index] - 2, 0), index + 1):
            if q[j] > q[index]:
                steps += 1
    print(steps)


if __name__ == '__main__':
    q = [1, 2, 5, 3, 7, 8, 6, 4]
    minimumBribes(q)
