import random
from time import sleep

print('\n')
print('{:=^40}'.format(' PEDRA, PAPEL, TESOURA '))
print('''
[1] PEDRA
[2] PAPEL
[3] TESOURA ''')

jogador = int(input('\nQual a sua opção? '))   
options = [' ', 'PEDRA', 'PAPEL', 'TESOURA']
computador = random.randint(1,3)
print('{}'.format(' JO'))
sleep(1)
print('{}'.format(' KEN'))
sleep(1)
print('{}'.format(' PO!!!'))
sleep(1)

print('-='*10)
print('\n Você jogou {} \n O computador jogou {}.\n'.format(options[jogador], options[computador]))
print('-='*10)
print('\n')

if jogador == computador :
    print(' EMPATE! 🙃 ')
elif jogador == 1 and computador == 2 :
    print(' VOCÊ PERDEU... 😭')
elif jogador == 1 and computador == 3 :
    print(' VOCÊ GANHOU! 😀')
elif jogador == 2 and computador == 1 :
    print(' VOCÊ GANHOU! 😀')
elif jogador == 2 and computador == 3 :
    print(' VOCÊ PERDEU... 😭')
elif jogador == 3 and computador == 1 :
    print(' VOCÊ PERDEU... 😭')
elif jogador == 3 and computador == 2 :
    print(' VOCÊ GANHOU 😀')   
