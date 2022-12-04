def leiaInt(txt):
    while True:
        try:
            n = int(input(txt))
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")
        else:
            return n


def linha(tam=42):
    return "-" * tam


def titulo(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    titulo("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c += 1
    print(linha())
    option = leiaInt("\033[32mDigite uma opção: \033[m")
    return option

