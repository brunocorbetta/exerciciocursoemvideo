text = str(input('Digite uma frase: '))
print('A letra "a" aparece {} vezes'.format(text.count('a')))
print('Aparce pela primeira vez na {} posição'.format(text.find('a')))
print('Pela ultima vez aparece na posição {}'.format(text.rfind('a')))