#!/usr/bin/python3
# Discovery Piscine
# Module2 - Python
# ex03
# Create a program called mult.py
# Ensure the program is executable
# When executed, the program should prompt the user to enter 2 numbers
# The program should:
#	Display whether the result of multiplying the two numbers is positive, negative, or zero.
#	Display the result of the multiplication

print("Enter the first number: ", end=" ")
first_num = int(input())

print("Enter the second number: ", end=" ")
second_num = int(input())

result = first_num * second_num

print(f"{first_num} x {second_num} = {result}")

if result < 0:
	print("The result is negative.")
elif result > 0:
	print("The result is positive.")
elif result == 0:
	print("The result is positive and negative.")
