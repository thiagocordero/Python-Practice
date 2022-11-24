'''Exercício Python 100: Faça um programa que tenha uma lista chamada
números e duas funções chamadas sorteia() e somaPar(). A primeira função vai
sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
mostrar a soma entre todos os valores pares sorteados pela função anterior.'''

from random import randint
from time import sleep
numeros = list()


def sortear():
    print("Sorteandos os 5 valores da lista: ", end='')
    for i in range(0, 5):
        n = randint(0, 10)
        sleep(0.5)
        print(n, end=' ')
        numeros.append(n)
    print("PRONTO!")
    sleep(0.5)
    print(f"A lista de números sorteados foi: {numeros}")


def somaPar():
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    print(f"A soma dos números pares é: {soma}")




sortear()
somaPar()