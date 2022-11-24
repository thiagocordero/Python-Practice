'''Exercício Python 084: Faça um programa que leia nome e peso de várias
pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

dadosTemporarios = []
pessoas = []
maior = menor = 0
while True:
    dadosTemporarios.append(str(input("Nome: ")))
    dadosTemporarios.append(float(input("Peso: ")))
    if len(pessoas) == 0:
        maior = menor = dadosTemporarios[1]
    else:
        if dadosTemporarios[1] > maior:
            maior = dadosTemporarios[1]
        if dadosTemporarios[1] < menor:
            menor = dadosTemporarios[1]
    pessoas.append(dadosTemporarios[:])
    dadosTemporarios.clear()
    option = str(input("Deseja continuar[S/N]? "))
    if option in 'Nn':
        break

print("-="*30)
#A) Quantas pessoas foram cadastradas.
print(f"Ao todo, foram registradas {len(pessoas)} pessoas.")
print("-="*30)
print(pessoas)
print("-="*30)
#B) Uma listagem com as pessoas mais pesadas.
print(f"O maior peso foi {maior}Kg. Esse é o peso de ", end='')
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(f"[{pessoa[0]}] ", end='')
print("\n"+("-="*30))
#C) Uma listagem com as pessoas mais leves.
print(f"O menor peso foi {menor}Kg. Esse é o peso de ", end='')
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(f"[{pessoa[0]}]", end='')
print("\n"+("-="*30))






