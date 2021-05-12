from datetime import date

def func(atual,data):
    if atual - data >= 16:
        if atual - data >= 18:
            return 'OBRIGATÓRIO!!!'
        else:
            return 'Opcional!'
    else:
        return 'NEGADO!!!'

    
aniver = int(input('Insira sua data de nascimento: '))
data_atual = date.today().year
print(f'Você pode votar? \n {func(data_atual,aniver)}')
