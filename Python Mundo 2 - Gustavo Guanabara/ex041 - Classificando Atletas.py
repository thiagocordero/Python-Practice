from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento do atleta: '))
idade = atual - nasc

if idade <= 9 :
    print('Você tem {} anos, categoria MIRIM.'.format(idade))
elif 9 < idade <= 14 :
# (idade <= 14) tambem funciona porque pra chegar aqui ja nao executou a de cima
    print('Você tem {} anos, categoria INFANTIL.'.format(idade))
elif 14 < idade <= 19 :
    print('Você tem {} anos, categoria JÚNIOR.'.format(idade))
elif 19 < idade <= 25 :
    print('Você tem {} anos, categoria SÊNIOR.'.format(idade))
elif idade > 25 :
    print('Você tem {} anos, categoria MASTER.'.format(idade))