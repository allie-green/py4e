'''
10.03
* Write a program that reads a file and prints the letters in decreasing order of frequency. 
* Convert all the input to lower case.
* Your program should not count spaces, digits, punctuation, or anything other than the letters a-z.
'''
import string

fname = input('Enter a text file: ')
fhandle = open(fname)
letters = list()
d = dict()

for line in fhandle:
    line = line.translate(str.maketrans('','', string.punctuation + string.digits)).lower()
    words = line.split()

    for word in words:
        for char in word:
            letters.append(char)

for char in letters:
    d[char] = d.get(char, 0) + 1

letters = sorted([(v,k) for (k,v) in d.items()], reverse=True)

for (k,v) in letters:
    print(v,k)