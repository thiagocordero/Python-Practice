maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(' Digite o peso da {}°a pessoa: '.format(c)))
    if peso > maior:
        maior = peso
    if peso < menor or menor == 0:
        menor = peso
print('Dos 5 valores digitados: \n O maior é {}Kg \n O menor é: {}Kg.'.format(maior, menor))
