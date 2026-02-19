#!/usr/bin/python3
# Discovery Piscine
# Module4 - Python
# The program should:
#	Prompt the user to enter their age.
#	Display the user's current age and their age in 10, 20 & 30 years

print("Please tell me your age: ", end=" ")
age = int(input())

print(f"You are currently {age} years old.")

for i in range(10, 40, 10):
	print(f"In {i} years, you'll be {i+age} years old.") 

