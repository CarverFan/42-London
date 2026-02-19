#!/usr/bin/python3
# Discovery Piscine
# Module6 - Python
# The program should:
#	The program should take two parameters.
#	The first parameter is a keyword to search for in a string.
#	The second parameter is the string to be searched.
#	When executed, the program should display the number of times the keyword 
#	appears in the string.
#	If the number of parameters is different from 2 or if the first string does
#	appear in the second, it should display none followed by a newline.

import sys, re

if len(sys.argv) != 3:
	print("none")
else:
	first = sys.argv[1]
	second = sys.argv[2]
	result = re.findall(first, second)
	print(len(result))
	

