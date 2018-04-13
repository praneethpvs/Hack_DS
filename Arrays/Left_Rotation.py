#!/bin/python

from __future__ import print_function

import os
import sys

if __name__ == '__main__':
    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())
    s = d % n
    r = a[s:] + a[:s]
    print(*r, sep=" ")
