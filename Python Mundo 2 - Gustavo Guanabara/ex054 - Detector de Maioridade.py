from datetime import date
ano_atual = date.today().year
maiores = 0
menores = 0
for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da PESSOA {}: '.format(c)))
    idade = ano_atual - nasc
    if idade >= 18 :
        maiores += 1
    else :
        menores += 1
        
print(' {} pessoas são maiores de idade. \n {} pessoas são menores de idade.'.format(maiores, menores))