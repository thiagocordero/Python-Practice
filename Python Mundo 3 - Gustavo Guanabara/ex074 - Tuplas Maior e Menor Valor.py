'''Exercício Python 074: Crie um programa que vai gerar cinco números
aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print("-="*15)
print(f"Numeros sorteados foram: {numeros}")
print("-="*15)
print(f"O maior valor sorteado foi: {max(numeros)}")
print("-="*15)
print(f"O menor valor sorteado foi: {min(numeros)} ")
print("-="*15)
