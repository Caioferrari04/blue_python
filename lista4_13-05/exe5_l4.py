from typing import List


cont1 = 0
cont2 = 0

for i in range(1,16):
    r = input('Insira: [Casado] ou [Solteiro]: ').lower()
    if r == 'casado':
        cont1+=1
    elif r == 'solteiro':
        cont2+=1
    else:
        print('Inválido!')

    
print(f'Há {cont1} casados e {cont2} solteiros.')