#!/usr/bin/python3
# Discovery Piscine
# Module5 - Python
# The program should:
#	Display the number of parameters passed to it, followed by a newline

import sys

# Minus 1 because sys.argv[0] is the script name
count = len(sys.argv) - 1

print(f"Number of parameters: {count}.")
