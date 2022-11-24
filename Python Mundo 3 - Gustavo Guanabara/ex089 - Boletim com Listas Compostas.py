'''Exercício Python 089: Crie um programa que leia nome e duas notas de
vários alunos e guarde tudo em uma lista composta. No final, mostre um
boletim contendo a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individualmente.'''

boletim = []
while True:
    nome = str(input("Nome do aluno: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2)/2
    boletim.append([nome, [nota1, nota2], media])

    option = str(input("Gravado com sucesso! Deseja continuar[S/N]? ")).upper()[0]
    if option in "Nn":
        break

print("=-"*30)
print(f"{'BOLETIM':^30}")
print("=-"*30)
print(f"{'NUM':<5}{'NOME':^10}{'MÉDIA':>8}")
print("-"*30)
for i, a in enumerate(boletim):
    print(f"{i+1:<5}{a[0]:^10}{a[2]:>8.1f}")
while True:
    print("-"*30)
    individual = int(input("Mostrar notas de qual número [999 interrompe]? "))
    if individual == 999:
        print("FINALIZANDO...")
        break
    if individual <= len(boletim):
        print(f"O aluno {boletim[individual-1][0]} tirou {boletim[individual-1][1]}")
print("<<< VOLTE SEMPRE >>>")



