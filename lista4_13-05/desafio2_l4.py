
mater = int(input('Insira quantas matérias tem: '))
nota = list()
media = 0

for i in range(0,mater):
    nota.append(float(input(f'Insira sua nota da materia [{i+1}]: ')))
    media  += nota[i]

media = media/mater
print(f'Média final: {media}')