import socket
import select
import sys


if len(sys.argv) != 3:
    print(b'Correct usage: name script, IP address, port number')
    exit()

IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.connect((IP_address, Port))

    while True:
        socket_list = [sys.stdin, server]
        read_sockets, write_socket, error_socket = select.select(socket_list, [], [])
        for socks in read_sockets:
            print(socket_list.remove(socks))
            if socks == server:
                message = socks.recv(2048).decode('utf-8')
                print(message)
            else:
                message = sys.stdin.readline()
                server.send(message.encode('utf-8'))
                sys.stdout.write('You')
                sys.stdout.write()
                sys.stdout.flush()
                # print(message)
    
        server.close()
