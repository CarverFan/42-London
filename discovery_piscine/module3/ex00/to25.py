#!/usr/bin/python3
# Discovery Piscine
# Module3 - Python
# The program should:
# Accepts user input, which will be stored in a numeric variable.
# Use a loop to display all numbers from entered number up to 25.
# If the input number is greater than 25, display "Error" followed by a newline.


print("Enter a number less than 25")
num = int(input())

if num > 25:
	print("Error")
else:
	while num <= 25:
		print(f"Inside the loop, my variable is {num}")
		num += 1
