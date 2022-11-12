n1 = int(input('Digite o 1o valor: '))
n2 = int(input('Digite o 2o valor: '))
n3 = int(input('Digite o 3o valor: '))

menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
    
print('Maior Valor: {} \n Menor Valor: {}'.format(maior, menor)) 
