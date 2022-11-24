''' Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros 
colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o Corinthians.'''

campeonato = ("Palmeiras", "Internacional", "Fluminense", "Corinthians",
              "Flamengo", "Athetico-PR", "Atlético-MG", "Botafogo",
              "América-MG", "Fortaleza", "São Paulo", "Santos", "Goiás",
              "Bragantino", "Coritiba", "Cuiabá", "Avaí", "Atlético-GO",
              "Ceará SC", "Juventude")

print("-="*15)
print(f"Lista de Times Brasileirão: {campeonato}")
print("-="*15)

# a) 5 primeiros colocado
print(f"Os 5 primeiro colocado são: {campeonato[0:5]}")
print("-="*15)

#b) Os últimos 4 colocados.
print(f"Os 4 últimos colocados são: {campeonato[-4:]}")
print("-="*15)

#c) Times em ordem alfabética.
print(f"Times em ordem alfabética: {sorted(campeonato)}")
print("-="*15)

#d) Em que posição está o Corinthians
print(f"O Corinthians está na {campeonato.index('Corinthians')+1}° posição.")