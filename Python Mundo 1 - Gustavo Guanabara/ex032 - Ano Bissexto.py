from datetime import date
print('-'*10)
print('ANO BISSEXTO OU NÃO?')
print('-'*10)
ano = int(input('Digite um ano para analisar ou 0 para o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print('O ano {} É BISSEXTO! \n Fevereiro tem 29 dias.'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO \n Fevereiro tem 28 dias.'.format(ano))
    
