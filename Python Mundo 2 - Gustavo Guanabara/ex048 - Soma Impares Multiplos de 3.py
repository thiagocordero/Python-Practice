acumulador = 0
contador = 0
for n in range(1,501, 2) :
    if n % 3 == 0:
        acumulador += n
        contador += 1
print('A soma dos {} valores multiplos de 3 é: {}'.format(contador, acumulador))