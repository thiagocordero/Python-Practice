'''Exercício Python 099: Faça um programa que tenha uma função chamada
maior(), que receba vários parâmetros com valores inteiros. Seu programa
tem que analisar todos os valores e dizer qual deles é o maior.'''


def maior(* num):
    maior = menor = 0
    print("-="*30)
    print("Analisando os valores passados", end='')
    for i in range(1, 4):
        sleep(0.5)
        print(".", end='')
    print()
    sleep(0.5)
    print(f"{num} Foram passados {len(num)} números ao todo.")
    for i in range(0, len(num)):
        if i == 0:
            menor = num[i]
            maior = num[i]
        else:
            if num[i] < menor:
                menor = num[i]
            if num[i] > maior:
                maior = num[i]
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")


from time import sleep

maior(2, 31, 64, 92, 31, 9, 104, 232)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)