import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9999
s.connect((host, port))

while True:
    server_response = s.recv(1024).decode('utf-8')
    print(server_response, end='')

    sentence = input()
    s.send(sentence.encode('utf-8'))

    server_response = s.recv(1024).decode('utf-8')
    print(server_response)

    break

s.close()
