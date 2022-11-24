'''Exercício Python 098: Faça um programa que tenha uma função chamada
contador(), que receba três parâmetros: início, fim e passo. Seu programa
tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''


def contador(inicio, fim, passo):
    if passo < 0:
        passo = abs(passo)
    if passo == 0:
        passo = 1
    print("-=" * 30)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}: ")
    if inicio < fim:
        while inicio <= fim:
            sleep(0.5)
            print(inicio, end=' ')
            inicio += passo
        sleep(0.5)
        print("FIM!")
    elif fim < inicio:
        while fim <= inicio:
            sleep(0.5)
            print(inicio, end=' ')
            inicio -= passo
        sleep(0.5)
        print("FIM!")


from time import sleep

contador(1, 10, 1)
contador(10, 0, 2)
print("-=" * 30)
print("Agora é sua vez de personalizar a contagem!")
contador(
    int(input("Início: ")),
    int(input("Fim: ")),
    int(input("Passo: "))
)
