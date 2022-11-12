'''Exercício Python 071: Crie um programa que simule o funcionamento de um
caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser
sacado (número inteiro) e o programa vai informar quantas cédulas de cada
valor serão entregues. OBS: considere que o caixa possui cédulas de
R$50, R$20, R$10 e R$1.'''

print("="*30)
print("{:^30}".format("BANCO TIGER"))
print("="*30)

saque = int(input("Qual valor deseja sacar? R$"))

notas1 = notas10 = notas20 = notas50 = 0


while saque >= 50:
    notas50 += 1
    saque -= 50
while saque >= 20:
    notas20 += 1
    saque -= 20
while saque >= 10:
    notas10 += 1
    saque -= 10
while saque >= 1:
    notas1 += 1
    saque -= 1

print(f'''Você receberá: 
{notas50} notas de R$50
{notas20} notas de R$20
{notas10} notas de R$10
{notas1} notas de R$1''')
