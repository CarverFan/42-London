#!/usr/bin/python3
# Discovery Piscine
# Module7 - Python
# The program should:
#	This program should take 2 numbers as parameters
#	The first number must be strictly small than the second one.
#	You must construct an array containing all the values between
#	these two numbers
#	You must display the array using the print function
#	If the number of parameters is different from 2, the program
#	displays 'none' followed by a newline.

import sys

arr = []

if len(sys.argv) != 3:
	print("none")
else:
	first = int(sys.argv[1])
	second = int(sys.argv[2])
	for i in range(first, second + 1):
		arr.append(i)
	print(arr)

