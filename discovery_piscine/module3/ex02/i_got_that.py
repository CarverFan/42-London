#!/usr/bin/python3
# Discovery Piscine
# Module3 - Python
# The program should:
# 	Use a while loop that continously accepts user input and responds with
#	"I got that! Anything else?" after each input
#	The loop should only stop when the user enters "STOP"

print("What you gotta say? : ", end=" ")
text = input()

while text != "STOP":
	print("I got that! Anything else? : ", end=" ")
	text = input()
