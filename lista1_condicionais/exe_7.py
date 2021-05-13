def func(aby,bby):
    if aby > bby:
        return bby
    elif aby == bby:
        return 'Os valores são iguais!!'
    else:
        return aby


ab = int(input('Insira o primeiro número: '))
bb = int(input('Insira o segundo valor: '))
print(f'O menor número é: {func(ab,bb)}')
