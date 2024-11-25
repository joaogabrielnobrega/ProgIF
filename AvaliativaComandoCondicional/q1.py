#Codigo para calcular o IMC do usuario

#Variaveis que pede ao usuario os valores necessarios
peso = float(input("Insira seu peso em kilogramas: \n"))
altura = int(input("Insira sua altura em centimetros: \n"))
situação_imc = ""

#Variavel que recebe o valor do IMC de acordo com os valores entregues pelo usuario
altura_m = altura / 100
imc = peso / (altura_m ** 2)

#Condicionais para determinar a situação de acordo com o IMC e a tabela do site dado na questão
if imc <= 18.5:
    situação_imc = "Abaixo do normal"
elif 18.6 <= imc < 25:
    situação_imc = "Peso normal"
elif 25 <= imc < 30:
    situação_imc = "Sobrepeso"
elif 30 <= imc < 35:
    situação_imc = "Obesidade grau I"
elif 35 <= imc < 40:
    situação_imc = "Obesidade grau II"
elif imc >= 40:
    situação_imc = "Obesidade grau III"

#Funções para mostrar no console o IMC e a situação do usuario
print("\nEste é o seu IMC: ", round(imc, 2))
print("Essa é sua situação de acordo com seu IMC: \n", situação_imc)
