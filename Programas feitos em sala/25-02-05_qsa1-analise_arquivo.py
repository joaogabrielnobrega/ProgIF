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
respostas_data = open("respostas_data.txt", "w")
pedidos_horaMinuto = dict()
respostas = dict()

for linha in fd:
    seguementos = linha.split()
    #print(seguementos[3])
    hora_minuto = seguementos[3].split(":")[1] + seguementos[3].split(":")[2]
    #print(hora_minuto)
    if hora_minuto not in pedidos_horaMinuto: pedidos_horaMinuto[hora_minuto] = 1
    else: pedidos_horaMinuto[hora_minuto] += 1
    if seguementos[8] not in respostas: respostas[seguementos[8]] = 1
    else: respostas[seguementos[8]] += 1
x = list()
for a, b in pedidos_horaMinuto.items():
    x.append((a, b))
x.sort(reversed = True, key = lambda v: v[1])
print(x)
print(pedidos_horaMinuto)
print(respostas)



fd.close()
respostas_data.close()
