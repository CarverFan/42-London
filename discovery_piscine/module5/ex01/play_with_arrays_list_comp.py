#!/usr/bin/python3
# Discovery Piscine
# Module5 - Python
# The program should:
# Create a program called play_with_arrays.py
# Ensure this program is executable
# Define an array of numbers
# Iterate over this array, creating a new array by adding 2 to each value in the original
# array.
# Your program should contain two arrays: The original array and the modified array.
# Display both arrays on the screen.

arr1 = [2, 8, 9, 48, 8, 22, -12, 2]

arr2 = [n+2 for n in arr1]

print(arr1)
print(arr2)
