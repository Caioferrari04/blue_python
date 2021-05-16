
def cont18oumais(age):
    total = 0
    for y in range(0,len(age)):
        if age[y] >= 18:
            total += 1
    return total

def homens(gen):
    total = 0
    for x in range(0,len(gen)):
        if gen[x] == 'H':
            total +=1
    return total


def mulheres20oumenos(gene,idad):
    total = 0
    for z in range(0,len(gene)):
        if gene[z] == 'M':
            if idad[z] < 20:
                total += 1
    return total


nomes = list()
idade = list()
genero = list()
boolea = ''

while True:
    nomes.append(input('Insira o nome: '))
    idade.append(int(input('Insira a idade: ')))
    genero.append(str(input('Insira o gênero [Homem ou mulher]: ')).upper().strip()[0])
    boolea = str(input('Deseja parar o programa? ')).upper().strip()[0]
    if boolea == 'S':
        break

print(f'O total de pessoas que tem mais de 18 anos é de: {cont18oumais(idade)} ')
print(f'O total de homens é: {homens(genero)}')
print(f'O total de mulheres abaixo de 20 anos é: {mulheres20oumenos(genero,idade)}')
