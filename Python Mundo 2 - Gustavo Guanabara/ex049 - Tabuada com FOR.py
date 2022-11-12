n = int(input('De qual número você quer saber a tabuada? '))
print('-'*15)
print(' TABUADA DO ', n)
print('-'*15)

for c in range(1, 11):
    print(' {} x {:2} = {}'.format(n, c, n*c))