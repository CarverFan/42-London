#!/usr/bin/python3
# Discovery Piscine
# Module2 - Python
# ex00
# Create a program called iszero.py
# Ensure this program is executable (pay attention to file permissions).
# When executed, the program should prompt the user to enter a number
# If the number is equal to zero, the program should display: 
# "This number is equal to zero."
# If the number is not equal to zero, the program shoud display:
# "This number is different from zero."

number = int(input())
if number == 0:
	print("This number is equal to zero.")
else:
	print("This number is different from zero.")

# Note: inputting anything but an integer will result in an error
# A 'try' block would have to be implemented to handle this error...
