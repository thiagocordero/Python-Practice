salario = float(input('Qual o salário da pessoa? '))
valor = float(input('Qual o valor do empréstimo? '))
tempo = float(input('Em quantos anos vai pagar? '))

parcela = valor / (tempo * 12)
maximo_parcela = (30*salario) / 100
if parcela >= maximo_parcela :
    print('EMPRÉSTIMO NÃO AUTORIZADO')
else:
    print('EMPRÉSTIMO APROVADO')
    print('{} parcelas de R${}.'.format(tempo*12, parcela))  