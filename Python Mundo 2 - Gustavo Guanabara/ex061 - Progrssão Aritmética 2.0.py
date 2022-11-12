#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de
#uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print("GERADOR DE PA")
print("=-="*10)

primeiroTermo = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão da PA? '))

termo = primeiroTermo
c = 1
while c <= 10:
    print('{} >>> '.format(termo), end='')
    termo += razao
    c += 1
print("FIM")
