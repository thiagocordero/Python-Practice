'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
 O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
 consecutivas que ele conquistou no final do jogo.'''
from random import randint
vitorias = 0
print("=-="* 20)
print("JOGO DO PAR OU IMPAR")
print("=-="* 20)

while True:
    computador = randint(0, 5)

    jogador = int(input("Digite um número de 0 a 5: "))
    while jogador < 0 or jogador > 5:
        jogador = int(input("Escolha um número de 0 a 5: "))

    tipo = str(input("Par ou Impar [P/I] ? ").upper().strip()[0])
    while tipo not in "PpIm":
        tipo = str(input("Par ou Impar [P/I] ? ").upper().strip()[0])

    total = jogador + computador

    print("=-="*20)
    print(f"Você jogou {jogador} e o computador jogou {computador}! Total de {total}")
    print("Deu PAR!" if total % 2 == 0 else "Deu IMPAR!", end='')

    if tipo == 'P':
        if total % 2 == 0:
            print(" Você ganhou! :) ")
            vitorias += 1
        else:
            print(" Você perdeu. :( ")
            break
    elif tipo == "I":
        if total % 2 != 0:
            print(" Você ganhou! :)")
            vitorias += 1
        else:
            print(" Você perdeu. :( ")
            break
    print("Vamos jogar novamente...")
print(f"GAME OVER!! Voce venceu {vitorias} vezes!")








