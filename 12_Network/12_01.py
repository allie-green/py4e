'''
12.01
* Prompt the user for the URL so it can read any web page. 
* Use split('/') to break the URL so you can extract the host name for the socket connect call. 
* Use try and except to handle the condition where the user enters an improperly formatted or non-existent URL.
'''
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
    # Check if response contains 400 Bad Request or 404 Not Found
    # in case the URL is non-existent
    if '400 Bad Request' or '404 Not Found' in data.decode():
         print('Non-existent URL, the program ends here :(')
         quit()
    print(data.decode(),end='')

mysock.close()

#http://data.pr4e.org/romeo.txt