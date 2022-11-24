'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA
SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em
uma lista composta.'''

from random import randint
from time import sleep

print("-"*30)
print(f'{"JOGOS MEGA SENA":^30}')
print("-"*30)
jogo = []
todosJogos = []
numJogos = int(input("Quantos jogos da MEGA SENA deseja sortear? "))
totJogos = 0

while totJogos < numJogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont == 6:
            break
    jogo.sort()
    todosJogos.append(jogo[:])
    jogo.clear()
    totJogos += 1

print("\n", "-="*5 , f"SORTEANDO {numJogos} JOGOS", "-="*5)

for jogo, lista in enumerate(todosJogos):
    print(f"Jogo {jogo+1}: {lista}")
    sleep(1)

print("-="*5, f"< BOA SORTE! >", "-="*5)
