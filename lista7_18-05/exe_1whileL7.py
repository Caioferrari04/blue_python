
v1 = v2 = a = 0
ch = 0

v1 = int(input('Insira um valor: '))
v2 = int(input('Insira outro valor: '))

while a!=1:
    print('Escola o que deseja fazer:')
    print('\t[1]Somar')
    print('\t[2]multiplicar')
    print('\t[3]Maior')
    print('\t[4]Novos Números')
    print('\t[5]Sair do programa ')
    ch = int(input('Insira a opção: '))
    if ch == 1:
        result = v1+v2
        print(f'{v1}+{v2} = {result}')
    if ch == 2:
        result = v1*v2
        print(f'{v1}*{v2} = {result}')
    if ch == 3:
        if v1 > v2:
            result = v1
        else:
            result = v2
        print(f'O maior número é: {result}')
    if ch == 4:
        v1 = int(input('Insira um valor: '))
        v2 = int(input('Insira outro valor: '))
    if ch == 5:
        a += 1
        print('Buh Bye!')