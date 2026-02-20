#!/usr/bin/python3
# Discovery Piscine
# Module9 - Python
# The program should:
#	This script should contain a method called array_of_names
#	This method should take a dictionary that associates first names with
#	last names as its parameter.
# 	It should build an array containing he full names of the people, with the first
#	letter of each name capitalized. The method should then return this array.

def array_of_names(name_dict):
	names = []
	for first, last in name_dict.items():
		names.append(first.capitalize() + " " + last.capitalize())
	return names

persons = {
	"jean": "valjean",
	"grace": "hopper",
	"xavier": "niel",
	"fifi": "brindacier"
}

print()
print(array_of_names(persons))
print()
