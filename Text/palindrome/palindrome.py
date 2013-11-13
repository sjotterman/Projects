#! /usr/bin/python
#palindrome.py

import sys
from ..string_reverse import string_reverse

def is_palindrome(str_input):
    if(str_input == string_reverse.reverse(str_input)):
        return True
    return False


if __name__ == "__main__":
    print("Please enter text")
    user_input = raw_input()
    if(is_palindrome(user_input)):
        print("\"" + user_input + "\" is a palindrome!")
    else:
        print("\"" + user_input + "\" is not a palindrome!")

