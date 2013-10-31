#! /usr/bin/python

import sys

def reverse(input):
    out_str = ''
    for num in range(len(input) - 1, -1, -1):
        out_str += input[num]
    return out_str
