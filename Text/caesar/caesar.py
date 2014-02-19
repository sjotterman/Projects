#! /usr/bin/python
#caesar.py

import sys

def shift(str_input, key):

    key = int(key)

    # ensure large keys just wrap around the alphabet
    key = key % 26
    out_str = ''
    for num in range(0,len(str_input)):
      c_init_char = str_input[num]
      i_init_char = ord(c_init_char)

      # upper case letter
      if (str.isupper(c_init_char)):
        i_new_char = i_init_char + key
        if i_new_char > 90:
          i_new_char -= 26
        c_new_char = chr(i_new_char)        
      # lower case letter
      elif (str.islower(c_init_char)):
        i_new_char = i_init_char + key
        if i_new_char > 122:
          i_new_char -= 26
      else:
         c_new_char = c_init_char
      c_new_char = chr(i_new_char)
      out_str += c_new_char

    return out_str

if __name__ == "__main__":
    print("Please enter text")
    user_input = raw_input()
    print("Please enter a number")
    shift_num = raw_input()
    print("Your text shifted " + shift_num + " spaces is: ")
    print(shift(user_input, shift_num))
