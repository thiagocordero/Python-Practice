'''Exercício Python 101: Crie um programa que tenha uma função chamada
voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL
e OBRIGATÓRIO nas eleições.'''


def voto(ano_nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        return f"NÃO VOTA! Você tem {idade}anos, mas precisa ter pelo menos 16 anos para votar."
    elif 16 <= idade < 18 or idade > 65:
        return f"VOTO OPCIONAL! Você tem {idade} anos e pode decidir votar ou não."
    elif 18 <= idade <= 65:
        return f"VOTO OBRIGATÓRIO! Você tem {idade} anos e é obrigado a votar."


#Programa Principal

print("=-"*20)
print("INFORMAÇÕES SOBRE A VOTAÇÃO")
print("=-"*20)
anoNascimento = int(input("Digite o seu ano de nascimento: "))

print(voto(anoNascimento))

