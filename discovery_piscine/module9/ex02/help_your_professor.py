#!/usr/bin/python3
# Discovery Piscine
# Module9 - Python
# The program should:
#	This script should contain a method called average.
#	This method should take a dictionary as a parameter, where the
#	keys are the students' first names and the values their scores on
#	an assignment. The method should then calculate the class average
#	for that asssignment.

def average(dict):
	values = dict.values()
	avg = sum(values) / len(values)
	return avg

class_3B = {
	"marine": 18,
	"jean": 15,
	"coline": 8,
	"luc": 9
}

class_3C = {
	"quentin": 17,
	"julie": 15,
	"marc": 8,
	"stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")
