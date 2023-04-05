'''
9.3 (basically the same as in exercise 9.2 )
 * build a histogram using a dictionary to count how many messages have come from each email address
 * print the dictionary.
 ** personal requierment: use dict.get(key,value) method.
'''
f_name = input('Enter a file name: ')
f_handle = open(f_name)
d = dict()
senders = list()

for line in f_handle:
    if not line.startswith('From '):
        continue
    senders.append(line.split()[1])

for address in senders:
    d[address] = d.get(address,0) + 1

print(d)