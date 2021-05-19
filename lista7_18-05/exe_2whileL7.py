
pessoas = list()
cont = cont2 = cont3 = 0

while True:
    pessoas.append(str(input('Insira o nome: ')))
    pessoas.append(int(input('Insira sua idade: ')))
    pessoas.append(str(input('Insira seu gênero[Homem/Mulher]: ').strip().upper()[0]))
    if pessoas[1] > 18:
        cont +=1
    if pessoas[2] == 'H':
        cont2 +=1
    if pessoas[2] == 'M' and pessoas[1] < 20:
        cont3 +=1
    ch = str(input('Deseja parar o programa?[Sim/Não] ').strip().upper()[0])
    if ch == 'S':
        break
    pessoas.clear()

print(f'Número de maiores de 18 é de: {cont} pessoas')
print(f'Número de homens é de: {cont2} pessoas')
print(f'Número de mulheres menores de 20 é de: {cont3} pessoas')

