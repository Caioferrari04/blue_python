def profMuitoLegal(not1,not2,not3):
    if not1 >= 0 and not1 <= 10 and not2 >= 0 and not2 <= 10 and not3 >= 0 and not3 <= 10:
        if not1 >= not2 and not1 >= not3:
            if not2 > not3:
                media1 = (not1+not2)/2
            else:
                media1 = (not1+not3)/2
        elif not3 >= not1 and not3 >= not2:
            if not1 > not2:
                media1 = (not3+not1)/2
            else:
                media1 = (not3+not2)/2
        else:
            if not1 > not3:
                media1 = (not2+not1)/2
            else:
                media1 = (not2+not3)/2
        return media1
    else:
        return 'Uma das notas está inválida!!'


def tudo(note1,note2,note3):
    if note1 >= 0 and note1 <= 10 and note2 >= 0 and note2 <= 10 and note3 >= 0 and note3 <= 10:
        return (note1+note2+note3)/3
    else:
        return 'UMA DAS NOTAS ESTÁ INVÁLIDA!!'


def maismenos(notu1,notu2,notu3):
    if notu1 >= 0 and notu1 <= 10 and notu2 >= 0 and notu2 <= 10 and notu3 >= 0 and notu3 <= 10:
        if notu1 >= notu2 and notu1 >= notu3:
            if notu2 >= notu3:
                return f'Maior nota: {notu1}\nMenor nota: {notu3}'
            else:
                return f'Maior nota: {notu1}\nMenor nota: {notu2}'
        elif notu3 >= notu1 and notu3 >= notu2:
            if notu1 >= notu2:
                return f'Maior nota: {notu3}\nMenor nota: {notu2}'
            else:
                return f'Maior nota: {notu3}\nMenor nota: {notu1}'
        else:
            if notu1 >= notu3:
                return f'Maior nota: {notu2}\nMenor nota: {notu3}'
            else:
                return f'Maior nota: {notu2}\nMenor nota: {notu1}'
    else:
        return 'Uma das notas está inválida!!'


nota1 = float(input('Insira nota 1: '))
nota2 = float(input('Insira nota 2: '))
nota3 = float(input('Insira nota 3: '))
print(f'Media final (2 notas mais altas): {profMuitoLegal(nota1,nota2,nota3)}')
print(f'Media final (3 notas): {tudo(nota1,nota2,nota3)}')
print(f'Maior e menor nota: {maismenos(nota1,nota2,nota3)}')