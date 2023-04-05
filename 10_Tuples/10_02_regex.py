import re
fhandle = open("mbox-short.txt")
l_hours = list()
d = dict()

for line in fhandle:
    line = line.strip()
    h = re.findall('^From.+ ([0-9][0-9]):', line)
    if len(h) > 0:
        for hour in h:
            l_hours.append(hour)

for x in l_hours:
    d[x] = d.get(x, 0) + 1

hours_sorted = sorted(d.items())
for (k, v) in hours_sorted:
    print(k,v)

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008