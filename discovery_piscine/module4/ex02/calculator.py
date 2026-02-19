#!/usr/bin/python3
# Discovery Piscine
# Module4 - Python
# The program should:
#	Prompt the user to enter two numbers.
#	Store these numbers as numeric values in two variables.
#	Display the result of adding, subtracting, dividing and 
#	multiplying these numbers.

print("Give me the first number: ", end=" ")
first_num = int(input())
print("Give me the second number: ", end=" ")
second_num = int(input())
print("Thank you!")
print(f"{first_num} + {second_num} = {first_num + second_num}")
print(f"{first_num} - {second_num} = {first_num - second_num}")
print(f"{first_num} / {second_num} = {first_num / second_num}")
print(f"{first_num} * {second_num} = {first_num * second_num}")
