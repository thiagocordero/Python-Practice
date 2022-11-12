nome = str(input('Digite seu nome completo: ')).strip().upper()
divide = nome.split()
print('Primeiro nome: {}'.format(divide[0]))
print('Último nome: {}'.format(divide[-1]))
