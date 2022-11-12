s = float(input('Qual o salário do funcionário? R$'))
aumento = float(input('Qual a porcentagem de aumento? '))
sf = s + (s*aumento/100)
print('O salário atualizado, com aumento de {}% é de R${}.'.format(aumento, sf))
