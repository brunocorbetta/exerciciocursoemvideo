jogador = {}
partidas = []
time = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input("Quer continuar? [S/N]"))
        if resp in 'SN':
            break
        print('Erro! responda apenas S ou N. ')
    if resp in 'Nn':
        break
print('-=' * 40)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 40)

'''Voltar aqui'''


