# 12_05
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('data.pr4e.org', 80))
request = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
sock.send(request)

response_text = ''
response_body = ''

while True:
    data = sock.recv(300)
    if len(data) < 1:
        break
    response_text += data.decode()
sock.close()

response_body = response_text.split('\r\n\r\n', 1)[1]

print(response_body, end='')