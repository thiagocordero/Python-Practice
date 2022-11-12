'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários
produtos. O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

print("=-="*20)
print("LISTA DE COMPRAS")
print("=-="*20)

total = maisQ1000 = maisBarato = cont = 0;
produtoMaisBarato = " "

while True:
    produto = str(input("Produto: ")).strip().upper()
    preco = float(input("Preço: R$"))

    total += preco
    if preco >= 1000:
        maisQ1000 += 1

    if cont == 0 or preco < maisBarato:
        maisBarato = preco
        produtoMaisBarato = produto

    option = str(input("Continuar[S/N]: ")).strip().upper()[0]
    if option == "N":
        break

print("=-="*20)

print(f"Total da Compra: {total}")
print(f"{maisQ1000} produtos custam mais de R$1000,00")
print(f"O produto mais barato foi {produtoMaisBarato}, custando R${maisBarato}")

print("=-="*20)
