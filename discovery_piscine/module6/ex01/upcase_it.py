#!/usr/bin/python3
# Discovery Piscine
# Module6 - Python
# The program should:
# 	Display the string in uppercase, followed by a newline
#	If the number of parameters is different from 1, display "none" 
#	followed by a newline

import sys

if len(sys.argv) > 1:
	first = sys.argv[1]
	print(first.upper())
else:
	print("none")

