'''Exercício Python 082: Crie um programa que vai ler vários números e
colocar em uma lista. Depois disso, crie duas listas extras que vão conter
apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.'''

numeros = []
while True:
    numeros.append(int(input("Digite um número: ")))
    option = str(input("Deseja continuar [S/N]? "))[0]
    if option in 'Nn':
        break

par = []
impar = []
for c in range(0, len(numeros)-1):
    if numeros[c] % 2 == 0:
        par.append(numeros[c])
    else:
        impar.append(numeros[c])

print("-="*30)
print(f"Os numeros digitados foram: {numeros}")
print(f"Os valores pares foram: {par}")
print(f"Os valores impares foram: {impar}")
