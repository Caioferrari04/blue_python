
price = float(input('Insira o preço do pão: '))
novo_price = 0
print('Panificadora Pão de Hoje -  Tabela de Preços')
for i in range(1,51):
    novo_price += price
    print(f'{i} - R${novo_price:.2f}')