l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 2: '))

if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('PODE formar triângulo')
else:
    print('NÃO PODE formar triângulo')