'''cont = 0
cont_m = 0
idade1 = 0
h_mais = ''
for c in range(1,5):
    nome = input('Nome do {} : '.format(c))
    idade = int(input('Idade do {} :'.format(c)))
    if idade > 1:
        idade1 = idade
        if idade > idade1:
            h_mais = nome

    sexo = (input('Sexo M/F: ').upper())
    if sexo == 'F':
        cont_m = cont_m + 1
    cont = idade + cont
media = float(cont / 4)
print('A medio de Idade do Grupo é {} anos '.format(media))
print('Tem {} mulheres do grupo.'.format(cont_m))
print(h_mais)'''

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('-----{}ª Pessoa -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade / 4
print('A media de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {} '.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos. '.format(totmulher20))
