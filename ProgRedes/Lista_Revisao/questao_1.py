import json
import datetime

def decToBin(n: str) -> str:
    if not isinstance(n, str):
        return False
    if 0 > int(n) > 255:
        return False
    return f"{int(n):08b}"

def binToDec(bine: str) -> str:
    '''
    Transforma um numero binario recebido, como string, em seu equivalente em decimal, tambem como string. 
    '''
    if not isinstance(bine, str):
        return False
    dec = 0
    weigth = range(len(bine) - 1, -1, -1)
    for i in range(len(bine)):
        dec += int(bine[i]) * (2 ** weigth[i])
    return str(dec)

def validateIP(ip: str):
    '''
    Verifica se um ip fornecido, como string, é valido
    '''
    if not isinstance(ip,str):
        return False
    octetos = ip.split('.')
    if len(octetos) < 4:
        return False
    for octeto in octetos:
        if 0 <= int(octeto) <= 255:
            continue
        else:
            return False
    return True

def webMask(mask: int) -> list:
    '''
    Transforma uma mascara de sub-rede CIDR em seu formato binario
    '''
    if not isinstance(mask, int):
        return False
    mask_bin = ''
    mask_bin += '1' * (mask)
    mask_bin += '0' * (32 - mask)
    
    oct_mask = [mask_bin[i: i + 8] for i in range(0, 32, 8)]
    mask_bin = '.'.join(oct_mask)
    mask_dec = '.'.join([binToDec(i) for i in oct_mask])
    return mask_bin, mask_dec, oct_mask

def ipDecToBin(ip: str) -> str:
    '''
    Tranforma um IP de sua forma em decimal para seu equivalente em binario
    '''
    if not isinstance(ip, str):
        return False
    octetos = ip.split('.')
    ip_bin = '.'.join([decToBin(i) for i in octetos])
    return ip_bin

def enderecoRede(ip: str, mask: str) -> tuple:
    '''
    Recebe um IP e uma mascara de sub-rede e retorna o endereço da rede referente a esses dois
    '''
    if not isinstance(ip, str) or not isinstance(mask, str):
        return False
    octetos_ip = ip.split('.')
    octetos_mask = mask.split('.')
    ip = [int(i) for i in octetos_ip]
    mask = [int(i) for i in octetos_mask]
    ip_rede = '.'.join(list(map(lambda x, y: str(x & y), ip, mask)))
    bin_ip_rede = ipDecToBin(ip_rede)
    return bin_ip_rede, ip_rede

def firstHost(ip_rede: str):
    octetos_ip = ip_rede.split('.')
    host = '.'.join(octetos_ip[:-1]) + f".{int(octetos_ip[-1]) + 1}"
    return host

def lastHost(ip_rede: str, mask: int):
    host = ''.join(ip_rede.split('.'))[:mask] + '1' * (32 - mask)
    broadcast = '.'.join([binToDec(host[i:i + 8]) for i in range(0, 32, 8)])
    last_host = '.'.join(broadcast.split('.')[:-1]) + f".{int(broadcast.split('.')[-1]) - 1}"
    num_host = (2 ** (32 - mask)) - 2
    return last_host, broadcast, num_host

user_ip = input('Digite o endereço IP: ')
first_mask = int(input('Digite a máscara de rede inicial (CIDR): '))
last_mask = int(input('Digite a máscara de rede final (CIDR): '))
resultado = {}

for mask in range(first_mask, last_mask + 1):
    masks = webMask(mask)
    ips_rede = enderecoRede(user_ip, masks[1])
    ho_bro = lastHost(ips_rede[0], mask)
    print(f"\nEndereco de rede: {ips_rede[1]}")
    print(f"Primeiro host: {firstHost(ips_rede[1])}")
    print(f"Ultimo host: {ho_bro[0]}")
    print(f"Broadcast: {ho_bro[1]}")
    print(f"Mascara de sub-rede decimal: {masks[1]}")
    print(f"Mascara de sub-rede binario: {masks[0]}")
    print(f"Numero de hosts: {ho_bro[2]}")
    resultado[f"/{mask}"] = {"Endereco de rede" : f"{ips_rede[1]}", "Primeiro host" : f"{firstHost(ips_rede[1])}", "Ultimo host" : f"{ho_bro[0]}", "Broadcast" : f"{ho_bro[1]}", "Mascara de sub-rede decimal" : f"{masks[1]}", "Mascara de sub-rede binario" : f"{masks[0]}", "Numero de hosts" : f"{ho_bro[2]}"}
    print("")

date = datetime.datetime.now()
end = {f'{str(date)}': resultado}
arch = open("calcjson.txt", 'a')
arch.write("\n")
arch.write(json.dumps(end, indent=3))
arch.close()
