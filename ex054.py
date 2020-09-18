cont = 0
for c in range(1, 8):
     ano = int(input('Digite o ano de nascimento do {}:'.format(c)))
     if 2020 - ano < 18:
         print('ela é menor de idade')
         cont = cont + 1
     else:
         print('Ele é maior de idade')
print('{} pessoas não atigiram a maioridade'.format(cont))

