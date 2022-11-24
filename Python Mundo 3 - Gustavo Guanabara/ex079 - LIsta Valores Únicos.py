'''Exercício Python 079: Crie um programa onde o usuário possa digitar
vários valores numéricos e cadastre-os em uma lista. Caso o número já
exista lá dentro, ele não será adicionado. No final, serão exibidos todos
os valores únicos digitados, em ordem crescente.'''

valoresUnicos = list()
while True:
    n = int(input("Digite um numero para adicionar: "))
    if n in valoresUnicos:
        print(f"Valor duplicado, não foi possível adicionar.")
    else:
        valoresUnicos.append(n)
        print(f"{n} adicionado com sucesso!")
    option = str(input("Deseja continuar [S/N]? ")).upper()[0]
    if option == "N":
        break
print("=-"*30)
print(f"A lista final foi: {sorted(valoresUnicos)}")
print("=-"*30)




