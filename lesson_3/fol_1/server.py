import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(('localhost', 10000))
    # server_sock.setblocking(False)
    server_sock.listen(10)


    while True:
        conn, addr = server_sock.accept()
        print('connected:', addr[1])
        conn.send(b'You is connect')
        data = conn.recv(1024)
        print(str(data))
        conn.send(data.upper())
        # conn.close()
