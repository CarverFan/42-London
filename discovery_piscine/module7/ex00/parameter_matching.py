#!/usr/bin/python3
# Discovery Piscine
# Module7 - Python
# The program should:
#	Take a string as a parameter.
#	Prompt the user to enter a word that matches the parameter passed
#	as an argument, as shown in the example below.
#	Display "Good job!" followed by a newline if the word entered by the user
#	matches the parameter passed.
#	Display "Nope, sorry..." followed by a newline if the word entered by the
#	user does not match the parameter passed.
#	Display "none" followed by a newline if the number of parameters passed
#	is different from 1.

import sys, re

if len(sys.argv) != 2:
	print("none")
else:
	attempt = sys.argv[1]
	secret = "Hello"
	if attempt == secret:
		print("Good job!")
	else:
		print("Nope, sorry...")
