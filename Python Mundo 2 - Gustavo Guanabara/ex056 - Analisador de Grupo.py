tot_idade = 0
maisvelho = 0
nome_maisvelho = ''
m20 = 0
for c in range (1, 5):
    nome = str(input(' PESSOA {} - Nome: '.format(c)))
    idade = int(input(' PESSOA {} - Idade: '.format(c)))
    sexo = str(input(' PESSOA {} - Gênero(H/M/NB): '.format(c))).upper()
    tot_idade += idade
    if sexo == 'H' and idade > maisvelho:
        maisvelho = idade
        nome_maisvelho = nome
    if sexo == 'M' and idade < 20:
        m20 += 1

media = tot_idade / 5
print('A media de idades do grupo é {}'.format(media))
print('O homem mais velho é {}'.format(nome_maisvelho))
print(' {} mulheres tem menos de 20 anos.'.format(m20))
