#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.


def checkMagazine(magazine, note):
    flag_map = {}
    for magazine_word in magazine:
        if magazine_word not in flag_map:
            flag_map[magazine_word] = 0
        flag_map[magazine_word] += 1
    for note_word in note:
        if note_word in magazine and flag_map[note_word] > 0:
            flag_map[note_word] -= 1
        else:
            print("No")
            return
    print("Yes")


if __name__ == '__main__':
    magazine = "two times two and three is not four".split()

    note = "two times two is four".split()

    checkMagazine(magazine, note)
