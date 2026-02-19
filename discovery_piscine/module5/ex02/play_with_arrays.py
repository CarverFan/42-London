#!/usr/bin/python3
# Discovery Piscine
# Module5 - Python
# The program should:
# Modify your previous program to process only the values greater than 5 in the 
# original array.

arr1 = [2, 8, 9, 48, 8, 22, -12, 2]
arr2 = []

for val in arr1:
	#print("inner", val)
	if val > 5:
		arr2.append(val + 2)
		#print(i)

print(arr1)
print(arr2)
