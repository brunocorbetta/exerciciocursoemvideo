while True:
    numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
               'seis','sete', 'oito', 'nove', 'dez', 'onze', 'doze',
               'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
               'dezoito', 'dezenove', 'vinte')
    num = int(input('Digite um numero de 0 a 20: '))
    if num <= 20:
        print(f'Você digitou {numeros[num]}')
        break

    else:
        print('Digite novemente...')