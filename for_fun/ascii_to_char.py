# convert ASCII values to characters

in_values = input('Enter the ASCII values separeted by a space: ')
l_values = in_values.split(' ')
chars = ''

for i in l_values:
    ascii_value = int(i)
    chars += chr(ascii_value)

print(f'The ASCII values represent the following:\n{chars}')
