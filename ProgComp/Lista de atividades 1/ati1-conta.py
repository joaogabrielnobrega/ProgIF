# Codigo para calcular quanto de troco precisa ser dado em uma conta 

conta = float(input("Insira o valor da conta: "))
pago = float(input("Insira quanto foi pago: "))
troco = pago - conta

if troco > 0:
    
    cedulas = troco // 200
    if cedulas > 0:
        print(f"Número de notas de 200 reais é: {cedulas}")
    troco_meio = troco % 200
    
    cedulas = troco_meio // 100
    if cedulas > 0:
        print(f"Número de notas de 100 reais é: {cedulas}")
    troco_meio = troco_meio % 100
    
    cedulas = troco_meio // 50
    if cedulas > 0:
        print(f"Número de notas de 50 reais é: {cedulas}")
    troco_meio = troco_meio % 50
    
    cedulas = troco_meio // 20
    if cedulas > 0:
        print(f"Número de notas de 20 reais é: {cedulas}")
    troco_meio = troco_meio % 20
    
    cedulas = troco_meio // 10
    if cedulas > 0:
        print(f"Número de notas de 10 reais é: {cedulas}")
    troco_meio = troco_meio % 10
    
    cedulas = troco_meio // 5
    if cedulas > 0:
        print(f"Número de notas de 5 reais é: {cedulas}")
    troco_meio = troco_meio % 5
    
    cedulas = troco_meio // 2
    if cedulas > 0:
        print(f"Número de notas de 2 reais é: {cedulas}")
    troco_meio = troco_meio % 2
    
    cedulas = troco_meio // 1
    if cedulas > 0:
        print(f"Número de moedas de 1 real é: {cedulas}")
    troco_meio = troco_meio % 1
else:
    if troco == 0:
        print("Não há troco")
    if troco < 0:
        print("Não foi pago o suficiente")