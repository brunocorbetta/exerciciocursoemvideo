from time import sleep

def contador(i, f, p):
    print(f'Contagem de {i} ate o {f} de {p} ')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM!!!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM!!!')

contador(1, 10, 1)
contador(10, 0, 2)