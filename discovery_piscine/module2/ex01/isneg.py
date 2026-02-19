#!/usr/bin/python3
# Discovery Piscine
# Module2 - Python
# ex01
# Create a program called isneg.py
# Ensure this program is executable
# When executed, the program should prompt the user to enter a number
# If the number is negative, the program should display "This number is negative."
# If the number is positive, the program should display "This number is positive."
# If the number is equal to zero, the program should display "This number is both positive and negative."
number = int(input())

if number < 0:
	print("This number is negative.")
elif number > 0:
	print("This number is positive.")
elif number == 0:
	print("This number is both positive and negative.")
