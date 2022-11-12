'''Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999, que é a condição
 de parada. No final, mostre quantos números foram digitados e qual foi a soma
 entre elas (desconsiderando o flag).'''

n = soma = contador = 0
while True:
    n = int(input("Digite um número [999 para sair]: "))
    if n == 999:
        print("Finalizando...")
        break
    soma += n
    contador += 1
print(f"Foram digitados {contador} números e a soma de todos eles é {soma}")