# Complicado, cheio de IF e FEIO.
def func(DIA,MES,ANO):
    if DIA > 31:
        return None
    if MES == 1:
        return f'{DIA}/Janeiro/{ANO}'
    elif MES == 2:
        if ANO % 4 == 0 or ANO % 400 == 0:
            if DIA > 29:
                return f'{None}/Fevereiro/{ANO}'
            else:
                return f'{DIA}/Fevereiro/{ANO}'
        else:
            if DIA > 28:
                return f'{None}/Fevereiro/{ANO}'
            else:
                return f'{DIA}/Fevereiro/{ANO}'
    elif MES == 3:
        return f'{DIA}/Março/{ANO}'
    elif MES == 4:
        if DIA > 30:
            return f'{None}/Abril/{ANO}'
        else:
            return f'{DIA}/Abril/{ANO}'
    elif MES == 5:
        return f'{DIA}/Maio/{ANO}'
    elif MES == 6:
        if DIA > 30:
            return f'{None}/Junho/{ANO}'
        else:
            return f'{DIA}/Junho/{ANO}'
    elif MES == 7:
        return f'{DIA}/Julho/{ANO}'
    elif MES == 8:
        return f'{DIA}/Agosto/{ANO}'
    elif MES == 9:
        if DIA > 30:
            return f'{None}/Setembro/{ANO}'
        else:
            return f'{DIA}/Setembro/{ANO}'
    elif MES == 10:
        return f'{DIA}/Outubro/{ANO}'
    elif MES == 11:
        if DIA > 30:
            return f'{None}/Novembro/{ANO}'
        else:
            return f'{DIA}/Novembro/{ANO}'
    elif MES == 12:
        return f'{DIA}/Dezembro/{ANO}'
    else:
        return f'{DIA}/{None}/{ANO}'

# Simples, sem muito if e BONITO.       
def func2(DIA,MES,ANO):
    meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho',
    'Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    if MES >= 1 and MES <= 12:
        if DIA >= 1 and DIA <=31:
            MES -= 1

            if MES == 1:
                MES = meses[MES]

                if ANO % 4 == 0 or ANO % 400 == 0:
                    if DIA > 29:
                        return f'{None}/{MES}/{ANO} !!! Dia inválido'
                    else:
                        return f'{DIA}/{MES}/{ANO}'
                else:
                    if DIA > 28:
                        return f'{None}/{MES}/{ANO} !!! Dia inválido '
                    else:
                        return f'{DIA}/{MES}/{ANO}'

            if MES == 3 or MES == 5 or MES == 8 or MES == 10:
                MES = meses[MES]
                if DIA > 30:
                    return f'{None}/{MES}/{ANO} !!! Dia inválido '
                else:
                    return f'{DIA}/{MES}/{ANO}'

            MES = meses[MES]
            return f'{DIA}/{MES}/{ANO}'
    else:
        return f'{DIA}/{None}/{ANO} !!! Mês inválido'


dia = int(input('Insira o dia: '))
mes = int(input('INsira o mês: '))
ano = int(input('Insira o ano: '))
print(f'Data: {func(dia,mes,ano)}')
print(f'Data usando código bonito: {func2(dia,mes,ano)}')
