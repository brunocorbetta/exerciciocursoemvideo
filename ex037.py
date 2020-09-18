number = int(input('Escolha um numero inteiro:'))
chose = int(input('Para converter binario (1)  octal(2) exdecimal(3) '))
if chose == 1:
    chose = bin(number)[2:]
elif chose == 2:
    chose = oct(number)[2:]
elif chose == 3:
    chose = hex(number)[2:]

print(chose)


