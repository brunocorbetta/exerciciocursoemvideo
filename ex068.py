import random
cont = 0
while True:
    pc = random.randint(0, 6)
    pessoal = int(input('Digite um valor de 0 a 5: '))
    pi = str(input('PAR ou IMPAR? [P/I]: ')).strip().upper()
    soma = pc + pessoal
    if pi == 'P' and soma % 2 == 0:
        print('Você ganhou !')
        cont += 1
    elif pi == 'I' and soma % 2 == 1:
        print('Você ganhou !')
        cont += 1
    else:
        break
print(f'Você perdeu, mas no total você ganhou {cont} vezes.')