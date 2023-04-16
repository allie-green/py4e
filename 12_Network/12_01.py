# 12_01
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
url = input('Enter an URL: ')
cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()

try:
    host_name = url.split('/')[2]
    mysock.connect((host_name, 80))
except:
    print('Improperly formatted URL, the program ends here :(')
    quit()

mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    # Check in case the URL is non-existent
    if 'HTTP/1.1 400 Bad Request' in data.decode() or 'HTTP/1.1 404 Not Found' in data.decode():
        print('Not a valid URL, the program ends here :(')
        quit()
    print(data.decode(),end='')

mysock.close()

#http://data.pr4e.org/romeo.txt