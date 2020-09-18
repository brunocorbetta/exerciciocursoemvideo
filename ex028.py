import random
print('Vou pensar em um numero de 0 a 5....')
number = random.randint(0,5)
user_number = int(input('Que numero eu pensei? '))
if number == user_number:
    print('Você acertou parabens!!!')
else: print('Você errou!!! eu pensei no numero {}'.format(number))
