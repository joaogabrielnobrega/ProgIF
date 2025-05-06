def xor_arquivos(arquivo_origem: str, palavra_chave: str, arquivo_destino: str):
    """
    Aplica a operação XOR byte a byte do arquivo de origem com os caracteres da palavra-chave e escreve o resultado em um arquivo de destino.

    """
    try:
        arch_dst_veri = open(arquivo_destino, 'rb')
        arch_dst_veri.close()
        print("Arquivo {arquivo_destino} já existe, escolha outro nome")
        return
    except:
        ...
    try:
        arch_orig = open(arquivo_origem, 'rb')
        arch_dst = open(arquivo_destino, 'wb')
        while True:
            byte_origem = arch_orig.read(1)
            if not byte_origem:
                arch_orig.close()
                arch_dst.close()
                break
            ind_chave = (arch_orig.tell() - 1) % len(palavra_chave)
            byte_chave = ord(palavra_chave[ind_chave])
            byte_xor = byte_origem[0] ^ byte_chave
            arch_dst.write(bytes([byte_xor]))
        
        print(f"Arquivo '{arquivo_destino}' criado com sucesso aplicando a operação XOR.")
        return
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_origem}' não encontrado.")
        return
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return

arquivo_origem = input("Digite o nome do arquivo de origem: ")
palavra_chave = input("Digite a palavra-chave: ")
arquivo_destino = input("Digite o nome do arquivo de destino: ")
xor_arquivos(arquivo_origem, palavra_chave, arquivo_destino)
