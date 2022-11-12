frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
#inverso = junto[::-1)

print(' Você digitou a frase {} \n O contrario é: {}'.format(junto, inverso))

if junto == inverso :
    print(' É PALÍNDROMO!')
else :
    print(' NÃO É PALINDROMO!')