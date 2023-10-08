import socket
import datetime
import time

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

    time.sleep(5)

    response = '\nYou sent: ' + client_answer.decode('utf-8') + '\nYou sent it at: ' + current_time

    response_bytes = response.encode('utf-8')

    if len(response_bytes) != clientsocket.send(response_bytes):
        print('\nError: Not all data sent successfully')
    else:
        print('\nAll data sent successfully')
        break  

clientsocket.close()

