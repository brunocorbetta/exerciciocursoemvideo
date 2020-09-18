ano = int(input('Em que ano você nasceu: '))
idade = 2020 - ano
if idade < 18:
    print('Falta {} anos para você se alistar.'.format(18 - idade))
elif idade == 18:
    print('Você tem que se alistar esse ano')
else:
    print('Ja passou {} anos do periodo de alistamento.'.format(idade - 18))
    print('Você tem {} anos.' .format(idade))