pt = int(input('Qual o primeiro termo? '))
r = int(input('Qual a razão da PA? '))
n = pt
print(' {}...'.format(n))
for c in range(1,10):
    n = n + r
    print(' {}...'.format(n))

"""
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10-1) * razão

for c in range(primeiro, décimo + razão, razão)
    print('{}'.format(c), end='...')
	
"""