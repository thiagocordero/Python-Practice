'''Exercício Python 72: Crie um programa que tenha uma dupla totalmente
preenchida com uma contagem por extenso, de zero até vinte. Seu programa
deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

contagem = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete",
            "oito", "nove", "dez", "onze", "doze", "treze", "catorze", "quinze",
            "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    n = int(input("Digite um número entre 0 e 20: "))
    while n < 0 or n > 20:
        n = int(input("Número inválido! Digite um número entre 0 e 20: "))
    print(f"Você digitou o número {contagem[n]}")

    option = str(input("Deseja continuar[S/N]? ")).upper()[0]

    if option == "N":
        break;
