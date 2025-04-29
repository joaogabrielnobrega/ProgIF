# Codigo para calcular investimento com juros compostos e aporte mensal

cap_inicial = float(input("Insira seu captal inicial: "))
apo_men = int(input("Insira o aporte mensal que você pretende fazer: "))
juros = float(input("Insira o juros mensal do titulo: "))
meses = int(input("Insira quantos meses a operação durará: "))

j0 = (juros / 100) 
j1 = 1 + j0

valor_final = cap_inicial * (j1 ** meses) + apo_men * ((j1 ** meses) - j1) / j0
valor_juros = valor_final - (cap_inicial + (apo_men * meses))

#valor_final = cap_inicial * (1 + juros/100) ** meses + apo_men * ((1 + juros/100) ** meses - (1 + juros/100))/ (juros/100)

print(f"\nEsse é o valor que você terá ao final da operação R${valor_final} \nIsso é quanto você ganhou a partir dos juros R${valor_juros}")