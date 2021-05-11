def func(NOTA):
    if NOTA >=0 and NOTA <=10:
        if NOTA >=9:
            return 'A'
        elif NOTA >=8:
            return 'B'
        elif NOTA >=7:
            return 'C'
        elif NOTA >=6:
            return 'D'
        elif NOTA <=4:
            return 'F'
    else:
        return 'INVÁLIDO!!!'


nota = float(input('Insira sua nota: '))
print(f'Você tirou a nota: {func(nota)}')
