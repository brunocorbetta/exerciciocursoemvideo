total = 0
mil = 0
menor = 0
barato = ''
while True:
    nome_produto = str(input('Nome do produto: ')).upper()
    preco_produto = float(input('Preço do Produto: '))
    total += preco_produto
    if preco_produto >= 1000:
        mil += 1
    if mil == 1:
        menor = preco_produto
        barato = nome_produto
    else:
        if preco_produto < menor:
            menor = preco_produto
            barato = nome_produto
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
print(f'O valor total da compra é R${total}')
print(f'{mil} Produtos custam menos de R$ 1.000')
print(f'O produto mais barato foi {nome_produto} que custa R${menor}')

