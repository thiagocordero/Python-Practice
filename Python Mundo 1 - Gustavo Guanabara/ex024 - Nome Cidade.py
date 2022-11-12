cidade = str(input('Digite o nome de uma cidade: ')).strip()
cidade = cidade.upper()
print('O nome da cidade é {}'.format(cidade))
print('Tem SANTO no nome? {}'.format(cidade[:5]=='SANTO'))