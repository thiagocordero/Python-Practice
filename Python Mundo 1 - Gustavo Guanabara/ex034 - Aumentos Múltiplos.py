salario = float(input('Digite o valor do salario: R$'))
if salario > 1250:
    aumento = (10*salario)/100
else:
    aumento = (15*salario)/100
    
print('O salario de R${:.2f} terá um aumento de R${:.2f}'.format(salario, aumento))
print('O novo salario é de: R${:.2f}'.format(salario+aumento))
