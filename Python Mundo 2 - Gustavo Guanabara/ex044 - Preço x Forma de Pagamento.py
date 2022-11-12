print('\n')
print('{:=^40}'.format(' TIGER LANGUAGES '))
valor = float(input('Preço das compras: R$'))
print(''' \n FORMAS DE PAGAMENTO
[1] A VISTA: Dinheiro/Cheque
[2] A VISTA: Cartão
[3] 2x no Cartão
[4] 3x ou + no Cartão''')

formaPagamento = int(input('Forma de pagamento: '))


if formaPagamento == 1 :
    total = valor - (valor*10/100)
elif formaPagamento == 2 :
    total = valor - (valor*5/100)
elif formaPagamento == 3 :
    total = valor
    print('Serão 2x de R${:.2f}'.format(valor/2))
elif formaPagamento == 4 :
    total = valor + (valor*20/100)
    parcelas = int(input('Quantas parcelas? '))    
    print('Serão {}x de R${:.2f}.'.format(parcelas, total/parcelas))
else :
    print('Você nao digitou um valor válido. Tente novamente.')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, total))