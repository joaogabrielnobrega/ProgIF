import random 

#Variaveis que determinam valores necessarios
num_ale = random.randint(1, 100)
mini = 1
maxi = 100

#Variavel que recebe a tentativa do usuario
tenta = int(input(f"Tente advinhar o numero entre {mini} e {maxi}: \n"))

#Condicional para saber se o numero dado pelo usuario está no intervalo determinado
if mini <= tenta <= maxi:
    #Condicional para determinar se a tentativa do usuario é diferente do numero aleatorio e tomar as medidas para as proximas tentativas
    if tenta != num_ale:
        #Condicional que atualiza o intervalo possivel para a proxima tentativa 
        if tenta > num_ale:
            maxi = tenta
        elif tenta < num_ale:
            mini = tenta
        
        #Inicio da proxima tentativa, perguntando ao usuario sua tentativa
        tenta = int(input(f"Tente advinhar o numero entre {mini} e {maxi}: \n"))

        if mini <= tenta <= maxi:
            if tenta != num_ale:
                if tenta > num_ale:
                    maxi = tenta
                elif tenta < num_ale:
                    mini = tenta
                tenta = int(input(f"Tente advinhar o numero entre {mini} e {maxi}: \n"))

                if mini <= tenta <= maxi:
                    if tenta != num_ale:
                        if tenta > num_ale:
                            maxi = tenta
                        elif tenta < num_ale:
                            mini = tenta
                        tenta = int(input(f"Tente advinhar o numero entre {mini} e {maxi}, essa é sua ultima tentativa: \n"))

                        if mini <= tenta <= maxi:
                            if tenta != num_ale:
                                print("Você errou")
                                
                            else:
                                print("Acertou!!")
                        else:
                            print(f"O numero digitado não está entre {mini} e {maxi}")
                    else:
                        print("Acertou!!")
                else:
                    print(f"O numero digitado não está entre {mini} e {maxi}")
            else:
                print("Acertou!!")
        else:
            print(f"O numero digitado não está entre {mini} e {maxi}")
    else:
        #Se o numero escolhido pelo usuario igual ao numero aleatorio a função exibira a mensagem
        print("Acertou!!")
else:
    #Caso o numero escolhido pelo usuario não estiver no intervalo a função mostrará a mensagem no console
    print(f"O numero digitado não está entre {mini} e {maxi}")