valor = 1
cont = 0
tentativas = 0
while valor != 999:
    valor = int(input('Digite 999 para parar: '))
    if valor != 999:
        cont += valor
        tentativas += 1
print('Você digitou {} vezes e o total é {}'.format(tentativas, cont))


    