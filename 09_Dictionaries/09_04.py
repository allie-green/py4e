'''
9.4
* Add code to 9.3 to figure out who has the most messages in the file.
* print how many messages the person has.
'''

f_name = input('Enter a file name: ')
f_handle = open(f_name)
d = dict()
senders = list()
most_address = None
most_count = None

for line in f_handle:
    if not line.startswith('From '):
        continue
    senders.append(line.split()[1])

for address in senders:
    d[address] = d.get(address,0) + 1
#   {key: value}
for key,value in d.items():
    if most_count is None or value > most_count:
        most_count = value
        most_address = key

print(most_address, most_count)