ano = int(input('Ano de nascimento do atleta:'))
idade = 2020 - ano
if idade <= 9:
    print('O atleta tem {} anos e  está na categoria mirim'.format(idade))
elif idade > 9 and idade <= 14:
    print('O atleta tem {} anos e está na categoria Infantil'.format(idade))
elif idade > 14 and idade <= 19:
    print('O atleta tem {} anos e está na categooria Junior'.format(idade))
elif idade > 19 and idade <= 25:
    print('O atleta tem {} anos e está na categoria Senior'.format(idade))
else:
    print('O atleta tem {} anos e está na categoria Mater'.format(idade))