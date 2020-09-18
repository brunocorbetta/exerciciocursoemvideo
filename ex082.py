lista1 = []
lista2 = []
lista3 = []
while True:
    lista1.append(int(input('Digite um numero: ')))
    resp = str(input('Quer Continuar [S/N]: '))
    if resp in 'Nn':
        break
for valor in lista1:
    if valor % 2 == 0:
        lista2.append(valor)
for valor in lista1:
    if valor % 2 == 1:
        lista3.append(valor)
print(f'lista original {lista1}')
print(f'Lista de pares {lista2}')
print(f'Lista impar {lista3}')