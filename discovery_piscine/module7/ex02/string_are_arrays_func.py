#!/usr/bin/python3
# Discovery Piscine
# Module7 - Python
# The program should:
#	When executed, the program should display "z" for each occurrence of the
#	character "z" in the string passed as a parameter, followed by a newline
#	If the number of parameters is different from 1, or if there are no "z"
#	characters in the string, it should display "none" followed by a newline.

import sys, re

# I don't like the repeated use of re.findall(), I should create a function for this
def find_occurrences(t, string):
	occ = re.findall(t, string)
	return occ

if len(sys.argv) != 2 or not find_occurrences("z", sys.argv[1]):
	print("none")
else:
	string = sys.argv[1]
	occ = find_occurrences("z", string)
	for i in occ:
		print("z", end="")
	print()
