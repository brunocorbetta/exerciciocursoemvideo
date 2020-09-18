import random
cont = 0
print('Vou pensar em um numero de 0 a 10')
num_pc = random.randint(0, 10)
num = int(input('Qual numero eu pensei? '))
while num != num_pc :
    print('Você errou, tente novamente...')
    num = int(input('Qual numero eu pensei? '))
    cont = cont + 1
print('Eu pensei no {}, parabens você ganhou'.format(num_pc))
print('Você tentou {} vezes'.format(cont))

