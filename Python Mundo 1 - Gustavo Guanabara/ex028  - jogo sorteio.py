import random
import time

##lista = [1, 2, 3, 4, 5]
##sorteio = random.choice(lista)
sorteio = random.randint(0,5)
print('-×-'*20)
print('VOU PENSAR EM UM NUMERO ENTRE 0 E 5, TENTE ADIVINHAR!')
n = int(input('Digite um numero de 0 a 5: '))

print('PROCESSANDO...')
time.sleep(2)

if n==sorteio :
    print('Você GANHOU! Eu pensei no mumero {}.'.format(sorteio))
else:
    print(sorteio)
    print('Voce PERDEU! Eu pensei no número {}, e não no {}'.format(sorteio, n))
    