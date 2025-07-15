import os, socket

from constantes import *

os.makedirs(client_img_dir, exist_ok=True)

tcp_sock = socket.socket(socket.AF_NET, socket.SOCK_STREAM)

tcp_sock.connect(host_server_ip, host_port)

while True:

    mensagem = input("Digite o comando: ").lower().strip()

    if mensagem == 'exit': break

    tcp_sock.send(mensagem.encode(page_code))

    reply = tcp_sock.recv(buffer_size)
    str_reply = reply.decode(page_code)

    if '|' in str_reply and not str_reply.lower().startswith("erro"):
        nome_arq, tam_arq = str_reply.split("|")
        tam_arq = int(tam_arq)

        print(f"Recebendo arquivo {nome_arq}, de tamanho {tam_arq} bytes")

        bytes_recebidos = 0
        arch_recebendo = open(f"{client_img_dir}\\{nome_arq}", "wb")
        while bytes_recebidos < tam_arq:
            bytes_reply = tcp_sock.recv(buffer_size)
            arch_recebendo.write(bytes_reply)
            bytes_recebidos += len(bytes_reply)
        
        print(f"Arquivo {nome_arq} recebido e salvo em {client_img_dir}.")
        
    else:
        print(str_reply)

tcp_sock.close()
    