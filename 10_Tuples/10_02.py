'''
10.02
* Pull the hour from the “From” line.
* Accumulate the counts for each hour.
* Print out the counts, one per line, sorted by hour.
'''

fname = input("Enter a file name: ")
fhandle = open(fname)
l_hours = list()
l_hours_sorted = list()
d = dict()

for line in fhandle:
    if line.startswith('From '):
        l_hours.append(line.split()[5][0:2])

for x in l_hours:
    d[x] = d.get(x, 0) + 1

l_hours_sorted = sorted(d.items())

for (k, v) in l_hours_sorted:
    print(k,v)