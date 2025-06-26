
import os

http_port = 80
https_port = 443
page_code = 'utf-8'
buffer_size = 4096
http = False
https = False

head_template = 'HEAD / HTTP/1.1\r\nHost: {}\r\nAccept: text/html\r\nConnection: close\r\n\r\n'
get_template  = 'GET / HTTP/1.1\r\nHost: {}\r\nAccept: text/html\r\nConnection: close\r\n\r\n'

dir_app = os.path.dirname(__file__)



'''
    Biblioteca de funções a serem usadas pela aplicação
'''
import socket, ssl

from constantes import *

# --------------------------------------------------
# Obtém o Status Code da Requisição
def obterStatusCode(headerResposta: str) -> int:
    strStatusLine = headerResposta.split('\r\n')[0]
    intStatusCode = int(strStatusLine.split(' ')[1]) if 'HTTP/' in strStatusLine else 0
    return intStatusCode

# --------------------------------------------------
# Extrai informações do HEADER
def extrairHeaders(headerResposta: str) -> tuple:
    strNovoHost = next((line[9:].strip() for line in headerResposta.split('\r\n') 
                      if line.lower().startswith('location:')), None)
    
    intTamanhoConteudo = int(next((line[15:].strip() for line in headerResposta.split('\r\n') 
                                 if line.lower().startswith('content-length:')), 0))
    
    return (strNovoHost, intTamanhoConteudo)

# --------------------------------------------------
# Cria um SOCKET SSL
def criarSocketSSL(host: str) -> socket:
    context = ssl.create_default_context()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_sock = context.wrap_socket(sock, server_hostname=host)
    return ssl_sock

# --------------------------------------------------
# Recebe a resposta HTTP completa
def obterFullResponse(sock: socket) -> str:
    data = b''
    while True:
        part = sock.recv(BUFFER_SIZE)
        if not part: break
        data += part
    return data.decode(CODE_PAGE, errors='ignore')

# --------------------------------------------------
# Cria um diretório com o nome do host se não existir
def criarDiretorioHost(host: str) -> str:
    host_clean = host.replace('http://', '').replace('https://', '').split('/')[0]
    host_clean = host_clean.split(':')[0]
    
    dir_host = os.path.join(DIR_APP, host_clean)
    if not os.path.exists(dir_host):
        os.makedirs(dir_host)
    return dir_host




'''
    Função principal da aplicação
'''
import socket, sys, os

from constantes import *
from lib_funcoes import *

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
    dir_host = criarDiretorioHost(host)

    #Realiza conexão e requisição get via http
    if http:
        try:
            sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            sock_tcp.connect((url, http_port))

            sock_tcp.sendall(get_template.format(url).encode(page_code))
            reply_get = obterFullResponse(sock_tcp)
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
    
    #Realiza conexão e requisição get via https
    if https:
        try:
            sock_tcp = socket.socket(sock)
            
            # Cria novo socket SSL
            sock_tcp = criarSocketSSL(new_host)
            sock_tcp.connect((url, https_port))
        
        
            sock_tcp.sendall(get_template.format(url).encode(page_code))
            reply_get = obterFullResponse(sock_tcp)
        
        
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



    try:
        # Primeiro tentamos HTTP na porta 80
        sockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #sockTCP.settimeout(10)
        sockTCP.connect((strHost, PORT_HTTP))
        
        # Requisita o Header
        sockTCP.sendall(REQ_HEAD_TEMPLATE.format(strHost).encode(CODE_PAGE))
        strRespHeader = obterFullResponse(sockTCP)
        sockTCP.close()
        
        # Obtém informações do cabeçalho
        intStatusCode = obterStatusCode(strRespHeader)
        strNewHost, _ = extrairHeaders(strRespHeader)
        
        # Salvando o Header da Requisição na porta 80
        with open(os.path.join(dir_host, 'header_porta_80.txt'), 'w', encoding=CODE_PAGE) as f:
            f.write(strRespHeader)
        
        # Se houver redirecionamento para HTTPS
        if 300 <= intStatusCode < 400 and strNewHost:
            new_host = strNewHost.split('//')[-1].split('/')[0]
            
            # Cria novo socket SSL
            sockTCP = criarSocketSSL(new_host)
            #sockTCP.settimeout(10)
            sockTCP.connect((new_host, PORT_HTTPS))
            
            # Envia requisição GET para obter conteúdo completo
            sockTCP.sendall(REQ_GET_TEMPLATE.format(new_host).encode(CODE_PAGE))
            full_response = obterFullResponse(sockTCP)
            
            # Separa headers do conteúdo
            if '\r\n\r\n' in full_response:
                strRespHeaders, strContent = full_response.split('\r\n\r\n', 1)
            else:
                strRespHeaders, strContent = full_response, ''
            
            # Salvando o Header da nova porta
            with open(os.path.join(dir_host, f'header_porta_{PORT_HTTPS}.txt'), 'w', encoding=CODE_PAGE) as f:
                f.write(strRespHeaders)
            
            # Exibe informações
            print(f'\nRedirecionado para............: {new_host}')
            print(f'Socket conectado..............: Porta {PORT_HTTPS}')
            print(f'Tamanho do conteúdo...........: {len(strContent)} bytes')
            
            # Salva o conteúdo
            with open(os.path.join(dir_host, f'conteudo_porta_{PORT_HTTPS}.txt'), 'w', encoding=CODE_PAGE) as f:
                f.write(strContent)
        else:
            # Se não houve redirecionamento, faz GET na porta 80
            sockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #sockTCP.settimeout(10)
            sockTCP.connect((strHost, PORT_HTTP))
            sockTCP.sendall(REQ_GET_TEMPLATE.format(strHost).encode(CODE_PAGE))
            full_response = obterFullResponse(sockTCP)
            
            if '\r\n\r\n' in full_response:
                strRespHeaders, strContent = full_response.split('\r\n\r\n', 1)
            else:
                strRespHeaders, strContent = full_response, ''
            
            print(f'\nSocket conectado..............: Porta {PORT_HTTP}')
            print(f'Tamanho do conteúdo..........: {len(strContent)} bytes')
            
            with open(os.path.join(dir_host, f'conteudo_porta_{PORT_HTTP}.txt'), 'w', encoding=CODE_PAGE) as f:
                f.write(strContent)
              
    except Exception as e:
        sys.exit(f'\nERRO.... {type(e).__name__}\n{str(e)}')
    finally:
        if 'sockTCP' in locals(): 
            sockTCP.close()


