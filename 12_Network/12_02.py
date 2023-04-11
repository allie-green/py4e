'''
12.02
* Retrieve the entire document and count the total number of characters.
* Stop displaying any text after it has shown 3000 characters.
* Display the count of the number of characters at the end of the document.
'''
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = input('Enter an URL: ')
cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
count = 0

try:
    host_name = url.split('/')[2]
    mysock.connect((host_name, 80))
except:
    print('Improperly formatted URL, the program ends here :(')
    quit()

mysock.send(cmd)

while True:
    data = mysock.recv(500) # the num of bytes recived depends on the internet connection
    if len(data) < 1:
        break

    # Check if response contains 400 Bad Request or 404 Not Found
    if '400 Bad Request' in data.decode() or '404 Not Found' in data.decode():
        print('Non-existent URL, the program ends here :(')
        quit()

    count += len(data)

    if count <= 3000:
        print(data.decode(),end='')

print(f'\nNumber of characters: {count}')

mysock.close()

#http://data.pr4e.org/romeo.txt
#http://data.pr4e.org/romeo-full.txt