distance = float(input('Qual e a distancia do seu distino?'))
if distance <= 200:
    print('O valor da passagem é R$ {} referente a {}Km'.format(distance * 0.5, distance))
else:
    print('O valor da passagem é R$ {} referente a {}Km'.format(distance * 0.45, distance))