"""
6.1 Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.
"""

string = "honey"

# in this way we start at the last index of the string
index = len(string) - 1 #length is 5, the last letter has index 4

while index >= 0:
	letter = string[index]
	print(letter)
	index -= 1 
