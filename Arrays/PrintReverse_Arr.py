#!/bin/python

from __future__ import print_function

import os
import sys


#
# Complete the reverseArray function below.
#
def reverseArray(a):
    return a[::-1]
    #
    # Write your code here.
    #


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
