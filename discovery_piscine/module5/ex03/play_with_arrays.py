#!/usr/bin/python3
# Discovery Piscine
# Module5 - Python
# The program should:
# 	Modify your previous program to remove duplicates in the output.
#	You should explicitly remove values from your arrays.
#	For this exercise, the use of Set is mandatory..

arr1 = [2, 8, 9, 48, 8, 22, -12, 2]
seen = set()

for val in arr1:
	if val > 5:
		# The line below isn't necessary as sets won't allow duplicates
		if val not in seen:
			seen.add(val + 2)

print(arr1)
print(sorted(seen))
