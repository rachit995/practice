#!/bin/python3

from collections import defaultdict
import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.


def find_median(count_array, median_index, d):
    count = 0
    index = 0
    if d % 2 == 0:
        left_index = 0
        right_index = 0
        while count < median_index:
            count += count_array[left_index]
            left_index += 1
        count = 0
        while count < median_index + 1:
            count += count_array[right_index]
            right_index += 1
        return left_index + right_index - 2
    else:
        while count < median_index:
            count += count_array[index]
            index += 1
        return 2 * (index - 1)


def activityNotifications(expenditure, d):
    notifications = 0
    count_array = [0] * 201
    median_index = 0
    expenditure_len = len(expenditure)
    if (d % 2 == 0):
        median_index = int(d / 2)
    else:
        median_index = int(d / 2) + 1
    for e in expenditure[:d]:
        count_array[e] += 1
    for exp_index in range(d, expenditure_len):
        med = find_median(count_array, median_index, d)
        if expenditure[exp_index] >= med:
            notifications += 1
        count_array[expenditure[exp_index]] += 1
        count_array[expenditure[exp_index - d]] -= 1
    return notifications


if __name__ == '__main__':
    nd = "5 3".split()
    n = int(nd[0])
    d = int(nd[1])
    expenditure = list(map(int, "10 20 30 40 50".rstrip().split()))
    result = activityNotifications(expenditure, d)
    print(result)
