#!/bin/python

from __future__ import print_function

import os
import sys


#
# Complete the arrayManipulation function below.
#


def arrayManipulation(n, queries):
    #
    # Write your code here.
    #
    if n >= 3 and n <= pow(10, 7):
        test_list = [0] * n
        if len(queries) >= 1 and len(queries) <= 2 * pow(10, 5):
            for query in queries:
                query = list(query)
                a = query[0] - 1
                b = query[1] - 1
                if a >= 0 and a <= n - 1 and b >= 0 and b <= n - 1:
                    k = query[2]
                    if k >= 0 and k <= pow(10, 9):
                        if 0 <= a < len(test_list):
                            test_list[a] += k
                        if a < b < len(test_list):
                            test_list[b] -= k

            max_number = sys.maxsize * -1
            number = 0
            for val in test_list:
                number += val
                max_number = max(max_number, number)
            return max_number


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(map(int, input().rstrip().split()))

    result = arrayManipulation(n, queries)

    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
