ano = int(input('Digite um ano:'))
ano_bi = ano % 4
if ano_bi == 0:
    print('O ano {} é um ano bisexto'.format(ano))
else:
    print('O ano {} não é um ano bisexro'.format(ano))