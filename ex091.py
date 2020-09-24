from random import randint
from time import sleep
from  operator import itemgetter
jogo = {
    'jogador_1' : randint(1, 6),
    'jogador_2' : randint(1, 6),
    'jogador_3' : randint(1, 6),
    'jogador_4' : randint(1, 6)
}
ranking = []
print('Valores Sorteados:')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
print('=-' * 30)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse= True)
for i, v in enumerate(ranking):
    print(f'{i+1} Lugar: {v[0]} com {v[1]}.')