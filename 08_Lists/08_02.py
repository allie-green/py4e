# 8.2
# write a program that is looking for the day of the week on the from lines of our known file:

f_handel = open('mbox-short.txt')

for line in f_handel:
    if not line.startswith("From"):
        continue
    words = line.split()
    if len(words) < 3: #we are looking for index 2
        continue
print(words[2])