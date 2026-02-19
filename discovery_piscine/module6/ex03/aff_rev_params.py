#!/usr/bin/python3
# Discovery Piscine
# Module6 - Python
# The program should:
#	When executed, the program should display all the strings passed as parameters,
#	followed by a newline, in reverse order.
#	If there are fewer than two parameters, it shoud display "none" followed by a
#	newline.

import sys

if len(sys.argv) > 2:
	for i in reversed(range(1, len(sys.argv))):
		print(sys.argv[i])
else:
	print("none")

