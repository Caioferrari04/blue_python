
stri = input('Insira uma frase: ').lower()
coc = ''

for i in stri:
    if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
        coc = coc + i

    
print(coc)