'''Exercício Python 105: Faça um programa que tenha uma função notas() que
pode receber várias notas de alunos e vai retornar um dicionário com as seguintes
informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)'''


def notas(* nota, sit=False):
    """
    --> Função para analisar notas e situações de vários alunos.
    :param nota: Uma ou mais notas dos alunos (aceita várias)
    :param sit: (opciona) indica se deve adicionar a situação ou não
    :return: dicionário com várias informações sobre a situação da turma
    """
    dic_notas = dict()
    dic_notas['qtdade_notas'] = len(nota)
    dic_notas['maior_nota'] = max(nota)
    dic_notas['menor_nota'] = min(nota)
    dic_notas['média'] = sum(nota)/len(nota)

    if sit:
        if dic_notas['média'] >= 9:
            dic_notas['situação'] = 'ÓTIMA'
        elif dic_notas['média'] >= 7:
            dic_notas['situação'] = 'BOA'
        elif dic_notas['média'] >= 5:
            dic_notas['situação'] = 'RUIM'
        else:
            dic_notas['situação'] = 'PÉSSIMA'

    return dic_notas


resp = notas(9, 9.2, 3, 4, 7.5, sit=True)
print(resp)
