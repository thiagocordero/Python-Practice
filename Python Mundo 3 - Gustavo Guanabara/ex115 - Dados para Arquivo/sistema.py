'''Exercício 115: Crie um pequeno sistema modularizado que permita cadastrar
pessoas pelo seu nome e idade em um arquivo de texto simples. O sistema só vai
ter 2 opções: CADASTRAR uma nova pessoa e LISTAR todas as pessoas cadastradas.'''

from library.interface import *
from library.arquivo import *
from time import sleep

arquivo = 'cadastroTeste.txt'

if not arquivoExiste(arquivo):
    criarArquivo('cadastroTeste.txt')

while True:
    resposta = menu(["Listar Pessoas Cadastradas", "Cadastrar Pessoa", "Sair do Sistema"])
    if resposta == 1:
        titulo("PESSOAS CADASTRADAS")
        listarPessoas(arquivo)
    elif resposta == 2:
        titulo("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        titulo("Saindo do sistema... Até logo!")
        break
    else:
        print("\033[0;31mERRO! Digite uma opção válida.\033[m")
    sleep(2)





