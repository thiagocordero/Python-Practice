'''Exercício Python 078: Faça um programa que leia 5 valores numéricos
e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições na lista.'''

valores = []
maior = menor = 0
for c in range(0, 5):
    valores.append(int(input(f"Digite o valor da Posição {c}: ")))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print(f"Os valores digitados foram: {valores}")
print(f"O maior valor digitado foi {maior} na(s) posição(ões) ", end='')
for i, v in enumerate(valores):
    if v == maior:
        print(i, end=' ')
print(f"\nO menor valor digitado foi {menor} na(s) posição(ões) ", end='')
for i, v in enumerate(valores):
    if v == menor:
        print(i, end=' ')



