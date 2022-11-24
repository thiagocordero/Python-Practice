'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com
vários jogadores, incluindo um sistema de visualização de detalhes do
aproveitamento de cada jogador.'''

todosJogadores = list()
jogador = dict()

while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome do Jogador: "))
    numPartidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    jogador['gols_por_partida'] = []
    for i in range(1, numPartidas+1):
        jogador['gols_por_partida'].append(int(input(f">>> Gols na Partida {i}: ")))
    jogador['total_gols'] = sum(jogador['gols_por_partida'])
    todosJogadores.append(jogador.copy())
    while True:
        option = str(input("Deseja continuar[S/N]? ")).upper()[0]
        if option in 'SN':
            break
        print("ERRO! Digite apenas S ou N")
    if option == "N":
        break

print("=-"*30)
print(f"{'JOGADORES DE FUTEBOL':^30}")
print("=-"*30)

print(f"{'COD':^5}{'NOME':^15}{'GOLS':^15}{'TOTAL':^15}")
for key, value in enumerate(todosJogadores):
    print(f"{key+1:^5}", end='')
    for d in value.values():
        print(f"{str(d):^15}", end='')
    print()

while True:
    busca = int(input("Mostrar dados de qual jogador? (999 parar) "))
    if busca == 999:
        break
    if busca-1 >= len(todosJogadores):
        print(f"ERRO! Não existe jogador com código {busca}")
    else:
        print(f"<<< LEVANTAMENTO JOGADOR {todosJogadores[busca-1]['nome'].upper()} >>>")
        for i, gols in enumerate(todosJogadores[busca-1]['gols_por_partida']):
            if gols == 1:
                print(f" >>> No jogo {i + 1} fez {gols} gol")
            else:
                print(f" >>> No jogo {i+1} fez {gols} gols")
    print("-"*30)
print("<<< VOLTE SEMPRE >>>")

