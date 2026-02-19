#!/usr/bin/python3
# Discovery Piscine
# Module6 - Python
# The program should:
# 	Display the frist string parameter passed, followed by a newline.
#	If there are no parameters, display "none" followed by a newline.

import sys

if len(sys.argv) > 1:
	first = sys.argv[1]
	print(first)
else:
	print("none")
