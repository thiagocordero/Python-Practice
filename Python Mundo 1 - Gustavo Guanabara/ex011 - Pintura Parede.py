altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = altura * largura
litros_tinta = area / 2
print('A sua parede tem {}x{} de dimensao e um total de {}m².'.format(largura, altura, area))
print('Você precisa de {} LITROS de tinta.'.format(litros_tinta))