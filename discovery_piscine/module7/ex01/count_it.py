#!/usr/bin/python3
# Discovery Piscine
# Module7 - Python
# The program should:
#	Display "parameters:" followed by thetotal number of parameters
#	passed as arguments.
#	For each parameter, display the parameter itself and its length,
#	ending with a newline.
#	If no parameters are provided, display "none" followed by a newline.

import sys

if len(sys.argv) <= 1:
	print("none")
else:
	for word in range(1, len(sys.argv)):
		print(sys.argv[word], end=": ")
		print(len(sys.argv[word]))
