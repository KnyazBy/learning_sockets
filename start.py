import socket
import views


URLS = {
        '/': views.index,
        '/blog': views.blog
        }


def parse_request(request):
    parsed = request.split(' ')
    #print(parsed)
    method = parsed[0]
    #print(method)
    url = parsed[1]
    #print(url)
    return (method, url)


def generate_headers(method, url):
    if not method == 'GET':
        return ('HTTP/1.1 405 Method not allowed\n\n', 405)

    if not url in URLS:
        return('HTTP/1.1 404 Not found\n\n', 404)

    return ('HTTP/1.1 200 Ok\n\n', 200)


def generate_content(code, url):
    if code == 404:
        return '<h1>404</h1><p>Not found</p>'
    if code == 405:
        return '<h1>405</h1><p>Method not allowed</p>'
    #return '<h1>{}</h1>'.format(URLS[url])
    return URLS[url]()


def generate_respons(request):
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)
    body = generate_content(code, url)
    #return (headers + 'hello').encode('utf-8')
    return (headers + body).encode('utf-8')

def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
       client_socket, addr =  server_socket.accept()
       request = client_socket.recv(1024)
       #print(request)#decode('UTF-8')
       #print()
       print(addr)
       
       response = generate_respons(request.decode('utf-8'))
       client_socket.sendall(response)
       client_socket.close()



if __name__ == ('__main__'):
    run()
