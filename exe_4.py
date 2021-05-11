def salario(SalBase,Hora):
    if Hora > 40:
        Saliquido = Hora*(SalBase*1.5)
    else:
        Saliquido = Hora*SalBase
    return Saliquido


salbase = float(input('Insira seu salário p/hora: '))
horas = int(input('Insira a quantidade de horas trabalhadas: '))
print(f'O seu salário é de: R${salario(salbase,horas)}')