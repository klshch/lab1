import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9999
s.connect((host, port))

while True:
    menu = s.recv(1024).decode('utf-8')
    print(menu, end='')

    choice = input()
    s.send(choice.encode('utf-8'))

    if choice == '1':
        sentence = input('\nEnter a sentence: ')
        s.send(sentence.encode('utf-8'))

        server_response = s.recv(1024).decode('utf-8')
        print(server_response)

    elif choice == '2':
        print('\nYou have exited the program.')
        break

s.close()
