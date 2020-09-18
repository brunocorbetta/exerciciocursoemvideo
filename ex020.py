import random
primeiro = input('Digite o primeiro aluno:')
segundo = input('Digite o segundo aluno:')
terceiro = input('Digite o terceiro aluno:')
quarto = input('Digite o quarto aluno:')
lista = [primeiro, segundo, terceiro, quarto]
random.shuffle(lista)
print('A ordem de apresentação será ')
print(lista)



