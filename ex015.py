km = float(input('Quantos KM foram percorridos:'))
day = float(input('Quantos dias o carro foi alugado:'))
valor = (day * 60) + (km * 0.15)
print('O valor a ser pago é R${:0.2f}'.format(valor))