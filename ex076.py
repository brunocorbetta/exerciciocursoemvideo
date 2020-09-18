suplemento = ('Whey Protein', 77.66, 'Creatina', 45.60, 'Multivitaminico', 27.90,
              'Glutamina', 50.55, 'Pre=treino', 120.21, 'Melatonina', 91.65)
print('-' * 30)
print('Listagem de Preços')
print('-' * 30)
for pos in range(0, len(suplemento)):
    if pos % 2 == 0:
        print(f'{suplemento[pos]:.<30}', end=' ')
    else:
        print(f'R${suplemento[pos]:>7}')