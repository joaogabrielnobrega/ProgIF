# Codigo para calcular juros composto

try:
    cap = float(input("Insira seu captal inicial para essa operação: "))
    juros = float(input("Insira o juros dessa operação: "))
    tempo = int(input("Insira o tempo que essa operação será feita de acordo com a forma em que o juros é calculado, se o juros for mensal o tempo precisa ser em meses: "))

    if cap > 0 and juros > 0 and tempo > 0:

        montante = cap * (1+ juros/100) ** tempo

        print(f"\nO montante ao final dessa operação é: {montante}")
    else: print("Um ou mais dos valores é zero ou negativo, por que?")
except:
    print("O valor do captal inicial, juros e/ou tempo é/são invalidos")
