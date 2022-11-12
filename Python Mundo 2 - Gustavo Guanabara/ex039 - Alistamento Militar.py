from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Estamos em {}. \n Você nasceu em {} e tem {} anos.'.format(atual, nasc, idade)) 

if idade == 18 :
    print('Você precisa se alistar ESTE ANO!')
elif idade > 18:
    saldo = idade - 18
    print('Ja passou seu prazo para se alistar. \n Seu alistamento foi há {} anos.'.format(idade - 18))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
elif idade < 18:
    saldo = 18 - idade
    print('Você precisa se alistar daqui a {} anos.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento foi em {}'.format(ano))