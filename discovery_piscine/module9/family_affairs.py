#!/usr/bin/python3
# Discovery Piscine
# Module9 - Python
# The program should:
#	This should contain a method called find_the_redheads
#	This method will take a dictionary as a parameter, where the keys
#	are family members' first names and the values are their hair colors
#	The method should use the filter function to collect the first names
#	of individuals with red hair into a new list, which it will return.
#	The result must be converted into a list before being returned by using 
#	the function list()

def find_the_redheads(dict):
	nlist = []
	for key, value in dict.items():
		if value == "red":
			nlist.append(key)
	return nlist

dupont_family = {
	"florian": "red",
	"marie": "blond",
	"virginie": "brunette",
	"david": "red",
	"franck": "red"
}


print(find_the_redheads(dupont_family))
