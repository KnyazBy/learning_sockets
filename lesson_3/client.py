import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
    client_sock.connect(('192.168.100.8', 10000))

    while True:
        data = client_sock.recv(1024)
        print(data.decode('utf-8'))
        message = input('You message:')
        client_sock.send(message.encode('utf-8'))

        # client_sock.close()


