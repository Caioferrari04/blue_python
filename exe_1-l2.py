def func(aaa,bbb):
    if aaa > bbb:
        return bbb
    elif aaa == bbb:
        return 'Valores iguais!'
    else:
        return bbb

aa = int(input('Insira o primeiro valor: '))
bb = int(input('Insira o segundo valor: '))
print(f'O menor dos valores inseridos é: {func(aa,bb)}')