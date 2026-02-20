#!/usr/bin/python3
# Discovery Piscine
# Module8 - Python
# The program should:
#	The downcase_it method should take a string as an argument and return
#	the string in lowercase
#	Apply this method to each program's parameters and display the return
#	value for each.
#	If there are no parameters, display "none" followed by a line break.

import sys

def downcase_it(el):
	elow = el.lower()
	return elow

if len(sys.argv) >= 2:
	for el in sys.argv[1:]:
		print(downcase_it(el))
else:
	print("none")

