# Codigo para descobrir quanto é necessario para passar de ano no IFRN

t1 = float(input("Insira quanto você tirou no trabalho do 1º bimestre: "))
p1 = float(input("Insira quanto você tirou na prova do 1º bimestre: "))
t2 = float(input("Insira quanto você tirou no trabalho do 2º bimestre: "))

media_1 = ((t1 * 30) + (p1 * 70)) / 100
media = 60
p2 = (((((media*5)-(media_1 * 2)) / 3) * 100) - (t2*30)) / 70


########### teste #############
#p22 = float(input("Insira quanto você tirou na prova do 2º bimestre"))
#media_2 = ((media*5)-(media_1 * 2)) / 3
#media_22 = ((t2 * 3) + (p22 * 7))/10 
#media_f = ((media_1 * 2) + (media_22 * 3))/ 5
########### fim teste ############

#teste# media_2 = ((t2 * 30) + (p2 * 70)) / 100

########## Primeira tentativa ###########
#6 = (media_1 * 40) + (((t2 * 30) + (p2 * 70)/100) * 60)/ 100
#6 * 100   = (media_1 * 40) + (((t2 * 30) + (p2 * 70)/100) * 60)
#(((6*100)*60)*40) = media_1 + ((t2 * 30) + (p2*70)/100)
#((((6*100)*60)*40)*100) = media_1 + (t2 * 30) + (p2*70)
#((((((6*100)*60)*40)*100)*70)- media_1) - (t2*30) 
#p2 = ((((((6*100)*60)*40)*100)*70)- media_1) - (t2*30) 
#p2 = ((media_1 * 40) + ((((t2 * 30) + (p2 * 70))/100) * 60))/ 100
########## fim tentativa ###########

########## segunda tentativa ###########
#6 = ((media_1 * 40) + ((((t2 * 30) + (p2 * 70))/100) * 60))/ 100
#6*100 = ((media_1 * 40) + ((((t2 * 30) + (p2 * 70))/100) * 60))
#6*100-(media *40) = ((((t2 * 30) + (p2 * 70))/100) * 60)
#((6*100-(media *40))/60) = (((t2 * 30) + (p2 * 70))/100
#(((6*100-(media *40))/60)*100) = ((t2 * 30) + (p2 * 70))
#((((6*100-(media *40))/60)*100)- (t2 * 30)) = (p2 * 70)
#p2 = (((((60*10-(media_1 *40))/60)*10)- (t2 * 3))/7) * -1
#p3 = ((media_1 * 2) + ((((t2 * 3) + (p2 * 7))/10) * 3))/ 5
########## fim tentativa ###########

############# Ultima tentativa ##########
#((t2 * 30) + (p2 * 70))/100 = ((media*5)-(media_1 * 2)) / 3
#(t2 * 30) + (p2 * 70) = ((((media*5)-(media_1 * 2)) / 3) * 100)
#(p2 * 70) = ((((media*5)-(media_1 * 2)) / 3) * 100) - (t2*30)
#p2 = (((((media*5)-(media_1 * 2)) / 3) * 100) - (t2*30)) / 70
########## FIM tentativa ###########

############ teste #########
#print(f"media 1 {media_1}")
#print(f"media 2: {media_22}")
#print(f"media final: {media_f}")
########### teste ###############

print(f"Você precisa de {p2} pontos na prova para passar na disciplina")
