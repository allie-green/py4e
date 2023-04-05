import re
fname = input('Enter a file name: ')
fhandle = open(fname)
regex = input('Enter a regular expression: ')
count = 0

for line in fhandle:
    line = line.strip()
    if re.search(regex, line): count += 1

print(f'{fname} had {count} lines that matched {regex}')