print('====================')
print('10 Termos de uma PA  ')
print('====================')
pt = int(input('Primeiro Termo:'))
razao = int(input('Razao: '))
decimo = pt + (10-1) *razao
for x in range(pt, decimo + razao, razao):
    print('{}'.format(x), end='-> ')
print('Acabou')



