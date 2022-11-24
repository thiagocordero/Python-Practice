'''Exercício Python 080: Crie um programa onde o usuário possa digitar
cinco valores numéricos e cadastre-os em uma lista, já na posição correta
de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'''

ordenados = []
for c in range(1, 6):
    n = int(input(f"Digite o {c}° numero: "))
    if c == 1 or n > ordenados[-1]:
        ordenados.append(n)
        print(f"Adicionado no final da fila")
    else:
        pos = 0
        while pos < len(ordenados):
            if n <= ordenados[pos]:
                ordenados.insert(pos, n)
                print(f"Número {n} adicionado na posição {pos}")
                break
            pos += 1
print("=-"*30)
print(f"A lista digitada em ordem foi: {ordenados}")




