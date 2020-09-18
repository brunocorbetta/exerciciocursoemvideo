braileirao = ('internacional', 'flamengo', 'são paulo', 'plameiras',
              'atletico-mg', 'vasco', 'santos', 'fortaleza', 'fluminense',
              'atletico-pr', 'gremio', 'sport', 'ceara', 'corinthians',
              'atletico - go', 'bahia', 'botafogo', 'coritiba', 'bragantino',
              'goias')
print(f'Os cincos pimeiros do campeonato são {braileirao[0:6]}')
print(f'Os quatro ultimos colocados são {braileirao[16:21]}')
print(sorted(braileirao))
print('O São paulo esta na {} posição'.format(braileirao.index('são paulo')+1))
