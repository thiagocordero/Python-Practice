'''Exercício Python 103: Faça um programa que tenha uma função chamada
ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha
do jogador, mesmo que algum dado não tenha sido informado corretamente.'''


def ficha(nome_jogador='<desconhecido>', num_gols=0):
    if num_gols == 1:
        return f"O jogador {nome_jogador} fez {num_gols} gol no campeonato."
    else:
        return f"O jogador {nome_jogador} fez {num_gols} gols no campeonato."


nome = str(input("Nome do Jogador: "))
gol = str(input("Número de Gols: "))

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if nome.strip() == '':
   print(ficha(num_gols=gol))
else:
   print(ficha(nome, gol))

