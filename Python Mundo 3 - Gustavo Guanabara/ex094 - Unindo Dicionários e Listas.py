'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de
várias pessoas, guardando os dados de cada pessoa em um dicionário e todos
os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

todos = []
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Nome: "))
    while True:
        pessoa['sexo'] = str(input("Sexo [M/F]: ")).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print("SEXO INVÁLIDO! Digite M ou F")
    pessoa['idade'] = int(input("Idade: "))
    soma += pessoa['idade']
    todos.append(pessoa.copy())

    while True:
        option = str(input("Deseja continuar[S/N]? ")).upper()[0]
        if option in 'SN':
            break
        else:
            print("INVÁLIDO! Digite S ou N")
    if option in 'N':
        break

print("=-"*30)

#A) Quantas pessoas foram cadastradas
print(f"Foram cadastradas {len(todos)} pessoas")
print("-"*20)

#B) A média de idade
media = soma / len(todos)
print(f"A média de idades foi {media:.2f}")
print("-"*20)

#C) Uma lista com as mulheres
print("As mulheres cadastradas foram: ")
for p in todos:
    if p['sexo'] == 'F':
        print(f"[{p['nome']}]", end='')
print()
print("-"*20)

#D) Uma lista de pessoas com idade acima da média
print("As pessoas com idade acima da média são: ")
for p in todos:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f"{k} = {v}")
        print()
print("-"*20)
print("=-"*30)
print('<<< ENCERRADO >>>')

