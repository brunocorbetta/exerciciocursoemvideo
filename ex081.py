lista = []
cont = 0
while True:
    lista.append(int(input('Digite um numero: ')))
    cont += 1
    resp = str(input('Quer continuar [S/N]: ').strip().upper())
    if resp in 'Nn':
        break
print(f'Foram digitados {cont} numeros.')
lista.sort(reverse = True)
print(lista)
if 5 in lista:
    print('O numero 5 foi digitado')
else:
    print('O numero 5 não foi digitado...')
