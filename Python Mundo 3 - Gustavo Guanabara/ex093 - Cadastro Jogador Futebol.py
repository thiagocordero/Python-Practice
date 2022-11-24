'''Exercício Python 093: Crie um programa que gerencie o aproveitamento
de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas
ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols feitos
durante o campeonato.'''

jogador = dict()
jogador['nome'] = str(input("Nome do Jogador: "))
numPartidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

jogador['gols_por_partida'] = []
for i in range(1, numPartidas+1):
    jogador['gols_por_partida'].append(int(input(f">>> Gols na Partida {i}: ")))

jogador['total_gols'] =sum(jogador['gols_por_partida'])

print("=-"*30)
print(f"O jogador {jogador['nome']} jogou {numPartidas} partidas.")
for partida, gols in enumerate(jogador['gols_por_partida']):
    if gols == 1:
        print(f"   >>> Na partida {partida+1} fez {gols} gol")
    else:
        print(f"   >>> Na partida {partida + 1} fez {gols} gols")
print(f"O total de gols foi de {jogador['total_gols']}")

