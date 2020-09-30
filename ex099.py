from time import sleep
def maior(*num):
    cont = maior = 0
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1

    print(f'Foram informado {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 5, 4, 3, 2)
maior(3, 4, 6, 8)
maior(0, 3)
maior()