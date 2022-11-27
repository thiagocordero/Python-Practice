'''Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help
do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o
usuário digitar a palavra ‘FIM’, o programa se encerrará.
Importante: use cores.'''
from time import sleep
cores = ['\033[0;0m', '\033[0;30;44m', '\033[1;31m', '\033[1;34m', '\033[0;32m', '\033[;1m', '\033[1;36m', '\033[7;30m', '\033[0;30;45m']


def ajuda(txt):
    titulo(f"Acessando o comando {txt.upper()}...", 4)
    print(cores[-1])
    help(txt)
    print(cores[0])
    sleep(2)


def titulo(txt, cor=0):
    tam = len(txt)+4
    print(cores[cor], end='')
    print("~" * tam)
    print(f"  {txt}  ")
    print("~" * tam)
    print(cores[0], end='')
    sleep(1)


comando = ''
while True:
    titulo("SISTEMA DE AJUDA PYHELP", 1)
    comando = str(input("Função ou Biblioteca >>> "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
sleep(1)
titulo("ATÉ LOGO!", 2)
