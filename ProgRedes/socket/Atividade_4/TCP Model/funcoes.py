import socket, os

def getLocalIP():
    host_name = socket.gethostname()

    host_ip = socket.gethostbyname(host_name)
    return host_ip

def getAjuda():
    ajuda = "\nAJUDA:\n\? -> Ajuda\n\\f -> Lista os arquivos do servidor\n\\d:nome_do_arquivo -> copia o arquivo para o cliente\n"
    return ajuda

def sendFile(file_name: str, sender_sock: socket):
    try:
        if not os.path.isfile(file_name):
            raise FileNotFoundError
        
        if not os.access(file_name, os.R_OK):
            raise PermissionError
        
        file_size = os.path.getsize(file_name)
        real_name = os.path.basename(file_name)

        try:
            header = f"{real_name}|{file_size}"
            sender_sock.send(header.encode(page_code))
        except socket.gaierror as e:
            raise socket.gaierror(f'ERROR: Endereço/host {e}')
        except socket.timeout as e:
            raise socket.timeout(f'ERROR: Timeout enviando header {e}')
        except socket.error as e:
            raise socket.error(f'ERROR: Erro de socket enviando header {e}')
        
        try:
            file_to_send = open(file_name, 'rb')
            while True:
                bytes_to_send = file_to_send.read(buffer_size)
                if not bytes_to_send: break
                sender_sock.send(bytes_to_send)
            file_to_send.close()
        except Exception as e:
            raise Exception(f'ERRO: Enviando arquivo{e}')
        return True
    except Exception as e:
        raise e
