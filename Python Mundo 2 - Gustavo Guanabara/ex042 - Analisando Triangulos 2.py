l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 2: '))

if l1<l2+l3 and l2<l1+l3 and l3<l1+l2:
    print('PODE formar um', end=' ')
    if (l1 == l2) and (l2 == l3) :
        print('TRIÂNGULO EQUILÁTERO')
    elif (l1 == l2) or (l2 == l3) :
        print('TRIÂNGULO ISÓSCELES')
    elif (l1 != l2) and (l2 != l3) :
        print('TRIÂNGULO ESCALENO')
else:
    print('NÃO PODE formar triângulo')


