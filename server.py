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

while True:
    clientsocket.send('\nMenu:\n1. Enter data\n2. Exit\nSelect an option: '.encode('utf-8'))
    option = clientsocket.recv(1024).decode('utf-8')

    if option == '1':
        client_answer = clientsocket.recv(1024)
        print('\nReceived:', client_answer.decode('utf-8'))
        
        current_time = str(datetime.datetime.now())
        print('Received at:', current_time)

        time.sleep(5)

        response = '\nYou sent: ' + client_answer + '\nYou sent it at: ' + current_time

        response_bytes = response.encode('utf-8')

        if len(response_bytes) != clientsocket.send(response_bytes):
            print('\nError: Not all data sent successfully')
        else:
            print('\nAll data sent successfully')

    elif option == '2':
        print('Client terminated the program')
        break

clientsocket.close()

