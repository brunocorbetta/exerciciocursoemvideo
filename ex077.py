n1 = ('deca', 'stano', 'durateston', 'testex')
for vogal in n1:
    print(f'\nNa palavra {vogal.upper()} temos ', end=' ')
    for letra in vogal:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

