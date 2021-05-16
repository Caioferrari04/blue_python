
votos = [0,0,0,0,0]
vot = ''
esc = 0

while vot != 'nao' and vot != 'não':
    print('Vote no seu candidato favorito!\n1 - Josefina')
    print('2 - Makarov')
    print('3 - El Presidente')
    print('4 - Branco')
    print('5 - Nulo')
    esc = int(input('Vote aqui! '))
    votos[esc-1] += 1
    vot = input('Deseja continuar votando? ').lower()

print(f'Quantidade de votos para Josefina: {votos[0]} ')
print(f'Quantidade de votos para Makarov: {votos[1]} ')
print(f'Quantidade de votos para El Presidente: {votos[2]} ')
print(f'Quantidade de votos para Branco: {votos[3]} ')
print(f'Quantidade de votos para Nulo: {votos[4]} ')