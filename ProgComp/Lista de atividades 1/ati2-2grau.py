#calcular equação de segundo grau

try:
    A = int(input("Insira o valor de A: "))
    B = int(input("Insira o valor de B: "))
    C = int(input("Insira o valor de C: "))
    
    if A != 0:
        DELTA = B**2 - 4 * A * C

        X1 = (-B + DELTA**(1/2))/(2 * A)
        X2 = (-B - DELTA**(1/2))/(2 * A)
        
        if DELTA > 0:
            print(f"\nResultado de delta: {DELTA} \n\nResultado de x1: {X1} \nResultado de x2: {X2}")
        else: print("\nDelta não pode ser calculado")
    else: print("Valor de A precisa ser diferente de zero")
except:
    print("Valor de A, B e/ou C é/são invalidos")