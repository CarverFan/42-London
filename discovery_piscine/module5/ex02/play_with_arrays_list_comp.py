#!/usr/bin/python3
# Discovery Piscine
# Module5 - Python
# The program should:
# Modify your previous program to process only the values greater than 5 in the 
# original array.

arr1 = [2, 8, 9, 48, 8, 22, -12, 2]

arr2 = [n+2 for n in arr1 if n > 5]

print(arr1)
print(arr2)
