temp = list()
mta = list()
cont2 = cont3 = cont4 = 0

for cont in range(0,3):
    for i in range(0,3):
        temp.append(int(input('Insira um número: ')))
    for i in temp:
        if i % 2 == 0:
            cont2 += i
    if cont == 2:
        for i in temp:
            cont3 += i
    if cont == 1:
        for i in temp:
            if cont4 < i:
                cont4 = i

    mta.append(temp[:])
    temp.clear()

for i in mta:
    print(f'[  {i[0]}  ] [  {i[1]}  ] [  {i[2]}  ]')
print(f'A soma de todos os pares é igual a: {cont2}')
print(f'A soma da terceira coluna é igual a: {cont3} ')
print(f'O maior valor da coluna 2 é: {cont4}')