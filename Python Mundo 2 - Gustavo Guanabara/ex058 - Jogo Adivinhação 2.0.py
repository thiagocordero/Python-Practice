import random

print('-×-'*20)
print('VOU PENSAR EM UM NUMERO ENTRE 0 E 10, TENTE ADIVINHAR!')

sorteio = random.randint(0,10)
n = int(input('Qual seu palpite? '))

tentativas = 1
while n != sorteio:
    if n < sorteio:
        n = int(input('Mais... QUal seu palpite? '))
        tentativas += 1
    if n > sorteio:
        n = int(input('Menos... Qual seu palpite? '))
        tentativas += 1

if tentativas == 1:
    print('Você GANHOU! Foi {} tentativa para acertar.'.format(tentativas))
else:
    print('Você GANHOU! Foram {} tentativas para acertar.'.format(tentativas))