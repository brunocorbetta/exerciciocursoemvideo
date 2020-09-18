nove = 0
n1 = int(input('Digite um numero: '))
if n1 == 9:
    nove += 1
n2 = int(input('Digite um numero: '))
if n2 == 9:
    nove += 1
n3 = int(input('Digite um numero: '))
if n3 == 9:
    nove += 1
n4 = int(input('Digite um numero: '))
if n4 == 9:
    nove += 1
num = (n1, n2, n3, n4)
print(f'O numero nove aparece {nove} vezes.')
print(f'O numero 3 aparece na posição {num.index(3)}')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')



