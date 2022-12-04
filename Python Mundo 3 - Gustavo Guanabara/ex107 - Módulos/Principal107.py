'''Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções
incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa
que importe esse módulo e use algumas dessas funções.'''

import Moeda107

n = float(input("Digite um preço: R$"))
print(f"A metade de R${n},00 é R${Moeda.metade(n)},00")
print(f"O dobro de R${n},00 é R${Moeda.dobro(n)},00")
taxa = 10
print(f"Aumentando {taxa}% temos R${Moeda.aumento(n, taxa)},00")
print(f"Com um desconto de {taxa}% sai por R${Moeda.desconto(n, taxa)},00")
