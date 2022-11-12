'''Exercício Python 65: Crie um programa que leia vários números inteiros
pelo teclado. No final da execução, mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos. O programa deve perguntar ao
usuário se ele quer ou não continuar a digitar valores.'''

soma = contador = media = maior = menor = 0
option = "S"
while option != "N":
    n = int(input("Digite um numero: "))
    soma += n
    contador += 1

    if contador == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    option = str(input("Deseja continuar(S/N)? ").upper())
media = soma / contador
print("Foram digitados {} numeros e a media entre eles é de {}".format(contador, media))
print("O menor valor lido foi {} e o maior valor foi {}".format(menor, maior))












