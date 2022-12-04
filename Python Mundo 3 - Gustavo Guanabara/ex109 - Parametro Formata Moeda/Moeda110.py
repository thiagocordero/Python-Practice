def dobro(valor, dinheiro=False):
    final = valor*2
    return final if dinheiro is False else moeda(final)


def metade(valor, dinheiro=False):
    final = valor / 2
    return final if dinheiro is False else moeda(final)


def aumento(valor, taxa, dinheiro=False):
    final = valor + (valor*taxa)/100
    return final if dinheiro is False else moeda(final)


def desconto(valor, taxa, dinheiro=False):
    final = valor - (valor * taxa) / 100
    return final if dinheiro is False else moeda(final)


def moeda(valor=0, simbolo="R$"):
    return f"{simbolo}{valor:>8.2f}".replace(".", ",")


def resumo(preco=0, mais=10, menos=5):
    print("=-"*15)
    print(f"{'RESUMO DO VALOR':^30}")
    print("-"*30)
    print(f"Preço Analisado: {moeda(preco)} ")
    print("-" * 30)
    print(f"Metade do preço: \t{metade(preco, True)}")
    print(f"Dobro do preço: \t{dobro(preco, True)}")
    print(f"Aumento de {mais}%: \t{aumento(preco, mais, True)}")
    print(f"Desconto de {menos}%: \t{desconto(preco, menos, True)}")
    print("=-" * 15)

