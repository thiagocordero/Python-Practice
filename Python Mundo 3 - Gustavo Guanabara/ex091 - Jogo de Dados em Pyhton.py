'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um
dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário
em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor
tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter

resultados = dict()
ranking = list()

print("O JOGO COMEÇOU! \n>>>Valores dos Dados: ")
for n in range(1, 11):
    sleep(1)
    dado = randint(1, 6)
    resultados[f'Jogador {n}'] = dado
    print(f"Jogador {n}: Tirou {dado}")

#Ordenando o Dicionário
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print(">>> Ranking dos Jogadores: ")
for i, value in enumerate(ranking):
    sleep(1)
    print(f"{i+1}° lugar: {value[0]} com {value[1]} pontos")
