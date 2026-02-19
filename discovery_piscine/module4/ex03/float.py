#!/usr/bin/python3
# Discovery Piscine
# Module4 - Python
# The program should:
#	Prompt the user to enter a number.
#	Determine if the entered number is a decimal or not
#	and display the result

from decimal import Decimal

print("Give me a number:", end=" ")
num = float(input())

'''
#print(type(num))

if isinstance(num, float):
	print("This number is a decimal.")
elif isinstance(num, int):
	print("This number is an integer.")
'''

if Decimal(num) % 1 == 0:
	print("This number is a integer.")
else:
	print("This number is an decimal.")

