resposta = str (''.strip().upper())
soma = 0
cont = 0
while resposta == 'S':
    num = float(input('Digite um numero: '))
    resposta = str(input('Quer continuar: [S/N] ').strip().upper())
    soma = soma + num
    cont =+ 1
media = soma / cont
print('Você digitou {} numeros e a media entre eles é {}'.format(cont, media))
