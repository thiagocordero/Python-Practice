'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias
pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

maior18 = homens = mulherMenor20 = 0
while True:
    idade = int(input("Idade: "))
    sexo = str(input("Sexo[M/F/NB]: ")).strip().upper()
    while sexo != "M" and sexo != "NB" and sexo != "F":
        sexo = str(input("Inválido! Sexo[M/F/NB]: ")).strip().upper()

    if idade > 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == "F" and idade < 20:
        mulherMenor20 += 1

    option = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
    while option not in "SN":
        option = str(input("Inválido! Deseja continuar? [S/N]: ")).strip().upper()[0]
    if option == 'N':
        break
        
print("=-="*10)
print(f'''Foram cadastrados: 
>>> {maior18} pessoas com mais de 18 anos
>>> {homens} homens 
>>> {mulherMenor20} mulheres com menos de 20 anos''')
print("=-="*10)






