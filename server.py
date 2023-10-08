import socket
import datetime

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9999
serversocket.bind((host, port))
serversocket.listen(5)
print('\nThe server is waiting for connection')

clientsocket, addr = serversocket.accept()
print('Got a connection from {}'.format(addr))

clientsocket.send('\nSend something: '.encode('utf-8'))

while True:
    client_answer = clientsocket.recv(1024)
    print('\nReceived:', client_answer.decode('utf-8'))

    current_time = str(datetime.datetime.now())
    print('Received at:', current_time)

    break  

clientsocket.close()

