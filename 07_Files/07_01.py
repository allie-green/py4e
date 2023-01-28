"""
7.1  Write a program to read through a file and print the contents of the file (line by line) all in upper case.
"""
f_name = input("Enter a file name: ")
f_handle = open(f_name)

for line in f_handle:
	print(line.upper())