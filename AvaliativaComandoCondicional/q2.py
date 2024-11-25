#Codigo para calcular a nota de aluno do IFRN e verificar se foi aprovado em uma disciplina

#Variaveis que pedem a nota dos bimestre ao usuario
nota_b1 = float(input("Insira sua nota no primeiro bimestre: \n"))
nota_b2 = float(input("Insira sua nota no segundo bimestre: \n"))

#Variavel que recebe a media do usuario de acordo com a nota recebida
media = ((2 * nota_b1) + (3 * nota_b2))/ 5
situacao = ""

#Condicionais para atualizar a variavel situação
if media >= 60:
    situacao = "aprovado"
    print("\nEssa é sua media: ", media)

if media < 20:
    situacao = "reprovado"
    print("\nEssa é sua media: ", media)

#Condicional para o usuario que precise e possa prestar a prova final para saber se passará com ela
if 20 <= media < 60:
    situacao = "em prova final"
    print(f"\nVocê está {situacao}")
    
    #Variavel que pergunta ao usuario sua nota na prova final
    nota_final = float(input("Insira sua nota na prova final: \n "))
    
    #Variaveis que recebem o resultado dos calculos da media final
    media_final1 = (media + nota_final) / 2
    media_final2 = ((2 * nota_final)+(3 * nota_b2))/5
    media_final3 = ((2 * nota_b1) + (3 * nota_final))/5
    
    #Condicional para determinar se o usuario passou com a nota da prova final 
    if media_final1 >= 60 or media_final2 >= 60 or media_final3 >= 60:
        situacao = "aprovado"
    else:
        situacao = "reprovado"
    
    #Funções para teste 
    #print(f"mf1: {media_final1}")
    #print(f"mf2: {media_final2}")
    #print(f"mf3: {media_final3}")
    
    #Condicional para determinar a maior media final e exibila no console 
    if media_final1 > media_final2:
        if media_final1 > media_final3:
            print("Essa é sua media: ", media_final1)
        else:
            print("Essa é sua media: ", media_final3)
    elif media_final2 > media_final3:
        print("Essa é sua media: ", media_final2)
    else:
        print("Essa é sua media: ", media_final3)
        
    
#Função para exibir se o usuario passou ou reprovou na disciplina
print(f"Você foi {situacao} nessa materia")
