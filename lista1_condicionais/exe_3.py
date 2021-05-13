def ImpostoSoma(ImpostoTaxa,otsuc):
    otsuc = (ImpostoTaxa/10) * otsuc
    return otsuc


otusc = float(input('Insira aqui o custo de venda: '))
TaxaImposto = int(input('Insira aqui a porcentagem de imposto[Sem porcentagem]: '))

print(f'Valor final, com um aumento de {TaxaImposto}%: {ImpostoSoma(TaxaImposto,otusc)} ')