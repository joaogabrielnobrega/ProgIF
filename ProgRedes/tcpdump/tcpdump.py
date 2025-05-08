'''

usar tabulate

Desenvolva um programa que leia um arquivo capturado pelo tcpdump (alguns exemplos estão
disponibilizados no assignment do Github Classroom) e responda:
a) Mostre o conteúdo de cada um dos campos nos headers dos pacotes IP capturados
(vide https://pt.wikipedia.org/wiki/Protocolo_de_Internet);
b) Em que momento inicia/termina a captura de pacotes?
c) Qual o tamanho do maior TCP pacote capturado?
d) Há pacotes que não foram salvos nas suas totalidades? Quantos?
e) Qual o tamanho médio dos pacotes UDP capturados?
f) Qual o par de IP com maior tráfego entre eles?
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

def readFile(file: str):
    arch = open(file, 'rb')
    data = []
    
    file_header = readFileHeader(arch)
    n = 0
    while n < 5:
        packet_record = readPacketRecord(arch)
        packet_data = readPacket(arch, packet_record['captured_legth'])
        data.append(packet_data)
        data.append(packet_record)
        
        n += 1
    
    arch.close()
    return data

def readFileHeader(file: ):
    return file.read(24)

def readPacketRecord(file: ):
    full_record = file.read(16)
    splited_record = {}
    splited_record['timestamp'] = full_record[4]
    splited_record['timestamp_m'] = full_record[4 : 8]
    splited_record['captured_legth'] = full_record[8 : 12]
    splited_record['original_legth'] = full_record[12 : 16]
    return splited_record
    

def readPacket(file: ,size: int):
    packet = file.read(size)
    split_packet = {}
    split_packet['frame header'] = packet[14]
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
    split_packet['options'] = packet[34 : 38]
    return readPacket
