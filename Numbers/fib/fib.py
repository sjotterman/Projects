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
  print("Fibonacci numbers. \n Please enter an integer.")
  str_num = (raw_input())
  i_num = int(str_num)
  print("Fibonacci number " + str_num + " is:")
  print(fib(i_num))

if __name__ == "__main__":
        main()
