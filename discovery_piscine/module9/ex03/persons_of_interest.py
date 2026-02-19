#!/usr/bin/python3
# Discovery Piscine
# Module9 - Python
# The program should:
#	The script should contain a method aclled famous_births.
#	This method should take a dictionary as a parameter, representing
#	historical figures.  Each entry in the dictionary is itself a 
#	dictionary with the keys: name and date_of_birth
#	The method should sort the dictionary by birth dates and then display
#	each entry.

def famous_births(dict):
	for k, v in dict.items():
		print(f"{v['name']} is a great scientist born in {v['date_of_birth']}")

women_scientists = {
	"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
	"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
	"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
	"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)
