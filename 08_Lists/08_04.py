"""
8.4. Find all unique words in a file.

* List all unique words, sorted in alphabetical order, that are stored in a file romeo.txt
* Create a list of unique words, which will contain the final result.
"""
f_name = input('Enter file: ')
f_handle = open(f_name)
unique_words = list()

for line in f_handle:
    words = line.split()
    for word in words:
        x = word in unique_words
    if x == True:
        continue
unique_words.append(word)
unique_words.sort()
print(unique_words)