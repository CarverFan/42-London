#!/usr/bin/python3
# Discovery Piscine
# Module4 - Python
# The program should:
# 	Prompt the user to enter a sttring
#	Display the string with uppercase letters changed to lower case
#	and vice versa

text = input()

for i in text:
	if i.isupper():
		print(i.lower(), end="")
	else:
		print(i.upper(), end="")
print()

# see swapcase()
