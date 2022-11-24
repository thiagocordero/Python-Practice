'''Exercício Python 076: Crie um programa que tenha uma tupla única com
 nomes de produtos e seus respectivos preços, na sequência. No final,
 mostre uma listagem de preços, organizando os dados em forma tabular.'''

lista = ("Patinete Elétrico", 4000,
         "Computador", 2500,
         "Televisão", 1500,
         "Bicicleta", 600,
         "Mochila", 200,
         "Ventilador", 120,
         "Livro", 50)

print("-"*44)
print(f'{"LISTA DE PREÇOS":^44}')
print("-"*44)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f"{lista[pos]:.<30}", end='')
    else:
        print(f"R${lista[pos]:>10.2f}")

print("-"*44)
