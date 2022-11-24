'''Exercício Python 090: Faça um programa que leia nome e média de um
aluno, guardando também a situação em um dicionário. No final, mostre
o conteúdo da estrutura na tela.'''

aluno = dict()
aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))
if aluno['media'] >= 7:
    aluno['situação'] = "APROVADO(A)"
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = "RECUPERAÇÃO"
else:
    aluno['situação'] = "REPROVADO(A)"

'''print("-"*30)
print(f"NOME: {aluno['nome']}")
print(f"MÉDIA: {aluno['media']}")
print(f"SITUAÇÃO: {aluno['situação']}")
print("-"*30)'''

print("-"*30)
print(f"{'NOME':<10}{'MÉDIA':<5}{'SITUAÇÃO':^15}")
print(f"{aluno['nome']:<10}{aluno['media']:<5}{aluno['situação']:^15}")


