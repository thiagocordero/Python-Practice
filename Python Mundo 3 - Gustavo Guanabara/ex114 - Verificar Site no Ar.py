'''Exercício Python 114: Crie um código em Python que teste se o site pudim
está acessível pelo computador usado.'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://pudim.com.br/")
except urllib.error.URLError:
    print("O site Pudim não está acessível nesse momento.")
else:
    print("Consegui acessar o site Pudim com sucesso.")