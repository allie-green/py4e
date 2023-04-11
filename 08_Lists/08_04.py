"""
8.4. Find all unique words in a file.
"""
f_name = input('Enter file: ')
f_handle = open(f_name)
unique_words = list()

for line in f_handle:
    words = line.split()
    for word in words:
        x = word in unique_words
        if x == False:
            unique_words.append(word)

unique_words.sort()
print(unique_words)