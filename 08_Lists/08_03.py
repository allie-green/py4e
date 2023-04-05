"""
8.3
* Rewrite the guardian code in the example without two if statements. 
* Instead, use a compound logical expression using the or logical operator with a single if statement.

Example: 
fhand = open('mbox-short.txt')
for line in fhand:
  words = line.split()
  #the guardian
  if len(words) < 3:
   continue
  if words[0] != 'From':
    continue
  print(words[2])
"""

fhand = open('mbox-short.txt')

for line in fhand:
    words = line.split()
    # the guardian goes first, 
    # otherwise IndexError: list index out of range.
    if len(words) < 3 or words[0] != 'From':
        continue

print(words[2])