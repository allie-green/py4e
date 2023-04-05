'''
9.2
* look for lines that start with “From ” 
* look for the third word and keep a running count of each of the days of the week. 
* the program print out the contents of your dictionary (order does not matter).
'''
f_name = input('Enter a file name: ')
f_handle = open(f_name)
d = dict()

for line in f_handle:
    if not line.startswith('From '):
        continue
    day = line.split()[2]
    if day not in d:
        d[day] = 1
    else:
        d[day] +=1

print(d) 