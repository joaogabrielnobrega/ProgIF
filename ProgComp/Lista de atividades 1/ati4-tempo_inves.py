# Codigo para descobrir quanto tempo sera necessario para alcançar um montante em uma operação

import math

juros = 12
cap_inicial = 1000
montante_final = 1000000

t = (math.log(montante_final/cap_inicial)) / (math.log(1 + juros/100))

print(f"vai demorar {t} meses para chegar a R${montante_final}")