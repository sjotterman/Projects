#! /usr/bin/python3
#pi_digit.py

import sys

def pi_digit(n):
	if (n == 1):
		return 3
	full_pi = 3.141591
	stripped_pi = str(full_pi)
	str_digit = stripped_pi[n:n + 1]
	return int(str_digit)
