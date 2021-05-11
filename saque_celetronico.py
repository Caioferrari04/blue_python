cash = int(input('Insira o quanto você pagou: '))

if cash >= 10 and cash <= 600:

    pago100 = cash//100
    cash -= pago100*100

    pago50 = cash//50
    cash -= pago50*50

    pago10 = cash//10
    cash -= pago10*10

    pago5 = cash//5
    cash -= pago5*5

    pago1 = cash//1
    cash -= pago1*1
else:
    print('Valor inválido.')

print(f'Foram utilizadas {pago100} notas de R$100, {pago50} notas de R$50, {pago10} notas de R$10,{pago5} notas de R$5 e {pago1} notas de R$1')