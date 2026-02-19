#!/usr/bin/python3
# Discovery Piscine
# Module8 - Python
# The program should:
#	The upcase_it method should take a string as an argument and return the string
#	in uppercase.
#	Test the method by calling it in your program. In the example below, we test it
#	with "hello".

import sys

def upcase_it(text):
	print(text.upper())

if len(sys.argv) == 2:
	text = sys.argv[1]
	upcase_it(text)
else:
	print("none")

