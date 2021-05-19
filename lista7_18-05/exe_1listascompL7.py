
temp = list()
lista = list()

for i in range(0,7):
    temp.append(int(input('Insira um número: ')))

par = list()
impar = list()

for i in temp:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

par.sort()
impar.sort()
lista.append(par)
lista.append(impar)
print(f'Resultado: {lista}')
