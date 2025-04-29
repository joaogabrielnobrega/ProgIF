#Codigo para informar qual o dia do ano da data informada

#Variaveis que perguntam ao usuario a data que ele quer saber qual o dia do ano
dia = int(input("Insira o dia: "))
mes = int(input("Insira o mes como um numero: "))
ano = int(input("Insira o ano: "))
dia_do_ano = 0
dia_valido = True
mes_valido = True

#Variaveis para contas
mes4 = 30 
mes6 = 30
mes9 = 30 
mes11 = 30
mes1 = 31 
mes3 = 31 
mes5 = 31 
mes7 = 31 
mes8 = 31 
mes10 = 31 
mes12 = 31

#Variaveis para saber se o ano é bissexto
ano_bi1 = ano % 400
ano_bi2 = ano % 4
ano_bi3 = ano % 100

#Condicionais para saber se a data informada é valida
if mes > 12:
    mes_valido = False
    print("\nMês invalido")

if ano_bi1 == 0 or ano_bi2 == 0 and ano_bi3 != 0:
    #Variavel para calculo
    mes2 = 29
    if mes == 2:
        if dia > 29:
            dia_valido = False
            print("\nDia invalido")
            
else:
    #Variavel para calculo
    mes2 = 28
    if mes == 2:
        if dia > 28:
            dia_valido = False
            print("\nDia invalido")
    
if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia > 30:
        dia_valido = False
        print("\nDia invalido")
        
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia > 31:
        dia_valido = False
        print("\nDia invalido")


#Condicionais para descobrir qual calculo usar para saber o dia do ano
if dia_valido and mes_valido:
    if mes == 1:
        dia_do_ano = dia

    if mes == 2:
        dia_do_ano = mes1 + dia

    if mes == 3:
        dia_do_ano = mes1 + mes2 + dia

    if mes == 4:
        dia_do_ano = mes1 + mes2 + mes3 + dia

    if mes == 5:
        dia_do_ano = mes1 + mes2 + mes3 + mes4 + dia

    if mes == 6:
        dia_do_ano = mes1 + mes2 + mes3 + mes4 + mes5 + dia

    if mes == 7:
        dia_do_ano = mes1 + mes2 + mes3 + mes4 + mes5 + mes6 + dia

    if mes == 8:
        dia_do_ano = mes1 + mes2 + mes3 + mes4 + mes5 + mes6 + mes7 + dia

    if mes == 9:
        dia_do_ano = mes1 + mes2 + mes3 + mes4 + mes5 + mes6 + mes7 + mes8 + dia

    if mes == 10:
        dia_do_ano = mes1 + mes2 + mes3 + mes4 + mes5 + mes6 + mes7 + mes8 + mes9 + dia    

    if mes == 11:
        dia_do_ano = mes1 + mes2 + mes3 + mes4 + mes5 + mes6 + mes7 + mes8 + mes9 + mes10 + dia

    if mes == 12:
        dia_do_ano = mes1 + mes2 + mes3 + mes4 + mes5 + mes6 + mes7 + mes8 + mes9 + mes10 + mes11 +dia
    
    print(f"\nA data informada é o dia {dia_do_ano} do ano")

else:
    print("Escolha uma data valida")