'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
totalPar = totalColuna3 = maiorLinha2 = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f"Digite um numero para [{linha}] [{coluna}]: "))
        if matriz[linha][coluna] % 2 == 0:
            totalPar += matriz[linha][coluna]
        if coluna == 2:
            totalColuna3 += matriz[linha][coluna]
        if linha == 1:
            if coluna == 0:
                maiorLinha2 = matriz[linha][coluna]
            else:
                if matriz[linha][coluna] > maiorLinha2:
                    maiorLinha2 = matriz[linha][coluna]
print("-="*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end='')
    print()
print("-="*30)
#A) A soma de todos os valores pares digitados.
print(f"A SOMA de todos os valores PARES foi: {totalPar}")
#B) A soma dos valores da terceira coluna.
print(f"A SOMA dos valores da TERCEIRA COLUNA foi: {totalColuna3}")
#C) O maior valor da segunda linha.
print(f"O MAIOR valor da SEGUNDA LINHA foi: {maiorLinha2}")
