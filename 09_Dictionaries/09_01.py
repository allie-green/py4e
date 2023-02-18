"""
9.1
* Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
* It doesn’t matter what the values are. 
* Then you can use the in operator as a fast way to check whether a string is in the dictionary.
"""

f_handle = open('words.txt')
dictionary = dict()
v = 0

for line in f_handle:
    words = line.split()
    for word in words:
        dictionary[word] = v
        v+= 1
    
# print(dictionary)
x = 'fun' in dictionary
print(x)