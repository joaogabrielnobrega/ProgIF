texto = '''Procurar a nossa felicidade através da felicidade dos outros - aconselhava Olívia noutra carta sem data.
- Não estou pregando o ascetismo, a santidade, não estou elogiando o puro espírito de sacrifício e renúncia.
Tudo isso seria inumano, significaria ainda uma fuga da vida. Mas o que procuro, o que desejo, é segurar a vida
pelos ombros e estreitá-la contra o peito, beijá-la na face. Vida, entretanto, não é o ambiente em que te achas.
As maneiras estudadas, as frases convencionais, o excesso de conforto, os perfumes caros e a preocupação do
dinheiro são apenas uma péssima contrafação da vida. Buscar a poesia da vida será coisa que tenha nexo?
Ele agora vivia...Tinha tido apenas a ilusão de viver, mas na verdade andara morto por entre os homens.
O dia mais importante da minha vida foi aquele em que, recordando todos os meus erros, achei que já chegara
a hora de procurar uma nova maneira de ser útil ao próximo, de dar novo rumo às minhas relações humanas.
Que era que eu tinha feito senão satisfazer os meus desejos, o meu egoísmo? Podia ser considerada uma
criatura boa apenas porque não matava, porque não roubava, porque não agredia? A bondade não deve ser
uma virtude passiva. No dia em que eu achei Deus, encontrei a paz para mim e ao mesmo tempo percebi que
de certa maneira não haveria paz para mim. Descobri que a paz interior só se conquista com o sacrifício da paz
exterior. Era preciso fazer alguma coisa pelos outros. O Mundo está cheio de sofrimento, de gritos de socorro.
Que tinha eu feito até então para diminuir esse sofrimento, para atender a esses apelos? Eu via em meu redor
pessoas aflitas que, para se salvarem, esperavam apenas a mão que as apoiasse, nada mais que isso. E Deus
dera-me duas mãos. Pensei tudo isso numa noite de insônia. Quando o dia nasceu, senti que tinha nascido de
novo com ele. Era uma mulher nova.'''

chara_ind = [",",".","!","?"]

for c in chara_ind:
    texto = texto.replace(c, "")

conjunto_texto = texto.split("\n")
palavras = []

#Edição feita 31/01/2025

for linha in conjunto_texto:
    conjunto_palavras = linha.split()
    for palavra in conjunto_palavras:
        palavra = palavra.lower()
        for i in range(len(palavras) + 1):
            if i == len(palavras):
                palavras.append([palavra, 1])
                break
            if palavras[i][0] == palavra:
                palavras[i][1] += 1
                break

palavras = sorted(palavras, key= lambda x: x[1], reverse = True)
print(palavras)

'''
palavras = dict()

for linha in conjunto_texto:
    conjunto_palavras = linha.split()
    for palavra in conjunto_palavras:
        palavra = palavra.lower()
        palavras[palavra] = palavras.get(palavra, 0) + 1

print(palavras)

maior = 0
par = []

for pos, qtd in palavras.items():
    if qtd > maior:
        par = [pos, qtd]
        maior = qtd

print(f"{par[0]} {par[1]}")
'''

