aluno = {}
aluno['nome'] = str(input('Digite o nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
print('-=' * 30)
if aluno['media'] >= 7:
    aluno['situação'] = 'aprovado'
elif aluno['media'] >= 5 and aluno['media'] < 7:
    aluno['situação'] = 'recuperação'
else: aluno['situação'] = 'reprovado'

for k , v in aluno.items():
    print(f'{k} e igual a {v}')