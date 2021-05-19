# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista, 
# depois do dado inserido, pergunte ao usuário se ele quer continuar, 
# se ele não quiser pare o programa. No final mostre:
   # Quantas pessoas foram cadastradas
   # Mostre o maior peso
   # Mostre o menor peso

people = list()
grupo = list()
ch = cont = 0

while True:
    people.append(int(input('Insira o peso: ')))
    people.append(str(input('Insira o nome: ')))
    grupo.append(people[:])
    people.clear()
    ch = str(input('Deseja parar o programa?[Sim/Não] ')).upper().strip()[0]
    cont += 1
    if ch == 'S':
        break

max_peso = min_peso = 0

grupo.sort()

print(grupo)
max_peso = grupo[cont-1][0]
min_peso = grupo[0][0]

        
print(f'O maior peso é de: {max_peso}')
print(f'O menor peso é de: {min_peso}')
    