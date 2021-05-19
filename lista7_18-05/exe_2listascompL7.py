temp = list()
mta = list()
cont = 0

while cont != 3:
    for i in range(0,3):
        temp.append(int(input('Insira um número: ')))
    mta.append(temp[:])
    cont +=1
    temp.clear()


print(f'[{mta[0][0]}] [{mta[0][1]}] [{mta[0][2]}]')
print(f'[{mta[1][0]}] [{mta[1][1]}] [{mta[1][2]}]')
print(f'[{mta[2][0]}] [{mta[2][1]}] [{mta[2][2]}]')
