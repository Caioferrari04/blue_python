import random

valrand = (random.randint(1,51),random.randint(1,51),random.randint(1,51),
random.randint(1,51),random.randint(1,51))
maximum = max(valrand)
minimum = min(valrand)
print(f'Menor valor: {minimum}\nMaior valor: {maximum}\nTupla completa: {valrand}')
