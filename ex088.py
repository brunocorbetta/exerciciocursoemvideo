'''from random import randint
mega = []
for c in range(0, 6):
    mega.append(randint(0, 60))
print(mega)'''

from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print('      JOGA NA MEGA SENA      ')
print('-' * 30)
quant = int(input('Quantos jogos quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'Sorteando {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(2)
print('-=' * 5, 'Boa Sorte!', '-=' *5)

