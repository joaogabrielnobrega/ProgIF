# Codigo para descobrir o imposto ICMS que um vendedor pagara sob um produto 

taxa = 17/100
valor_compra = float(input("Insira quanto foi pago na compra do produto: "))
valor_venda = float(input("Insira quanto foi cobrado na venda do produto: "))

ICMS = (valor_venda - valor_compra) * taxa

print(f"O imposto que deve ser pago sob esse produto é: R${ICMS}")
