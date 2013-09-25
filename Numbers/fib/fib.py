#! /usr/bin/python3
#fib.py

import sys

def fib(n):
    return n        

def main():
   if (len(sys.argv) == 2):    
       print(fib(sys.argv[1]))   
   else:
       print("Usage: ", sys.argv[0], " [number]")

if __name__ == "__main__":
        main()
