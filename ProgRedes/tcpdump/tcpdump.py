'''

usar tabulate

Desenvolva um programa que leia um arquivo capturado pelo tcpdump (alguns exemplos estão
disponibilizados no assignment do Github Classroom) e responda:
a) Mostre o conteúdo de cada um dos campos nos headers dos pacotes IP capturados
(vide https://pt.wikipedia.org/wiki/Protocolo_de_Internet);
b) Em que momento inicia/termina a captura de pacotes?///--
c) Qual o tamanho do maior TCP pacote capturado? ////--
d) Há pacotes que não foram salvos nas suas totalidades? Quantos?////---
e) Qual o tamanho médio dos pacotes UDP capturados? ///// ---
f) Qual o par de IP com maior tráfego entre eles? ///// ---
g) Com quantos outros IPs o IP da interface capturada interagiu?

ATENÇÃO:
NÃO é permitido usar bibliotecas não nativamente incorporadas ao Python

arquivo inteiro
    
    ler header do arquivo
    
    ler header do pacote
        capturar tamanho do pacote capturado
        
    analisar pacote a pacote
        
            capturar Protocolo
            capturar tamanho original do pacote
            capturar IP origem
            capturar IP dst
'''

from datetime import datetime, timezone

def readFile(file: str):
    arch = open(file, 'rb')
    data = []
    
    file_header = readFileHeader(arch)
    print(file_header)
    n = 0
    while n < 5:
        packet_record = readPacketRecord(arch)
        print(packet_record)
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
    '''splited_record['timestamp'] = file.read(4)
    splited_record['timestamp_m'] = file.read(4)
    splited_record['captured_legth'] = file.read(4)
    splited_record['original_legth'] = file.read(4)'''
    full_record = file.read(16)
    splited_record['timestamp'] = full_record[4]
    splited_record['timestamp_m'] = full_record[4 : 8]
    splited_record['captured_legth'] = full_record[8 : 12]
    splited_record['original_legth'] = full_record[12 : 16]
    return splited_record
    

def readPacket(file, size: int):
    split_packet = {}
    split_packet['frame header'] = file.read(14)
    #split_packet['ip header'] = file.read(24)
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
    split_packet['options'] = file.read(4)
    print(size)
    packet = file.read(size - 38)
    '''split_packet = {}
    split_packet['frame header'] = packet[14]
    #split_packet['ip header'] = packet[14 : 38]
    split_packet['ver/hlen'] = packet[14: 15]
    split_packet['tos'] = packet[15 : 16]
    split_packet['total legth'] = packet[16 : 18]
    split_packet['identification'] = packet[18 : 20]
    split_packet['fragment offset'] = packet[20 : 22]
    split_packet['ttl'] = packet[22 : 23]
    split_packet['protocol'] = packet[23 : 24]
    split_packet['checksum'] = packet[24 : 26]
    split_packet['ip origem'] = packet[26 : 30]
    split_packet['ip destino'] = packet[30 : 34]
    split_packet['options'] = packet[34 : 38]'''
    return split_packet


def treatingData(data: dict, file_header: dict):
    tcp_packet_size = 0
    udp_packet_size = 0
    udp_packet_count = 0
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
        
        try:
            packets_per_connection[f'{i[1]["ip origem"]}-{i[1]["ip destino"]}'] += 1
        except:
            try:
                packets_per_connection[f'{i[1]["ip destino"]}-{i[1]["ip origem"]}'] += 1
            except:
                packets_per_connection[f'{i[1]["ip origem"]}-{i[1]["ip destino"]}'] = 1
            
        
        '''if not packets_per_connection[f'{i[1]["ip origem"]}-{i[1]["ip destino"]}']:
            if not packets_per_connection[f'{i[1]["ip destino"]}-{i[1]["ip origem"]}']:
                packets_per_connection[f'{i[1]["ip destino"]}-{i[1]["ip origem"]}'] = 1
            else:
                packets_per_connection[f'{i[1]["ip destino"]}-{i[1]["ip origem"]}'] += 1
        else: 
            packets_per_connection[f'{i[1]["ip origem"]}-{i[1]["ip destino"]}'] += 1'''
        
        
        if i[1]['protocol'] == '\x11':
            udp_packet_size += int(i[0]['captured_legth'])
            udp_packet_count += 1
        
        if i[0]['captured_legth'] < i[0]['original_legth']:
            packet_unfool += 1
        
        if time_type:
            time = int.from_bytes(i[0]["timestamp"], "big", signed=True) + (int.from_bytes(i[0]["timestamp_m"], "big", signed=True) / 1000000) #micro
        else:
            time = int.from_bytes(i[0]["timestamp"], "big", signed=True) + (int.from_bytes(i[0]["timestamp_m"], "big", signed=True) / 1000000000) #nano
        if time < first_packet:
            first_packet = time
        if time > last_packet:
            last_packet = time
    
    start_of_capture = datetime.fromtimestamp(first_packet, timezone.utc)
    end_of_capture = datetime.fromtimestamp(last_packet, timezone.utc)
    
    most_packets = ['', 0]
    
    for i, b in packets_per_connection.items:
        if b > most_packets[1]:
            most_packets = [i,b]
    
    medium_udp_packet = udp_packet_size / udp_packet_count
    
    
    return start_of_capture, end_of_capture, tcp_packet_size, packet_unfool, medium_udp_packet, most_packets

def main():
    file = input("Arquivo a ser lido: ")
    file_information = readFile(file)
    print(treatingData(file_information[0], file_information[1]))

main()
