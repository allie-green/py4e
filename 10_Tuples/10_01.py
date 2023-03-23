"""
10.01
* Read and parse the “From” lines and pull out the addresses from the line.
* Count the number of messages from each person using a dictionary.
* Create a list of tuples from the dictionary.
* Sort the list in reverse order and print out the person who has the most commits.
"""

fname = input("Enter a file name: ")
fhandle = open(fname)
l = list()
l_items = list()
d = dict()

for line in fhandle:
    if line.startswith('From '):
        l.append(line.split()[1])

for x in l:
    d[x] = d.get(x, 0) + 1

# two options to sort the list in desending order

# swapping (key, val) for (val, key), then `sort()`
# for key,val in list(d.items()):
#     l_items.append((val,key))
# l_items.sort(reverse=True)

# or with [list comprehension] as first argument in `sorted()` function
l_items = sorted([ (v,k) for (k,v) in d.items()], reverse=True)

for v,k in l_items[:1]:
    print(k,v)
