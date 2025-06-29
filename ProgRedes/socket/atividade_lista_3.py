
import socket, sys, ssl, os

http_port = 80
https_port = 443
page_code = 'utf-8'
buffer_size = 4096
http = False
https = False

head_template = 'HEAD / HTTP/1.1\r\nHost: {}\r\nAccept: text/html\r\nConnection: close\r\n\r\n'
get_template  = 'GET / HTTP/1.1\r\nHost: {}\r\nAccept: text/html\r\nConnection: close\r\n\r\n'

dir_app = os.path.dirname(__file__)


# Processa um header e retorna o codigo de status da requisição
def getStatusCode(header_reply: str) -> int:
    status_line = header_reply.split('\r\n')[0]
    if 'HTTP/' in status_line:
        status_code = int(status_line.split(' ')[1])  
    else: 
        status_code = 0
    return status_code

# Processa o header e extrai o tamanho do conteudo e para qual host o redirecionamento aponta
def processHeaders(header_reply: str) -> tuple:
    header_lines = header_reply.split('\r\n')
    host = []
    length = []
    for line in header_lines:
        if line.lower().startwith('location:'):
            host.append(line[9:].strip())
        if line.lower().startwith('content-length:'):
            length.append(line[15:].strip())
    
    new_host = next(host, None)
    content_length = int(next(length, 0))
    
    return (new_host, content_length)

# Cria um socket SSL
def createSSLSocket(host: str) -> socket:
    context = ssl.create_default_context()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = context.wrap_socket(sock, server_hostname=host)
    return ssl_sock

# Recebe a respota a uma requisição
def getFullReply(sock: socket) -> str:
    data = b''
    while True:
        part = sock.recv(BUFFER_SIZE)
        if not part: break
        data += part
    return data.decode(CODE_PAGE, errors='ignore')


# Cria um diretório com o nome do host se não existir, para informações relacionadas
def makeHostDir(host: str) -> str:
    dir_host = os.path.join(DIR_APP, host)
    if not os.path.exists(dir_host):
        os.makedirs(dir_host)
    return dir_host


# --------------------------------------------------
def main():
    #Solicita url
    url = input('\nInforme o nome do HOST ou URL do site: ').strip()

    #Verifica se a url está conectando via http ou https
    if url.startswith('http://'):
        http = True
    if url.startswith('https://'):
        https = True
    
    #Separa o host, caminho e nome do arquivo
    url = url.replace('http://', '').replace('https://', '')
    url_content = url.split('/')
    host = url_content[0]
    if len(url_content) > 2:
        path = '/'.join(url_content[1:-2])
        file_name = url_content[-1]
    
    #Cria diretorio relacionado a conexão
    dir_host = makeHostDir(host)

    #Realiza conexão e requisição get via http
    if http:
        try:
            sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            sock_tcp.connect((url, http_port))

            sock_tcp.sendall(get_template.format(url).encode(page_code))
            reply_get = getFullReply(sock_tcp)
            sock_tcp.close()
            
            if '\r\n\r\n' in full_response:
                header_reply, content = full_response.split('\r\n\r\n', 1)
            else:
                header_reply, content = full_response, ''
            
            print(f'\nSocket conectado..............: Porta {http_port}')
            print(f'Tamanho do conteúdo..........: {len(strContent)} bytes')
            
            with open(os.path.join(dir_host, f'header_porta_{http_port}.txt'), 'w', encoding=CODE_PAGE) as f:
                f.write(header_reply)

            with open(os.path.join(dir_host, f'conteudo_porta_{http_port}.txt'), 'w', encoding=CODE_PAGE) as f:
                f.write(content)

        except Exception as e:
            sys.exit(f'\nERRO ----- {type(e).__name__}\n{str(e)}')
        
        finally:
            if 'sock_tcp' in locals():
                sock_tcp.close()
    
    #Realiza conexão e requisição get via https
    if https:
        try:
            sock_tcp = socket.socket(sock)
            
            # Cria novo socket SSL
            sock_tcp = createSSLSocket(new_host)
            sock_tcp.connect((url, https_port))
        
        
            sock_tcp.sendall(get_template.format(url).encode(page_code))
            reply_get = getFullReply(sock_tcp)
        
        
            if '\r\n\r\n' in full_response:
                header_reply, content = full_response.split('\r\n\r\n', 1)
            else:
                header_reply, content = full_response, ''
        
        
            # Exibe informações
            print(f'\nRedirecionado para............: {new_host}')
            print(f'Socket conectado..............: Porta {https_port}')
            print(f'Tamanho do conteúdo...........: {len(strContent)} bytes')
        
            with open(os.path.join(dir_host, f'header_porta_{https_port}.txt'), 'w', encoding=CODE_PAGE) as f:
                f.write(header_reply)
        
            with open(os.path.join(dir_host, f'conteudo_porta_{https_port}.txt'), 'w', encoding=CODE_PAGE) as f:
                f.write(content)
        
        except Exception as e:
            sys.exit(f'\nERRO ----- {type(e).__name__}\n{str(e)}')
        
        finally:
            if 'sock_tcp' in locals():
                sock_tcp.close()
