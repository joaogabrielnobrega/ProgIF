import hashlib
import datetime
from tabulate import tabulate
from time import sleep

def findNonce(dataToHash, bitsToBeZero):
    s = datetime.datetime.now()
    nonce = 0
    while True:
        entrada = nonce.to_bytes(4, 'big') + dataToHash
        hash_resultado = hashlib.sha256(entrada).hexdigest()
        if hash_resultado.startswith('0' * bitsToBeZero):
            tempo = datetime.datetime.now() - s
            return nonce, tempo
        nonce += 1
        if nonce % 100000000 == 0:
            print("100 milhões foi", nonce)
    return

headers=["Transação", "Dificuldade", "Nonce", "Tempo (sec)"]

l = [["Esse é fácil", 8, None, None], 
["Esse é fácil", 10, None, None], 
["Esse é fácil", 15, None, None], 
["Texto maior muda o tempo?", 8, None, None], 
["Texto maior muda o tempo?", 10, None, None], 
["Texto maior muda o tempo?", 15, None, None], 
["É possível calcular esse", 18, None, None], 
["É possível calcular esse", 19, None, None], 
["É possível calcular esse", 20, None, None]]

for i in l:
    data = i[0].encode('utf-8')
    i[2], i[3] = findNonce(data, i[1])
    i[3] = f"{i[3].total_seconds()}"
    if i == l[2]:
        break




arch = open("TabelaResultado.txt", 'a')
arch.write('\n\n')
arch.write(tabulate(l, headers))
arch.close()
