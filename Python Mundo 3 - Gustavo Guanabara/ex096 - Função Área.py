'''Exercício Python 096: Faça um programa que tenha uma função chamada
área(), que receba as dimensões de um terreno retangular (largura e comprimento)
 e mostre a área do terreno.'''


def area(largura, comprimento):
    area = largura * comprimento
    print(f"A área de um terreno de {largura}m x {comprimento}m é de {area:.1f}m².")


print("-"*30)
print(f"{'ÁREA DE TERRENOS':^30}")
print("-"*30)

a = float(input("LARGURA(m): "))
b = float(input("COMPRIMENTO(m): "))
area(a, b)
