'''Exercício Python 104: Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante ‘a função input() do Python, só que
fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)'''


def leia_int(txt):
    while True:
        n = input(txt)
        if n.isnumeric():
            return int(n)
            break
        else:
            print("INVÁLIDO")


numero = leia_int("Digite um número: ")
print(f"Você digitou o numero {numero}")
