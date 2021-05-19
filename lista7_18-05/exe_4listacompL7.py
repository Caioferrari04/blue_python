import random

lista = [random.randint(0,60),random.randint(0,60),random.randint(0,60),
random.randint(0,60),random.randint(0,60),random.randint(0,60)]
lista_comp = list()

esc = int(input('Escreva quantos palpites deseja ver: '))

for i in range(1,esc+1):
    for y in range(0,5):
        if lista[y]==lista[y+1]:
            lista[y] = random.randint(0,60)
    lista_comp.append(lista)
    lista = [random.randint(0,60),random.randint(0,60),random.randint(0,60),
random.randint(0,60),random.randint(0,60),random.randint(0,60)]

for i in range(0,esc):
    print(f'Palpite nº{i+1}: {lista_comp[i]}')
