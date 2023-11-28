import socket 
import select
import _thread
import sys



def th_client(conn, addr):
    conn.send(b'Welcome to this chatroom')
    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                print(message + 'Это прошло')
        except:
            continue



def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    if len(sys.argv) != 3:
        print(b'Correct usage: name script, IP address, port number')
        exit()

    IP_address = str(sys.argv[1])
    Port = int(sys.argv[2])
    server.bind((IP_address, Port))

    server.listen(99)

    while True:
        conn, addr = server.accept()
        list_of_client.append(conn)
        print(addr[0] + "connected")
        _thread.start_new_thread(th_client, (conn, addr))
        # conn.close()
        server.close()

    

if __name__ == ('__main__'):
    list_of_client = []
    run_server()
    
