'''
9.5
* This program records the domain name (instead of the address) where the message was sent. 
* Print out the contents of your dictionary.
'''

f_name = input('Enter a file name: ')
f_handle = open(f_name)
d = dict()
addresses = list()
domains = list()

for line in f_handle:
    if not line.startswith('From '):
        continue
    addresses.append(line.split()[1])

for address in addresses:
    index = address.index('@') + 1
    domains.append(address[index:])

for domain in domains:
    d[domain] = d.get(domain, 0) + 1

print(d)