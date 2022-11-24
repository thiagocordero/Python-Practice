'''Exercício Python 081: Crie um programa que vai ler vários números e
colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
while True:
    lista.append(int(input("Digite um número: ")))
    option = str(input("Deseja continuar[S/N] ?"))[0]
    if option in 'Nn':
        break
print("-="*30)
print(f"Os números digitados foram: {lista}")
print("-="*30)
#A) Quantos números foram digitados.
print(f"Foram digitados: {len(lista)} números.")
#B) A lista de valores, ordenada de forma decrescente.
print(f"Os números digitados em ordem decrescente: {lista.sort(reverse=True)}")
#C) Se o valor 5 foi digitado e está ou não na lista.
if 5 in lista:
    print("O número 5 ESTÁ na lista!")
else:
    print("O número 5 NÃO ESTÁ na lista.")
print("-="*30)
