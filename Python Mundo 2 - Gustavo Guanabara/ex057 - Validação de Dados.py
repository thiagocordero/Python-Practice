

genero = str(input("Digite seu gênero (M/F/NB): ")).strip().upper()

while genero not in ["M", "F", "NB"]:
    genero = str(input("Dados inválidos. Por favor, digite seu gênero (M/F/NB) : ")).strip().upper()
print("Gênero {} registrado com sucesso".format(genero))

idade = int(input("Digite sua idade: "))