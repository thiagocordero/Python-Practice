'''Exercício Python 102: Crie um programa que tenha uma função fatorial()
que receba dois parâmetros: o primeiro que indique o número a calcular e
outro chamado show, que será um valor lógico (opcional) indicando se será
mostrado ou não na tela o processo de cálculo do fatorial.'''


def fatorial(num, show=False):
    """
    --> Calcula fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do fatorial de um número num.
    """
    tot = 1
    for c in range(num, 0, -1):
        tot *= c
        if show:
            if c > 1:
                print(f"{num} x ", end='')
            else:
                print(f"{num} = ", end='')
    return tot


print(fatorial(4, True))
help(fatorial)


