cont = 0
soma = 0
while True:
    n1 = int(input('Digite 999 para parar: '))
    if n1 == 999:
     break
    cont += 1
    soma += n1

print(f'Você digitou {cont} numeros e a soma deles da {soma} ')