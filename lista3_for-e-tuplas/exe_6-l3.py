val1 = int(input('Insira o primeiro valor: '))
val2 = int(input('Insira o segundo valor: '))
val3 = int(input('Insira o terceiro valor: '))
val4 = int(input('Insira o quarto valor: '))

cofre = (val1,val2,val3,val4)

#index = posição
#count = quantas vezes apareceu

print(f'Em que posição o número 9 apareceu na tuple? {cofre.index(9)}')
print(f'Quantas vezes o número 3 apareceu na tuple? {cofre.count(3)} vezes')