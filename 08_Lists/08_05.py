'''
8.5
* Write a program to read through the mail box data and find the lines that start with “From”.
* NOT “From:”
* Print out the second word for each From line.
* Count the number of From lines.
'''
f_name = input('Enter a file name: ')

f_handle = open(f_name)
count = 0

for line in f_handle:
    if not line.startswith('From '): # 'From '(notice the space)
        continue
    count += 1
    list = line.split()
    sender = list[1]
    print(sender)
print(f'There were {count} lines in the file with From as the first word')