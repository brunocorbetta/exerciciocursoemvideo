n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Aluno reprovado!')
elif media >= 5.0 and media < 6.9:
    print('Aluno em recuperação!')
else:
    print('Aluno aprovado!')
