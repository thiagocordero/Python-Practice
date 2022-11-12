n = int(input(' Digite um número inteiro: '))
divisivel = 0
for c in range(1, n+1 ):
    if n % c == 0:
        divisivel = divisivel + 1
        print('\033[33m', end='')
    else :
        print('\033[32m', end='')
    print(' {} '.format(c), end='')
print('\n\033[m O número {} foi divisível {} vezes'.format(n, divisivel))

if divisivel <= 2 :
    print(' \n É um numero PRIMO!')
else :
    print(' \n Não é primo.')
