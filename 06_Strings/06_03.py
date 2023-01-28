"""
6.3
* Write a function function named count, that counts the total number of a letter in a string.
* Generalize it so that it accepts the string and the letter as arguments.
"""

def count (string,letter):
	count = 0
	for index in string:
		if index == letter:
			count += 1
	print(count) 

count("aha aha", "h")