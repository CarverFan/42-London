#!/usr/bin/python3
# Discovery Piscine
# Module5 - Python
# The program should:
# 	Modify your previous program to remove duplicates in the output.
#	You should explicitly remove values from your arrays.
#	For this exercise, the use of Set is mandatory..

arr1 = [2, 8, 9, 48, 8, 22, -12, 2]

seen = {n+2 for n in arr1 if n > 5}

print(arr1)
print(sorted(seen))
