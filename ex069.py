maior = 0
homem = 0
mulher_menor = 0
while True:
    idade = int(input('Qual é a idade: '))
    if idade > 18:
        maior += 1
    sexo = str(input('Sexo [M/F}: ')).strip().upper()
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher_menor += 1
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if continuar == 'N':
        break
print(f'Temos {maior} pessoas com mais de 18 anos')
print(f'Foram cadastrados {homem} homens.')
print(f'Foram cadastradas {mulher_menor} mulheres menores de 20 anos.')