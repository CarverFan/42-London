#!/usr/bin/python3
# Discovery Piscine
# Module7 - Python
# The program should:
#	Display each parameter passed as an argument, one by one, by
#	appending it with "ism"
#	If a parameter already ends with "ism", it should be skipped and not
#	displayed.
#	If there are no parameters, the  program should display "none" followed
#	by a newline

import sys

if len(sys.argv) <= 1:
	print("none")
else:
	# iterate over the list starting at second position - slicing!
	for i in sys.argv[1:]:
		ism = i.find("ism")
		if ism == -1:
			print(i[0:] + "ism")





