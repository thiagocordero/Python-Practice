'''Exercício Python 110: Adicione o módulo moeda.py criado nos desafios
anteriores, uma função chamada resumo(), que mostre na tela algumas informações
geradas pelas funções que já temos no módulo criado até aqui.'''

import Moeda110

n = float(input("Digite um preço: R$"))
Moeda110.resumo(n, 20, 30)
