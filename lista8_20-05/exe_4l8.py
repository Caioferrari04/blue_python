from random import randint
from operator import itemgetter

dicion = {
    'p1': randint(0,6),
    'p2': randint(0,6),
    'p3': randint(0,6),
    'p4': randint(0,6)
}
print('Os valores sorteados são: ')
for i,y in dicion.items():
    print(f'O jogador {i} tirou {y}')

lista = sorted(dicion.items(),key=itemgetter(1),reverse=True)

print('A lista, em ordem decrescente:')
for i,y in lista:
    print(f'Jogador {i} = {y}')
