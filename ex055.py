maior = 0
menor = 0
for c in range(1,6):
    peso = eval(input('Qual e o peso do {}: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}KG'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))