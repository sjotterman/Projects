#! /usr/bin/python
#caesar.py

import sys

def shift(str_input, key):
    # ensure large keys just wrap around the alphabet
    key = key % 26
    c_init_char = str_input
    i_init_char = ord(str_input)
    
    # upper case letter
    if (i_init_char >= 65) and (i_init_char <= 90):
        i_new_char = i_init_char + key
        if i_new_char > 90:
            i_new_char -= 26
        c_new_char = chr(i_new_char)        
    # lower case letter
    elif (i_init_char >= 97) and (i_init_char <= 122):
        i_new_char = i_init_char + key
        if i_new_char > 122:
            i_new_char -= 26
        c_new_char = chr(i_new_char)

    return c_new_char

if __name__ == "__main__":
    print("Please enter text")
    user_input = raw_input()
    print("This doesnt't actually do anything yet.")
