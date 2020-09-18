vel_car = float(input('Qual a velocidade do carro?'))
multa = (vel_car - 80) * 7
if vel_car >= 80:
    print('Você foi multado')
    print('O valor da multa é R$ {}'. format(multa))
else:
    print('Siga em frente!')
