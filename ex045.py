import random
escolha = int(input('''Suas opções...
(1) - Pedra
(2) - Papel
(3) - Tesoura
Qual é a sua escolha? 
'''))
ia = random.randint(1,3)

if escolha == 1 and ia == 3:
    print('A inteligencia artificial escolheu {} tesoura, você ganhou!'. format(ia))
elif escolha == 1 and ia == 2:
    print('A inteligencia artificial escolheu {} papel, você perdeu'.format(ia))
elif escolha == 1 and ia == 1:
    print('A inteligencia artificial escolheu {} pedra, deu empate'.format(ia))
elif escolha == 2 and ia == 1:
    print('A inteligencia artificial escolheu {} pedra, você ganhou'.format(ia))
elif escolha == 2 and ia == 2:
    print('A inteligencia artificial escolheu {} papel, deu empate'.format(ia))
elif escolha == 2 and ia == 3:
    print('A inteligencia artificial escolheu {} tesoura, você perdeu'.format(ia))
elif escolha == 3 and ia == 1:
    print('A inteligencia artificial escolheu {} pedra, você perdeu'.format(ia))
elif escolha == 3 and ia == 2:
    print('A inteligencia artificial escolheu {} papel. você ganhoi'.format(ia))
elif escolha == 3 and ia == 3:
    print('A inteligencia artificial escolheu {} tesoura, deu empate.'.format(ia))
else:
    print('Escolha errada, escolha outro numero...')

