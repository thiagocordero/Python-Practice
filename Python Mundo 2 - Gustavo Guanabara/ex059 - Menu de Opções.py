# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

option = 0
while option != 5:

    print('''    [1] SOMAR 
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR''')
    option = int(input("Digite sua opção: "))

    if option == 1:
        soma = num1 + num2
        print(" O resultado de {} + {} = {}".format(num1, num2, soma))
    elif option == 2:
        produto = num1 * num2
        print(" O resultado de {} x {} = {}".format(num1, num2, produto))
    elif option == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print("Entre {} e {}, o maior é {}".format(num1, num2, maior))
    elif option == 4:
        print("Informe os números novamente: ")
        num1 = int(input("Digite o novo primeiro número: "))
        num2 = int(input("Digite o novo segundo número: "))
    elif option == 5:
        print("Finalizando...")
    else:
        print("Opção inválida! Tente novamente.")
    print("=-="*10)
    sleep(2)
