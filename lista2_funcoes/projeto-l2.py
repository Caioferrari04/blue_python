def custo_hotel(noite=0):
    result = noite * 140
    print(f'-Gastos com Hotel: R${result},00')
    return result


def custo_aviao(city=0):
    if city == 'São Paulo':
        print('--Gastos com avião: R$312,00')
        return 312
    elif city == 'Porto Alegre':
        print('--Gastos com avião: R$447,00')
        return 447
    elif city == 'Recife':
        print('--Gastos com avião: R$831,00')
        return 831
    elif city == 'Manaus':
        print('--Gastos com avião: R$986,00')
        return 986
    else:
        return 'Cidade inválida!!'


def custo_carro(dia=0):
    if dia > 0:
        if dia >= 3:
            result = (40*dia) - 20
            print(f'---Gastos com carro: R${result},00')
        elif dia >= 7:
            result = (40*dia) - 50
            print(f'---Gastos com carro: R${result},00')
        else:
            result = 40*dia
            print(f'---Gastos com carro: R${result},00')
    else:
        return 'Quantidade de dias inválido!'
    return result

    
def total(noit,cid,car):
    custo_hutel = custo_hotel(noit)
    custo_aviaum = custo_aviao(cid)
    custo_carru = custo_carro(car)
    gastos_extras = 0
    if custo_aviaum == 986 and custo_carru >= 430:
        gastos_extras += 800
        print('----Gastos extras: R$800,00')
    total = custo_hutel + custo_carru + custo_aviaum + gastos_extras
    return total

print('-----------***^^^BEM VINDO AO CALCULADOR DE GASTOS!!!^^^***-----------')
noites = int(input('Insira aqui a quantidade de noites no hotel: '))
cidade = input('Insira o seu destino a partir da seguinte lista: \nSão Paulo \nPorto Alegre \nRecife \nManaus\n ')
carros = int(input('Quantos dias irá alugar um carro?\nBONUS: Se alugar por 3 dias ou mais, terá direito a um disconto de 20 reais!\nBONUS EXTRA!!! Se alugar por 7 dias ou mais, terá direito a um disconto de 50 reais!!!\n '))
print(f'O valor total de gastos é: R${total(noites,cidade,carros)},00')

