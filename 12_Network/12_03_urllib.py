import urllib.request

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo-full.txt')
chars = 0
printed_chars = 0

for line in fhand:
    text = line.decode().strip()
    chars += len(text)

    if chars <= 3000:
        print(text)
        printed_chars += len(text)

fhand.close()

print(f'\nTotal number of characters: {chars}')
print(f'Total number of printed characters: {printed_chars}')