dicion = {
    'nome': '',
    'nota': 0,
    'situation': ''
}
dicion['nota'] = float(input('Insira a média: '))
if dicion['nota'] >= 7:
    dicion['situation'] = 'Aprovado!'
    print(dicion['situation'])
elif dicion['nota'] > 5 and dicion['nota'] < 6.9:
    dicion['situation'] = 'Recuperação!'
    print(dicion['situation'])
else:
    dicion['situation'] = 'Reprovado!'
    print(dicion['situation'])