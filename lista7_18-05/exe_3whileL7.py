
produto = list()
cont = cont2 = cont3 = cont5 = 0
cont4 = ''

while True:

    cont5 += 1
    produto.append(str(input('Insira o nome do produto: ')))
    produto.append(float(input('Insira o preço do produto: ')))

    cont += produto[1]
    if produto[1] >= 1000:
        cont2 += 1
    if cont5 == 1:
        cont3 = produto[1]
        cont4 = produto[0]
    else:
        if produto[1] < cont3:
            cont3 = produto[1]
            cont4 = produto[0]
    produto.clear()

    ch = str(input('Deseja parar o programa?[Sim/Não] ').strip().upper()[0])
    if ch == 'S':
        break

print(f'O preço total é de: R${cont:.2f}.')
print(f'O total de produtos que custam acima de R$1000,00 é: {cont2}.')
print(f'O produto mais barato pertence ao: {cont4}, custando {cont3}.')