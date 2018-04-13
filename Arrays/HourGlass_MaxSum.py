#!/bin/python

from __future__ import print_function
import os


#
# Complete the array2D function below.
#
def array2D(arr):
    #
    # Write your code here.
    #
    smax = -9 * 7
    for row in range(len(arr) - 2):
        for column in range(len(arr[row]) - 2):
            tl = arr[row][column]
            tc = arr[row][column + 1]
            tr = arr[row][column + 2]
            mc = arr[row + 1][column + 1]
            bl = arr[row + 2][column]
            bc = arr[row + 2][column + 1]
            br = arr[row + 2][column + 2]
            s = tl + tc + tr + mc + bl + bc + br
            smax = max(s, smax)
    return smax


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = array2D(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
