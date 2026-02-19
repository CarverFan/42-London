#!/usr/bin/python3
# Discovery Piscine
# Module8 - Python
# The program should:
#	Define a method called greetings which takes a name as a parameter
#	and displays a welcome message with that name.
#	If the method is called without an argument, its default parameter
#	should be 'noble stranger'
#	if the method is called with an argument that is not a string, an
#	error message should be displayed instead of the welcome message.


def greetings(text='noble stranger'):
	if isinstance(text, str):
		print(f"Hello, {text}")
	else:
		print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
