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

def downcase_it(text):
	print(text.lower())

if len(sys.argv) >= 2:
	for text in sys.argv[1:]:
		downcase_it(text)
else:
	print("none")

