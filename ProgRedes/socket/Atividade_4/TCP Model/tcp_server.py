import socket

from constantes import *
from funcoes import *

tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_sock.bind((host_server_ip,host_port))

tcp_sock.listen(4)
print("Recebendo Comandos")


while True:
    conexao, address = tcp_sock.accept()

    mensagem_bytes = conexao.recv(buffer_size)
    mensagem_str = mensagem_bytes.decode(page_code).lower().strip()

    erro = True

    if mensagem_str == "\\?":
        reply_msg = getAjuda()
    elif mensagem_str.startswith("\\d:"):
        comando, nome_arq = mensagem_str.split(":")
        if not nome_arq:
            reply_msg = 'Erro: nome do arquivo não informado'
        else:
            try:
                nome_arq = f"{server_img_dir}\\{nome_arq}"
                #verificar se o arquivo existe
                #criar comando para mostrar os arquivos que existem
                sucesso = sendFile()