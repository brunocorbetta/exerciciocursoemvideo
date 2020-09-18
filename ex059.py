n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('digite o segundo valor: '))
escolha = 0
while escolha != 5:
    print('''
    Escolha um modulo...
    [1] Somar
    [2] Multiplicar
    [3] maior
    [4] Novo numeros
    [5] Sair do programa ''')
    escolha = float(input('Sua escolha: '))
    if escolha == 1:
        print('A soma entre  {} e {} é {}'.format(n1, n2, n1 + n2))
    elif escolha == 2:
        print('a multiplicação entre {} e {} é {}'.format(n1, n2, n1 * n2))
    elif escolha == 3:
        print('Entre os dois numeros que você digitou o maio é o {}'.format(max(n1, n2)))
    elif escolha == 4:
        print('Informe os numeros novamente...')
        n1 = float(input('Digite o primeiro numero: '))
        n2 = float(input('Digite o segunto numero: '))
print('Ate mais')


