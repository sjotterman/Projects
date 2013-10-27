#! /usr/bin/python
##factorial.py

import sys

def fact_rec(n):
    if (n == 0):
        return 1
    if (n == 1):
        return 1
    if (n < 0):
        return 0
    return n * fact_rec(n - 1)

def fact_it(n):
    if (n < 0):
        return 0
    if (n <= 1):
        return 1
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    return sum

def main():
   if (len(sys.argv) == 2):
       print(fact_it(sys.argv[1]))
   else:
       print("Usage: ", sys.argv[0], " [number]")

if __name__ == "__main__":
        main()
