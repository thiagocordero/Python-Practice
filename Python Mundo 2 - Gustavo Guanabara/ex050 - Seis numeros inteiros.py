s = 0
t = 0
for c in range(1, 7):
    n = int(input('Digite o {}o número inteiro: '.format(c)))
    if (n % 2 == 0) :
        s = s + n
        t = t +1
print('A soma dos {} numeros pares digitados é: {}'.format(t, s))

