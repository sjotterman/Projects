#! /usr/bin/python
#fib.py

import sys

def fib(n):
    return n        

def main():
   if (len(sys.argv) == 2):    
       print(fib(sys.argv[1]))   

if __name__ == "__main__":
        main()
