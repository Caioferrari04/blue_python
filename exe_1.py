def func(y,h,m):
    z = y+h+m
    return z


a = int(input('Insira o primeiro numero: '))
b = int(input('Insira o segundo numero: '))
c = int(input('Insira o terceiro numero: '))
print(f'A soma dos três números é: {func(a,b,c)}')
