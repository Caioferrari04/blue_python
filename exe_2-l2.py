def func(prim,secun,limi):
    if prim + secun > limi:
        return True
    else:
        return False


pri = int(input('Insira o primeiro valor: '))
secu = int(input('Insira o segundo valor: '))
lim = int(input('Insira o valor limite: '))
print(f'A soma de {pri} + {secu} é maior que {lim}? \n {func(pri,secu,lim)}')
