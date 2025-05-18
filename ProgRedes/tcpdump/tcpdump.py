'''

a) Mostre o conteúdo de cada um dos campos nos headers dos pacotes IP capturados
(vide https://pt.wikipedia.org/wiki/Protocolo_de_Internet);
b) Em que momento inicia/termina a captura de pacotes?///--
c) Qual o tamanho do maior TCP pacote capturado? ////--
d) Há pacotes que não foram salvos nas suas totalidades? Quantos?////---
e) Qual o tamanho médio dos pacotes UDP capturados? ///// ---
f) Qual o par de IP com maior tráfego entre eles? ///// ---
g) Com quantos outros IPs o IP da interface capturada interagiu? ////

ATENÇÃO:
NÃO é permitido usar bibliotecas não nativamente incorporadas ao Py

'''

from datetime import datetime, timezone
from tabulate import tabulate

def readFile(file: str):
    arch = open(file, 'rb')
    data = []
    
    file_header = readFileHeader(arch)
    
    n = 0
    while n < 5:
        packet_record = readPacketRecord(arch)
        packet_data = readPacket(arch, int.from_bytes(packet_record['captured_legth'], "little", signed=True))
        data.append((packet_record, packet_data))
        
        n += 1
    
    arch.close()
    return data, file_header

def readFileHeader(file):
    split_fileHeader = {}
    split_fileHeader["magic number"] = file.read(4)
    split_fileHeader["rest"] = file.read(20)
    return split_fileHeader

def readPacketRecord(file):
    splited_record = {}
    splited_record['timestamp'] = file.read(4)
    splited_record['timestamp_m'] = file.read(4)
    splited_record['captured_legth'] = file.read(4)
    splited_record['original_legth'] = file.read(4)
    return splited_record
    

def readPacket(file, size: int):
    split_packet = {}
    split_packet['frame header'] = file.read(14)
    split_packet['ver/hlen'] = file.read(1)
    split_packet['tos'] = file.read(1)
    split_packet['total legth'] = file.read(2)
    split_packet['identification'] = file.read(2)
    split_packet['fragment offset'] = file.read(2)
    split_packet['ttl'] = file.read(1)
    split_packet['protocol'] = file.read(1)
    split_packet['checksum'] = file.read(2)
    split_packet['ip origem'] = file.read(4)
    split_packet['ip destino'] = file.read(4)
    packet = file.read(size - 34)
    return split_packet


def treatingData(data: dict, file_header: dict):
    tcp_packet_size = 0
    udp_packet_size = 0
    udp_packet_count = 0
    medium_udp_packet = 0
    packets_unfool = 0
    packets_per_connection = {}
    first_packet = 1000000000000000
    last_packet = 0
    time_type = ''
    if file_header["magic number"] == "\xd4\xc3\xb2\xa1":
        time_type = True
    elif file_header["magic number"] == "\xd4\x3c\xb2\xa1":
        time_type = False
    for i in data:
        if i[1]['protocol'] == '\x06' and i[0]['captured_legth'] > tcp_packet_size: 
            tcp_packet_size = i[0]['captured_legth']
        
        
        ip_origem = '.'.join([str(a) for a in i[1]["ip origem"]])
        ip_destino = '.'.join([str(a) for a in i[1]["ip destino"]])
        
        try:
            packets_per_connection[f'{ip_origem}-{ip_destino}'] += 1
        except:
            try:
                packets_per_connection[f'{ip_destino}-{ip_origem}'] += 1
            except:
                packets_per_connection[f'{ip_destino}-{ip_origem}'] = 1
        
        
        if i[1]['protocol'] == '\x11':
            udp_packet_size += int.from_bytes(i[0]['captured_legth'], 'little')
            udp_packet_count += 1
        
        if i[0]['captured_legth'] < i[0]['original_legth']:
            packets_unfool += 1
        
        if time_type:
            time = int.from_bytes(i[0]["timestamp"], "big", signed=True) + (int.from_bytes(i[0]["timestamp_m"], "big", signed=True) / 1000000) #micro
        else:
            time = int.from_bytes(i[0]["timestamp"], "little", signed = True) + (int.from_bytes(i[0]["timestamp_m"], "little", signed=True) / 1000000000) #nano
        
        if time < first_packet:
            first_packet = time
        if time > last_packet:
            last_packet = time
    
    start_of_capture = datetime.fromtimestamp(first_packet, timezone.utc)
    end_of_capture = datetime.fromtimestamp(last_packet, timezone.utc)
    
    most_packets = ['', 0]
    
    for i, b in packets_per_connection.items():
        if b > most_packets[1]:
            most_packets = [i,b]
    
    if udp_packet_count > 0:
        medium_udp_packet = udp_packet_size / udp_packet_count
    
    return start_of_capture, end_of_capture, tcp_packet_size, packets_unfool, medium_udp_packet, most_packets

def main():
    file = input("Arquivo a ser lido: ")
    file_information = readFile(file)
    data = treatingData(file_information[0], file_information[1])
    ip_headers = []
    for a in file_information[0]:
        ip_headers.append(a[1].values())
    print(tabulate(ip_headers, headers=file_information[0][0][1].keys()))
    print(f'Começo da captura: {data[0]}\nFim da captura: {data[1]}')
    print(f'Tamanho do maior pacote TCP capturado: {data[2]}')
    print(f'Numero de pacotes que não foram salvos por inteiro: {data[3]}')
    print(f'Tamanho medio de pacotes UDP capturados: {data[4]}')
    print(f'Conexão com maior numero de pacotes: {data[5]}')
    return

main()
