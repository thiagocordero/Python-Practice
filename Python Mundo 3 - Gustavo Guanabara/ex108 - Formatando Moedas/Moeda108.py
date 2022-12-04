def dobro(valor):
    return valor * 2


def metade(valor):
    return valor / 2


def aumento(valor, taxa):
    return valor + (valor*taxa)/100


def desconto(valor, taxa):
    return valor - (valor*taxa)/100


def moeda(valor=0, simbolo="R$"):
    return f"{simbolo}{valor:>8.2f}".replace(".", ",")

