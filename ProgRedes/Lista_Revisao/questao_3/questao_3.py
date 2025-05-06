import random
from functools import reduce

def randomWord(arquivo_palavras: str) -> str:
    """
    Abre o arquivo com as palavras, as adiciona a uma lista e sorteia uma palavra dessa lista
    """
    arch = open(f"{arquivo_palavras}", 'r' )
    palavras = [i[:-1] for i in arch]
    arch.close()
    palavra = random.choice(palavras)
    return palavra

def result(palavra_inserida: str, palavra_correta: str) -> list:
    """
    Verifica quão correta ou errada foi a tentativa e retorna as cores que cada letra da palavra deve ser de acordo com a questão
    """
    palavra_inserida = palavra_inserida.lower()
    palavra_correta = palavra_correta.lower()
    resultado = []
    for i in range(len(palavra_correta)):
        if palavra_inserida[i] == palavra_correta[i]:
            resultado.append(92)
        elif palavra_inserida[i] in palavra_correta:
            resultado.append(93)
        else:
            resultado.append(90)
    return resultado

def inputRequest(requirement: int):
    """
    Repete o pedido te input até uma palavra com a mesma quantidade de letras que a palavra correta tenha
    """
    while True:
        tentativa = input(f"A palavra precisa ter {requirement} letras\nPor favor insira uma palavra valida: ")
        if len(tentativa) == requirement:
            return tentativa
        

def termo():
    """
    Função principal que realiza a maioria dos processos do termoo
    """
    palavra = randomWord("pool_palavras_q3.txt")
    tamanho_palavra = len(palavra)
    correto = 92 * tamanho_palavra
    print(f"A palavra tem {tamanho_palavra} letras")
    for i in range(6, 0, -1):
        tentativa = input(f"Você ainda tem {i} tentativas. Tente adivinhar qual é!!\nDigite sua tentativa: ")
        if len(tentativa) != tamanho_palavra:
            tentativa = inputRequest(tamanho_palavra)
        resultado = result(tentativa, palavra)
        for i in range(len(resultado)):
            print(f"\033[{resultado[i]}m{tentativa[i]}\033[0m", end= ' ')
        print('')
        if reduce(lambda x, y: x + y, resultado) == correto:
            print('Parabéns, você acertou a palavra!!')
            return
    print(f"Infelizmente as tentativas acabaram. A palavra correta era: {palavra}")
    return

termo()
