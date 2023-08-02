#!/bin/python3

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    minimum = min(arr)
    maximum = max(arr)

    sum_max = sum(arr) - minimum
    sum_min = sum(arr) - maximum

    print(sum_min, sum_max)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)