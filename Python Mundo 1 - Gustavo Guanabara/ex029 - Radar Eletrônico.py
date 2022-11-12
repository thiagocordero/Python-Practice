from time import sleep
print('-'*10)
print('O LIMITE DE VELOCIDADE É 80KM/H')
print('-'*10)
carro = int(input('Digite a velocidade do carro: '))
if carro > 80:
    multa = (carro - 80) * 7
    print('PROCESSANDO...')
    sleep(2)
    print('MULTADO! O carro estava {}km/h acima do limite de velocidade. \n A multa é de R${:.2f}'.format((carro - 80), (carro - 80)*7))
print('Tenha um bom dia, dirija com segurança!')