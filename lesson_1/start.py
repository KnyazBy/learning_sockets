import socket
import views as v


URLS = {
        '/': v.index,
        '/blog': v.blog
        }


def parse_reg(reg):
    parsed = reg.split(' ')
    #print(parsed)
    method = parsed[0]
    #print(method)
    url = parsed[1]
    #print(url)
    return (method, url)


def gen_head(method, url):
    if not method == 'GET':
        return ('HTTP/1.1 405 Method not allowed\n\n', 405)

    if not url in URLS:
        return('HTTP/1.1 404 Not found\n\n', 404)

    return ('HTTP/1.1 200 Ok\n\n', 200)


def gen_cont(code, url):
    if code == 404:
        return '<h1>404</h1><p>Not found</p>'
    if code == 405:
        return '<h1>405</h1><p>Method not allowed</p>'
    #return '<h1>{}</h1>'.format(URLS[url])
    return URLS[url]()


def gen_res(reg):
    method, url = parse_reg(reg)
    headers, code = gen_head(method, url)
    body = gen_cont(code, url)
    #return (headers + 'hello').encode('utf-8')
    return (headers + body).encode('utf-8')

def run_serv():
    ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ser_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ser_sock.bind(('localhost', 5000))
    ser_sock.listen()

    while True:
       cl_sock, addr =  ser_sock.accept()
       reg = cl_sock.recv(1024)
       #print(reg)#decode('UTF-8')
       #print()
       print(addr)
       
       res = gen_res(reg.decode('utf-8'))
       cl_sock.sendall(res)
       cl_sock.close()



if __name__ == ('__main__'):
    run_serv()
