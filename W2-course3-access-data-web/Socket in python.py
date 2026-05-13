#using socket to connect web pages
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET https://xxxxxxxxxxxxxx.html HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
#bind URL addresss as 'xxxxxxxxxxxxxx'

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()