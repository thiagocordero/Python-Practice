km = float(input('Digite a distância em km: '))
custo = km * 0.45 if km > 200 else km * 0.5

'''if km > 200 :
    custo = km * 0.45
else:
    custo = km * 0.5'''
    
print('O custo da viagem será de: R${:.2f}'.format(custo))
