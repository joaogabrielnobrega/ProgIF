#   João Gabriel Nóbrega Santos
#               20242014050013
#
## Jogo termo(www.term.ooo) dueto com 7 tentativas

import random

#variavel que contem as palavras validas para o jogo, fornecida pela atividade.
palavras = (
    "ADAGA", "ADUBO", "AMIGO", "ANEXO", "ARAME", "ARARA", "ARROZ",
    "ASILO", "ASTRO", "BAILE", "BAIXA", "BALAO", "BALSA", "BARCO",
    "BARRO", "BEIJO", "BICHO", "BORDA", "BORRA", "BRAVO", "BREJO",
    "BURRO", "CAIXA", "CALDO", "CANJA", "CARRO", "CARTA", "CERVO",
    "CESTA", "CLIMA", "COBRA", "COLAR", "COQUE", "COURO", "CRAVO",
    "DARDO", "FAIXA", "FARDO", "FENDA", "FERRO", "FESTA", "FLUOR",
    "FORCA", "FORNO", "FORTE", "FUNDO", "GAITA", "GARRA", "GENIO",
    "GESSO", "GRADE", "GRANA", "GRAMA", "GURIA", "GREVE", "GRUTA",
    "HEROI", "HOTEL", "ICONE", "IMPAR", "IMUNE", "INDIO", "JUNTA",
    "LAPIS", "LARVA", "LAZER", "LENTO", "LESTE", "LIMPO", "LIVRO",
    "MACIO", "MAGRO", "MALHA", "MANSO", "MARCO", "METAL", "MORTE",
    "MORRO", "MURAL", "MOVEL", "NACAO", "NINHO", "NOBRE", "NORMA",
    "NORTE", "NUVEM", "PACTO", "PALHA", "PARDO", "PARTE", "PEDRA",
    "PEDAL", "PEIXE", "PRADO", "PISTA", "POMBO", "POETA", "PONTO",
    "PRATO", "PRECO", "PRESO", "PROSA", "PRUMO", "PULGA", "PULSO",
    "QUEPE", "RAIVA", "RISCO", "RITMO", "ROSTO", "ROUPA", "SABAO",
    "SALTO", "SENSO", "SINAL", "SITIO", "SONHO", "SOPRO", "SURDO",
    "TARDE", "TERNO", "TERMO", "TERRA", "TIGRE", "TINTA", "TOLDO",
    "TORRE", "TRAJE", "TREVO", "TROCO", "TRONO", "TURMA", "URUBU",
    "VALSA", "VENTO", "VERDE", "VISAO", "VINHO", "VIUVO", "ZEBRA"
)
# uma das regras era "somente aceite como entrada as palavras listadas no arquivo que acompanha essa atividade", -
# -mas eu não sabia se deveria mostrar as palavras que poderiam ser usadas na tentativa. -
# -por via das duvida eu o fiz.

print("\nEssas são as possiveis palavras para se tentar: \n", palavras)

#variaveis que escolhem uma palavra do pool para cada variavel.
palavra1 = random.choice(palavras)
palavra2 = random.choice(palavras)

#print(palavra1)
#print(palavra2)

#variavel que conterá se a palavra ainda não foi advinhada ainda.
tentando_palavra1 = True
tentando_palavra2 = True

#variavel contadora de tentativas.
tentativa = 1

while tentativa <= 7:
    #condicional que pergunta ao usuario sua proxima tentativa se uma das palavras ainda não foi advinhada. -
    # - alem de mostrar uma mensagem e parar o laço de repetição se o usuario advinhou as duas palavras.
    if tentando_palavra1 or tentando_palavra2:
            palavra_tentativa = input("\nDigite sua tentativa, toda em caixa alta(Capslock) e parte das palavras possiveis: ")
    else:
        print("Você acertou as duas palavras. Parabens!")
        tentativa += 10
    
    if palavra_tentativa in palavras:
        #variavel contadora do indice da letra
        letra = 0
        #laço para verificar cada letra se se ela esta no lugar correto, se apenas exite na primeira palavra ou se -
        #- nem existe na primeira palavra e mostrar o resultado de acordo com as regras do jogo termo.
        while tentando_palavra1 and letra < len(palavra1):
            if palavra_tentativa[letra] == palavra1[letra]:
                print(f"\033[1;37;42m{palavra_tentativa[letra]}\033[m", end="")
            elif palavra_tentativa[letra] in palavra1:
                print(f"\033[1;37;43m{palavra_tentativa[letra]}\033[m", end="")
            else: print(palavra_tentativa[letra], end="")
            if letra == len(palavra1) - 1 and  palavra_tentativa == palavra1:
                tentando_palavra1 = False
            letra += 1

        #variavel contadora do indice da letra
        letra = 0
        
        #função para pular uma linha e mostrar o resultado da segunda palavra nessa proxima linha.
        print("")
        
        #laço para verificar cada letra se se ela esta no lugar correto, se apenas exite na segunda palavra ou se- 
        # -nem existe na segunda palavra e mostrar o resultado de acordo com as regras do jogo termo.
        while tentando_palavra2 and letra < len(palavra2):
            if palavra_tentativa[letra] == palavra2[letra]:
                print(f"\033[1;37;42m{palavra_tentativa[letra]}\033[m", end="")
            elif palavra_tentativa[letra] in palavra2:
                print(f"\033[1;37;43m{palavra_tentativa[letra]}\033[m", end="")
            else: print(palavra_tentativa[letra], end="")
            if letra == len(palavra2) - 1 and palavra_tentativa == palavra2:
                tentando_palavra2 = False
            letra += 1
        
        #função para pular uma linha e mostrar o resultado da primeira palavra e as proximas mensagens nessa-
        # -proxima linha.
        print("")
        tentativa += 1
    else:
        print("Palavra invalida. Por favor digite uma tentativa valida")