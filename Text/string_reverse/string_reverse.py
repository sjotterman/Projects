#! /usr/bin/python

import sys

def reverse(input):
    out_str = ''
    for num in range(len(input) - 1, -1, -1):
        out_str += input[num]
    return out_str



if __name__ == "__main__":
    print("Please enter the text you want reversed.")
    user_input = raw_input()
    print(reverse(user_input))
