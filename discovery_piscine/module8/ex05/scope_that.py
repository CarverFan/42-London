#!/usr/bin/python3
# Discovery Piscine
# Module8 - Python
# The program should:
#	Inside the program, create a method called add_one that takes a parameter
#	and adds 1 to the parameter.

def add_one(num):
	num += 1
	print("Number in function: ", num)


num = 10
print("Number before it's passed to function: ", num)
add_one(num)
print("Number after it's been passed to function: ", num)

'''
Observation:
	variables in functions only have local scope.
'''
