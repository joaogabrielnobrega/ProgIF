# perguntar: tempo viagem (min), litros combustivel gasto(L), preço combustivel(R$), distancia percorrida(Km)
# mostrar: velocidade media (Km/h), custo combustivel viagem (R$), desempenho carro (Km/l, l/H, R$/Km)

t_v = int(input('Insira quanto tempo a viagem durou em minutos: '))
c_g = float(input('Insira quanto de combustivel foi gasto nessa viagem em litros: '))
p_c = float(input('Insira o preço do combustivel em reais: '))
d_p = float(input('Insira a distancia percorrida nessa viagem em kilometros: '))

v_m = d_p / t_v
c_c = c_g * p_c
d_kml = d_p / c_g
d_lh = c_g / t_v
d_rskm = c_c / d_p

print(f"\nA velocidade media dessa viagem foi: {v_m} Km/h \nFoi gasto R${c_c} em combustivel \nSeu carro fez {d_kml} Km/l \nSeu carro gastou {d_lh} l/h \nSeu carro gastou {d_rskm} R$/Km")

#print(f"A velocidade media dessa viagem foi: {v_m}")
#print(f"Foi gasto R${c_c} em combustivel")
#print(f"Seu carro fez {d_kml} Km/l")
#print(f"Seu carro gastou {d_lh} l/h")
#print(f"Seu carro gastou {d_rskm} R$/Km")