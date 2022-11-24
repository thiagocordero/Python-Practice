'''Exercício Python 083: Crie um programa onde o usuário digite uma
expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a
expressão passada está com os parênteses abertos e fechados na ordem correta.'''

exp = str(input("Digite uma expressão matemática: "))
pilha = []
for letra in exp:
    if letra == '(':
        pilha.append('(')
    elif letra == ')':
        if len(pilha) > 0:
            pilha.pop()
if len(pilha) == 0:
    print("Expressão válida!")
else:
    print("Expressão Inválida!")

