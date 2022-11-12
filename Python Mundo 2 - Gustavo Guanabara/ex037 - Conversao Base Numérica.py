n = int(input('Digite um número inteiro: '))
print('-'*10)
print('CONVERSÃO DE BASES NUMÉRICAS')
print('[ 1 ] para BINÁRIO')
print('[ 2 ] para OCTAL')
print('[ 3 ] para HEXADECIMAL')
conversao = int(input('Sua opção: '))

if conversao == 1 :
    print('{} convertido em BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif conversao == 2 :
    print('{} convertido em OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif conversao == 3 :
    print('{} convertido em HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Você não digitou um numero valido')
