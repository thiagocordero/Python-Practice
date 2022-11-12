n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

if media < 5 :
    print('REPROVADO. Sua média foi de {}.'.format(media))
elif (media >= 5) and (media <= 6.9) :
    print('EM RECUPERAÇÃO. Sua média foi de {}.'.format(media))
else :
    print('APROVADO. Sua média foi de {}.'.format(media))