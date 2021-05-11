def imc(PESO,ALT):
    IMC = PESO/(ALT**2)
    return IMC


peso = int(input('Insira seu peso: '))
alt = float(input('Insira sua altura[Em metros, com ponto]: '))
print(f'Seu IMC é de: {imc(peso,alt):.2f}kg/m²')