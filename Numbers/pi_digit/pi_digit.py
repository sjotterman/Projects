#! /usr/bin/python3
#pi_digit.py

import sys
from decimal import *

def pi_digit(n):
	if (n == 1):
		return 3
	full_pi = Decimal('3.141592653589793238462643383279')
	stripped_pi = str(full_pi).strip('.')
	str_digit = stripped_pi[n:n + 1]
	return int(str_digit)
