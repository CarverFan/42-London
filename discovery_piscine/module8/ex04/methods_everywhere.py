#!/usr/bin/python3
# Discovery Piscine
# Module8 - Python
# The program should:
# You need to create two different methods in this program:
#	The shrink method: Should take a string as a parameter and displays the
#	first eight characters of that string.
#	The enlarge method: Should take a string as a parameter and appends 'Z'
#	characters until the string has a total of eight characters. Then, it 
#	displays the resulting string.
# For each argument passed to the program:
#	If the argument has more than eight characters, call the shrink method on it.
# 	If the argument has less than eight characters, call the enlarge method in it.
#	If the argument has exactly eight characters, display it directly followed by
#	a new line.

import sys

def shrink(text):
	print(text[:8])

def enlarge(text):
	diff = 8 - len(text)
	print(text + "z" * diff)

if len(sys.argv) < 2:
	print("none")
else:
	for i in sys.argv[1:]:
		if len(i) > 8:
			shrink(i)
		elif len(i) < 8:
			enlarge(i)
		else:
			print(i)
