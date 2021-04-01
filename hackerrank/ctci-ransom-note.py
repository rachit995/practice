#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.


def checkMagazine(magazine, note):
    m = len(magazine)
    n = len(note)
    if n > m:
        print('No')
        return
    for note_word in note:
        if note_word not in magazine:
            print("No")
            return
        else:
            magazine.pop(magazine.index(note_word))
    print("Yes")


if __name__ == '__main__':
    magazine = "two times three is not four".split()

    note = "two times two is four".split()

    checkMagazine(magazine, note)
