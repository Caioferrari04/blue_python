def func(arg):
    if arg > 0:
        return 'P'
    elif arg < 0:
        return 'N'
    else:
        return 0


arguu = int(input('Insira um número: '))
print(f'*Trambores* Seu número é.... {func(arguu)}')