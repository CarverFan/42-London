#!/usr/bin/python3
# Discovery Piscine
# Module3 - Python
# The program should:
# 	Accepts user input, which will be stored in a numeric variable.
#	Display the multiplication table for that number 
#	(e.g., if the input is 2, display the multiplication table for 2)

print("Enter a number")
num = int(input())

for i in range(0, 13):
	answer = i * num
	print(f"{i} x {num} = {answer}")
