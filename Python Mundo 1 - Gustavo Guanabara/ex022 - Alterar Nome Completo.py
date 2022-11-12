nome = str(input('Qual é seu nome completo? ')).strip()
print('Nome Maiusculo: {}'.format(nome.upper()))
print('Nome Minusculo: {}'.format(nome.lower()))
letras = len(nome) - nome.count(' ')
print('Número de Letras: ', letras)
dividido = nome.split()
print('Letras no primeiro nome: ', len(dividido[0]))


