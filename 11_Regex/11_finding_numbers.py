import re
file = open("regex_sum_1729292.txt")
total = 0

for line in file:
    x = re.findall('[0-9]+',line)
    if len(x) > 0:
        for num in x:
            total += int(num)
print(total)