from random import randint

v1 = randint(0,11)
user = 35
cond = 0
print(v1)
while user != v1:
    user = int(input('Insira a sua advinhação: '))
    if user != v1:
        cond += 1

print(f'O valor era {v1} e você tentou {cond} vezes!')

