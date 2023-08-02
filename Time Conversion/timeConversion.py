#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    time_code = re.search(r"(AM|PM)$", s)
    
    if time_code:
        #extract the matched time code (AM or PM)
        time_code = time_code.group()
        if time_code == "AM" and s[:2] == "12":
            return "00" + s[2:-2]
        elif time_code == "AM":
            return s[:-2]
        elif time_code == "PM" and s[:2] == "12":
            return s[:-2]
        else:
            return str(int(s[:2]) + 12) + s[2:-2]
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
