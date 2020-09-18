'''pessada = []
leve = []
cont = 0
while True:
    nome = str(input('Digite O nome: '))
    peso = int(input('Digite o peso: '))
    cont += 1
    if peso > 70:
        pessada.append(nome)
    else:
        leve.append(nome)
    resp = str(input('Quer Continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('=-' * 30)
print(f'Foram cadastradas {cont} pessoas.')
print(f'Os mais pessados acima de 70 Kg são {pessada}')
print(f'O mais leves abaixo de 70 kg são {leve}')'''
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar: [N/S}: '))
    if resp in 'Nn':
        break
print('=-' * 30)
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}Kg')
for p in princ:
    if p[1] == mai:
        print(f'O menor peso foi de {men}Kg')