from random import randint
from  time import sleep
def sorteia(list):
    print('Sorteando 5 valores da lista ', end='')
    for c in range(0, 5):
        n = randint(0, 100)
        list.append(n)
        sleep(0.5)
        print(f'{n}', end=' ')
    print('Pronto')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares da {lista}, temos {soma}')


numeros = []
sorteia(numeros)
somapar(numeros)
