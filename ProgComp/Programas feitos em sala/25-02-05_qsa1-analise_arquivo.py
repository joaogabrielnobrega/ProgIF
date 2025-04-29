#
# Questão para analizar um arquivo
#       João Gabriel Nóbrega
#
#1) Quantos pedidos houve em cada hora/minuto?
#2) Qual o dia/hora com mais pedidos? 
#3) Houve respostas diferentes do código 200? Quais e quantos? Faca um gráfico de barra com essa informação.
#4) Gere um arquivo com nome "resposta_data.txt" em que cada linha contem a data e o número de pedidos naquela data. Exiba, também, esta informação em um gráfico de linhas.
#5) Qual o IP fez mais pedidos em cada um dos dias do log?
#6) Salve um arquivo com a lista de IPs (um por linha) que fizeram pedidos ao servidor. O nome desse arquivo deve ser "ips.txt"


fd = open("apache_logs.txt", "r")
resposta_data = open("resposta_data.txt", "w")
pedidos_horaMinuto = dict()
respostas = dict()
datas = dict()
diaHora = dict()
ips = dict()

for linha in fd:
    seguementos = linha.split()
    hora_minuto = seguementos[3].split(":")[1] + ":" + seguementos[3].split(":")[2]
    pos1Data = linha.find("[")
    pos2Data = linha.find(":")
    if hora_minuto not in pedidos_horaMinuto: pedidos_horaMinuto[hora_minuto] = 1
    else: pedidos_horaMinuto[hora_minuto] += 1
    if seguementos[8] not in respostas: respostas[seguementos[8]] = 1
    else: respostas[seguementos[8]] += 1
    if linha[pos1Data +1 :pos2Data] not in datas: datas[linha[pos1Data +1 :pos2Data]] = 1
    else: datas[linha[pos1Data +1 :pos2Data]] += 1
    if linha[pos1Data +1 :pos2Data + 3] not in diaHora: diaHora[linha[pos1Data +1 :pos2Data + 3]] = 1
    else: diaHora[linha[pos1Data +1 :pos2Data + 3]] += 1
    if linha[pos1Data +1 :pos2Data] not in ips: ips[linha[pos1Data +1 :pos2Data]] = {seguementos[0]: 1}
    elif seguementos[0] not in ips[linha[pos1Data +1 :pos2Data]]: ips[linha[pos1Data +1 :pos2Data]][seguementos[0]] = 1
    else: ips[linha[pos1Data +1 :pos2Data]][seguementos[0]] += 1

dia_hora = []
for a, b in diaHora.items():
    dia_hora.append((a, b))
diaHora = sorted(dia_hora, key = lambda x: x[1], reverse = True)

print("Pedidos por hora: ", pedidos_horaMinuto) #Q1
print("Dia/hora com mais pedidos: ", diaHora[0][0]) #Q2
print("Respostas: ", respostas) #Q3 Falta o grafico

for a in datas: #Q4
    resposta_data.write(f"{a}: {datas[a]}\n")

print("ips por dia", ips)#Q5
listaIps = []
for a in ips:
    print(len(ips[a]))
    for x, y in ips[a].items():
        listaIps.append([a])
    

'''
ips_dia = {}
for d in datas.keys():
    print(d)
    if d not in ips_dia:
        ips_dia[d] 
    else:
        for b in ips_dia:
            if d == 

for a, b in ips:
''' 

'''
for i in range(len(datas)):
    if 
for a, b in ips.items():
'''

fd.close()
resposta_data.close()
