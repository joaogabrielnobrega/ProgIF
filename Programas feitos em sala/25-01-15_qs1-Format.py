## 

print('''
     asd     
   fasdsad
''')
'''
n = 10/3

print(f'o valor é {n:4.2f}') # 4 caracteres totais 2 dps do ponto

x = 5 

print(f'valor x {x:6^3d}')
print(f'valor x {x:6<3d}')
print(f'valor x {x:6>3d}')
print(f'valor x {x:6=3d}')
print(f'valor x {x:63d}')
print(f'valor x {x:+63d}')
print(f'valor x {x:-63d}')
print(f'valor x {x:6^+3d}')
print(f'valor x {x:6^-3d}')

print(f'{-45.72793:+2.3f}')

print(f'\033[1;37;42m o valor x {x:#<+20d}\033[m')
'''

conta = int(input("Conta?"))
pago = int(input("Pago?"))
troco = pago - conta

cedulas = [200, 100, 50, 20, 10, 5, 2, 1]
cedulas_troco = []

for cedula in cedulas:
    if troco // cedula != 0:
        cedulas_troco.append(f'{troco // cedula} notas de {cedula}')
        print(f'{troco // cedula} notas de {cedula}')
    troco %= cedula

'''
for elemento in cedulas_troco:
    print(elemento)
'''