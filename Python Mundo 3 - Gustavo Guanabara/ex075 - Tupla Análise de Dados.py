'''Exercício Python 075: Desenvolva um programa que leia quatro valores
pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
valores = (n1, n2, n3, n4)

print(f"Você digitou os valores: {valores}")
#A) Quantas vezes apareceu o valor 9.
if valores.count(9) == 1:
    print(f"O número 9 apareceu {valores.count(9)} vez")
else:
    print(f"O número 9 apareceu {valores.count(9)} vezes")

#B) Em que posição foi digitado o primeiro valor 3.
if 3 in valores:
    print(f"O primeiro número 3 apareceu na {valores.index(3)+1}° posição")
else:
    print("O número 3 não foi digitado.")

#C) Quais foram os números pares.
print("Os valores pares foram: ", end='')
for v in valores:
    if v % 2 == 0:
        print(v, end=' ')
