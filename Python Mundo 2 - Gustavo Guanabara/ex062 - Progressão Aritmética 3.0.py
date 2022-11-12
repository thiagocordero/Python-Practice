'''Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário
se ele quer mostrar mais alguns termos. O programa encerrará quando ele
disser que quer mostrar 0 termos.'''

print("GERADOR DE PA")
print("=-="*10)

primeiro = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão da PA? '))
termo = primeiro

c = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while c <= total:
        print('{} >>> '.format(termo), end='')
        termo += razao
        c += 1
    print("PAUSA")

    mais = int(input("Quantos termos você quer ver a mais? "))
print("FIM")

print("Progressão Finalizada com {} termos mostrados.".format(total))