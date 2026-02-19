#!/usr/bin/python3
# Discovery Piscine
# Module3 - Python
# The program should:
#  Display multiplication tables from 0 to 10 in the following format:
#  You are only allowed to use two while loops

x = 0

while x < 11:
	print(f"Table of {x}: ", end=" ")
	y = 0
	while y < 11:
		z = x * y
		print(z, end=" ")
		y += 1
	print()
	x += 1
