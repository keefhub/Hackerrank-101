import math
import os
import random
import re
import sys


def matchingStrings(strings, queries):
    results = [0] * len(queries)

    for i in range(len(queries())):
        v = queries[i]
        results[i] = strings.count(v)

    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
