#   João Gabriel Nóbrega Santos
#               20242014050013
#
#   Programa para calcular quantos dias e sabados se passaram desde 27/04/1968 até hoje

import datetime

#variaveis para conseguir a data de hoje e desmembra-las nos valores necessarios
date = datetime.datetime.today()
dia = date.day
mes = date.month
ano = date.year

#variaveis com a data informada anteriormente 
#27/04/1968
dia_anterior = 27
mes_anterior = 4
ano_anterior = 1968

#variaveis dos meses de um ano e quantos dias cada um tem
mes1 = 31
mes2 = 28
mes3 = 31
mes4 = 30
mes5 = 31
mes6 = 30
mes7 =31
mes8 =31
mes9 = 30
mes10 =31
mes11 = 30
mes12 = 31

#variavel que terá o resultado ao fim do codigo
dias_totais = 0

#condicional que atualiza quantos dias o mês de fevereiro tem se o ano anterior for bisexto
if ano_anterior % 4 == 0 or ano_anterior % 400 == 0 and ano_anterior % 100 != 0:
    mes2 = 29

#condicionais que adicionam os dias até o fim do mes da data informada ao total de dias
if dia_anterior <= 31 and mes_anterior == 1 or mes_anterior == 3 or mes_anterior == 5 or mes_anterior == 7 or mes_anterior == 8 or mes_anterior == 10 or mes_anterior == 12:
    dias_totais += 31 - dia_anterior
    
if dia_anterior <= 30 and mes_anterior == 4 or mes_anterior == 6 or mes_anterior == 9 or mes_anterior == 11:
    dias_totais += 30 - dia_anterior

#condicionais que adicionam os dias dos meses restantes do ano ao total de dias 
if dia_anterior <= 31 and mes_anterior == 1:
    dias_totais += mes2 + mes3 + mes4 + mes5 + mes6 + mes7 + mes8 + mes9 + mes10 + mes11 + mes12

if dia_anterior <= 29 and mes_anterior == 2:
    dias_totais += mes3 + mes4 + mes5 + mes6 + mes7 + mes8 + mes9 + mes10 + mes11 + mes12

if dia_anterior <= 31 and mes_anterior == 3:
    dias_totais += mes4 + mes5 + mes6 + mes7 + mes8 + mes9 + mes10 + mes11 + mes12

if dia_anterior <= 30 and mes_anterior == 4:
    dias_totais += mes5 + mes6 + mes7 + mes8 + mes9 + mes10 + mes11 + mes12

if dia_anterior <= 31 and mes_anterior == 5:
    dias_totais += mes6 + mes7 + mes8 + mes9 + mes10 + mes11 + mes12

if dia_anterior <= 30 and mes_anterior == 6:
    dias_totais += mes7 + mes8 + mes9 + mes10 + mes11 + mes12

if dia_anterior <= 31 and mes_anterior == 7:
    dias_totais += mes8 + mes9 + mes10 + mes11 + mes12

if dia_anterior <= 31 and mes_anterior == 8:
    dias_totais += mes9 + mes10 + mes11 + mes12

if dia_anterior <= 30 and mes_anterior == 9:
    dias_totais += mes10 + mes11 + mes12

if dia_anterior <= 31 and mes_anterior == 10:
    dias_totais += mes11 + mes12

if dia_anterior <= 30 and mes_anterior == 11:
    dias_totais += mes12

##condicional inutil, estava copiando/colando e atualizando as condicionais e fiz esse no automatico. Resolvi deixar, efeito na performance é ignoravel 
if dia_anterior <= 31 and mes_anterior == 12:
    dias_totais += 0

#variavel contadora 
anterior = ano_anterior + 1

#laço que adiciona os dias de cada ano passado até 1 ano anterior ao atual
while anterior < ano:
    if anterior % 400 == 0 or anterior % 4 == 0 and anterior % 100 != 0:
        dias_totais += 366
    else:
        dias_totais += 365
    anterior += 1

#condicional que atualiza quantos dias o mês de fevereiro tem se o ano atual for bisexto
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    mes2 = 29
else: mes2 = 28

#condicionais que adicionam os dias do inicio do mes até data de hoje ao total de dias
if dia <= 31 and mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    dias_totais += dia
    
if dia <= 30 and mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dias_totais += dia

##condicional inutil, estava copiando/colando e atualizando as condicionais e fiz esse no automatico. Resolvi deixar, efeito na performance é ignoravel
if dia <= 31 and mes == 1:
    dias_totais += 0

#condicionais que adicionam os dias dos meses do inicio do ano até o mês atual ao total de dias 
if dia <= 29 and mes == 2:
    dias_totais += mes1

if dia <= 31 and mes == 3:
    dias_totais += mes1 + mes2

if dia <= 30 and mes == 4:
    dias_totais += mes1 + mes2 + mes3 

if dia <= 31 and mes == 5:
    dias_totais += mes1 + mes2 + mes3 + mes4

if dia <= 30 and mes == 6:
    dias_totais += mes1 + mes2 + mes3 + mes4 + mes5 

if dia <= 31 and mes == 7:
    dias_totais += mes1 + mes2 + mes3 + mes4 + mes5 + mes6

if dia <= 31 and mes == 8:
    dias_totais += mes1 + mes2 + mes3 + mes4 + mes5 + mes6 + mes7

if dia <= 30 and mes == 9:
    dias_totais += mes1 + mes2 + mes3 + mes4 + mes5 + mes6 + mes7 + mes8 

if dia <= 31 and mes == 10:
    dias_totais += mes1 + mes2 + mes3 + mes4 + mes5 + mes6 + mes7 + mes8 + mes9

if dia <= 30 and mes == 11:
    dias_totais += mes1 + mes2 + mes3 + mes4 + mes5 + mes6 + mes7 + mes8 + mes9 + mes10

if dia <= 31 and mes == 12:
    dias_totais += mes1 + mes2 + mes3 + mes4 + mes5 + mes6 + mes7 + mes8 + mes9 + mes10 + mes11
    #print('ok5') #usado para teste

#variaveis e condicionais usadas para descobrir quantos sabados houveram da data informada até hoje
sabados = dias_totais // 7
#usei duas fontes pra calcular quantos sabados havia nesse periodo( https://clubedospoupadores.com/calculadora-dias-uteis ) 
# -e um codigo usando a livraria datetime que o chatGPT me deu) as duas me deram resultados diferentes, o site me deu- 
# -2956,5 e o codigo deu 2957

# essa parte a seguir era minha tentativa de corrigir o calculo, eu fiz o teste com o codigo do GPT em um sabado e-
#-meu calculo dava 1 a menos 
'''
resto = dias_totais % 7
if resto == 0:
    sabados += 1
'''

#funções que mostra o resultado do calculo
print("Houveram ", dias_totais, " dias desde ", dia_anterior, "-", mes_anterior,"-",  ano_anterior, "até hoje")
print("Houveram ", sabados, " sabados desde ", dia_anterior, "-", mes_anterior,"-",  ano_anterior, "até hoje")
