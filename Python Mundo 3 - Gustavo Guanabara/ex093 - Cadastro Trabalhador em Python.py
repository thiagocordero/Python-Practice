'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento
 e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por
 acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano
 de contratação e o salário. Calcule e acrescente, além da idade, com
 quantos anos a pessoa vai se aposentar.'''
from datetime import datetime

trabalhador = dict();
trabalhador['nome'] = str(input("Nome: "))
trabalhador['idade'] = datetime.today().year - int(input("Ano de Nascimento: "))
trabalhador['ctps'] = int(input("CTPS (0 se não possuir): "))
if trabalhador['ctps'] != 0:
    trabalhador['ano_contratação'] = int(input("Ano de Contratação: "))
    trabalhador['salario'] = float(input("Salário: "))
    trabalhador['idade_aposentadoria'] = trabalhador['idade'] + (trabalhador['ano_contratação'] + 35) -datetime.today().year


print("=-"*30)
print(">>> DADOS CADASTRADOS:")
for k, v in trabalhador.items():
    print(f"{k}: {v}")
