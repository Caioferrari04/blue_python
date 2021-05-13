
stri = input('Insira uma palavra: ')
c = 0
for i in stri:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        c += 1

print(f'Uma vogal apareceu {c} vezes')