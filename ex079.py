'''valores = []
for num in range(0, 6):
    valores.append(int(input('Digite um numero: ')))
    if num in valores:
        valores.pop()
        print('Numero não adicionado...')
valores.sort()
print(valores)'''

numeros = list()
while True:
    n = int(input('Digite um Numero: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor acionado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar...')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}')
