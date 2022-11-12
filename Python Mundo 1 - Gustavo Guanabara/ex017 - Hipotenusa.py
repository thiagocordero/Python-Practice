import math
c1 = float(input('Qual o valor do 1o cateto? '))
c2 = float(input('Qual o valor do 2o cateto? '))
h = math.hypot(c1, c2)
print('Para catetos de {} e {}, a hipotenusa vale {:.2f}'.format(c1, c2, h))