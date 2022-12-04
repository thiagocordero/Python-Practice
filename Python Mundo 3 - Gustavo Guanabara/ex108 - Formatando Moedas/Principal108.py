import Moeda108

n = float(input("Digite um preço: R$"))
print(f"A metade de {Moeda108.moeda(n)} é {Moeda108.moeda(Moeda108.metade(n))}")
print(f"O dobro de {Moeda108.moeda(n)} é {Moeda108.moeda(Moeda108.dobro(n))}")
print(f"Aumentando {10}% temos {Moeda108.moeda(Moeda108.aumento(n, 10))}")
print(f"Com um desconto de {10}% sai por {Moeda108.moeda(Moeda108.desconto(n, 10))}")
