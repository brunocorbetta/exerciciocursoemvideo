altura = float(input('digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
tinta = area / 2
print('A area da parede é de {:0.3}m²'.format(area))
print('É necessario {:0.3} litros de tinta para pintar a parede'.format(tinta))

