##
# Primeira questão da aula de programação de computadores do dia 28/01/2024 
#
#   João Gabriel Nóbrega
#

x = dict()

x["e"] = "ifi"
x['c'] = 'efi'

print(x['e'], 'unica')
print(x["e"], 'dupla')


cahves = x.keys()
print(cahves)
print(x.keys())
print(x.items())
print(dir(x))
print(x)

print(x["e"])

del x['e']
print(x)


