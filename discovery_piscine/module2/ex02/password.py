#!/usr/bin/python3
# Discovery Piscine
# Module2 - Python
# ex02
# Create a program called password.py
# Ensure this program is executable
# Define a variable containing a password
password = "Python is awesome"

attempt = input()

if password != attempt:
	print("ACCESS DENIED")
elif password == attempt:
	print("ACCESS GRANTED")
