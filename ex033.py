a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
if a<b and a<c:
    menor = a
if b<c and b<a:
    menor = b
if c<a and c<b:
    menor = c

maior = a
if b> a and b>c:
    maior = b
if c> a and c> b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))