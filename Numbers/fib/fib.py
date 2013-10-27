#! /usr/bin/python
#fib.py

import sys

def fib(n):
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    return fib(n -1) + fib(n - 2)

def main():
   if (len(sys.argv) == 2):
       print(fib(sys.argv[1]))
   else:
       print("Usage: ", sys.argv[0], " [number]")

if __name__ == "__main__":
        main()
