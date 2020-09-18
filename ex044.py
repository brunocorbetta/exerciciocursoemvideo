produto = float(input('Qual é o valor do produto: '))
condicao = int(input('''Forma de pagamento:
(1) - à vista
(2) - à vista no cartão
(3) - 2x no cartão
(4) - 3x no cartão

digite aqui: '''))
if condicao == 1:
    print('O valor final do produto é R${}'.format(produto - (produto / 100 * 10)))
elif condicao == 2:
    print('O valor final do produto é R${}'.format(produto - (produto / 100 * 5)))
elif condicao == 3:
    print('O valor final do produto é R${}'.format(produto))
elif condicao == 4:
    print('O valor final do produto é R${}'.format(produto + (produto /100 *20)))
else:
    print('Valor digitado incorreto, tente novamente.')