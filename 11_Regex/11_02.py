import re
fhandle = open("mbox.txt")
count = 0
total = 0

for line in fhandle:
    line = line.strip()
    x = re.findall('^New Revision: ([0-9]+$)', line)
    if len(x) > 0: 
        count +=1
        for num in x:
            total += int(num)

print(int(total/count))
