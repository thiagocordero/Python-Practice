def leiadinheiro(msg):
    valid = False
    while not valid:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mErro! "{entrada}" é um preço inválido! Tente novamente\033[m')
        else:
            valid = True
            return float(entrada)

def leia_int(txt):
    while True:
        n = input(txt)
        if n.isnumeric():
            return int(n)
            break
        else:
            print("INVÁLIDO")
