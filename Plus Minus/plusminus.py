#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    length = len(arr)
    positive, negative, zero = 0,0,0
    for i in range(0, length):
        if arr[i] > 0:
            positive += 1
        elif arr[i] < 0:
            negative  +=1 
        else:
            zero += 1
            
    print (positive/length)
    print (negative/length)
    print (zero/length)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)