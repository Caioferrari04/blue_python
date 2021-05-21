registro = {
    'nome': '',
    'gen': '',
    'age': 0
}
res = list()
res.append(registro)
cond1 = cond2 = 0

while True:
    res[0]['nome'] = str(input('Insira um nome: '))
    res[0]['gen'] = str(input('Insira um gênero [Homem/Mulher]: ').strip().upper()[0])
    if registro['gen'] != 'H' and registro['gen'] != 'M':
        print('Inválido! Inválido! Inválido!')
        break
    res[0]['age'] = int(input('Insira uma idade: '))
    res[0][f'nome{cond1}'] = registro['nome']
    res[0][f'gen{cond1}'] = registro['gen']
    res[0][f'age{cond1}'] = registro['age']
    res[0].pop('nome')
    res[0].pop('gen')
    res[0].pop('age')
    cond1 += 1
    ch = str(input('Deseja parar o programa? [Sim/Não] ').strip().upper()[0])
    if ch == 'S' or ch == 'N':
        if ch == 'S':
            break
    else:
        print('Inválido! Inválido! Inválido!')
        break
        

print(f'Número de registros: {cond1}')

for i in range(0,cond1):
    cond2 += res[0][f'age{i}']
cond2 = cond2/cond1

print(f'A média de idades é de: {cond2}')

print('Lista de mulheres: ')
for i in range(0,cond1):
    if res[0][f'gen{i}'] == 'M':
        print(res[0][f'nome{i}'], end=', ')

print('\nLista de pessoas com idade acima da média: ')
for i in range(0,cond1):
    if res[0][f'age{i}'] > cond2:
        print(res[0][f'nome{i}'], end=', idade:')
        print(res[0][f'age{i}'])
        
