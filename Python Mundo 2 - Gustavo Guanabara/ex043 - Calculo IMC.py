altura = float(input('Altura: '))
peso = float(input('Peso: '))
imc = peso / (altura ** 2) #poderia ser sem parênteses, potenciação tem precedencia sobre divisão 
print('Você tem {}m de altura e {}Kg.'.format(altura, peso))
print('Seu IMC é de {:.2f} e você está: '.format(imc), end= ' ')

if imc <= 18.5 :
    print('ABAIXO DO PESO')
elif imc <= 25 :
    print('PESO IDEAL')
elif imc <= 30 :
    print('SOBREPESO')
elif imc <= 40 :
    print('OBESIDADE')
else :
    print('OBESIDADE MÓRBIDA')