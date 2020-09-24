lista = list()
par = []
impar = []
for c in range(0,7):
    lista.append(int(input(f'Digite o {c +1}ª. valor: ')))
for pos in lista:
    if pos % 2 == 0:
        par.append(pos)
    else:
        impar.append(pos)
print(lista)
print(par)
print(impar)